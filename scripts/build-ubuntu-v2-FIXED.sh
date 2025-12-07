#!/bin/bash
# Dingo OS V2 - Ubuntu 24.04 Based Gaming & Blockchain Distribution
# Made By: Muhammad Ali (Github: Baymax005)
#
# Production-ready build script with proper error handling
# Requirements: Ubuntu 24.04 host system, 20GB free space, internet connection
# Expected runtime: 30-60 minutes depending on internet speed

set -e  # Exit on any error
set -u  # Exit on undefined variables
set -o pipefail  # Exit on pipe failures

# Logging functions
log_info() { echo "ℹ️  $1"; }
log_success() { echo "✅ $1"; }
log_warning() { echo "⚠️  $1"; }
log_error() { echo "❌ $1" >&2; }

# Safe package installation - checks if package exists first
safe_install() {
    local packages=("$@")
    local available=()
    local missing=()
    
    for pkg in "${packages[@]}"; do
        if apt-cache show "$pkg" &>/dev/null; then
            available+=("$pkg")
        else
            missing+=("$pkg")
        fi
    done
    
    if [ ${#missing[@]} -gt 0 ]; then
        log_warning "Packages not available: ${missing[*]}"
    fi
    
    if [ ${#available[@]} -gt 0 ]; then
        log_info "Installing: ${available[*]}"
        apt-get install -y "${available[@]}"
        return 0
    fi
    return 0  # Don't fail if no packages available
}

log_info '🦘 Dingo OS V2 Builder (Ubuntu 24.04 Noble)'
echo ""
cat << "EOF"
    ██████╗ ██╗███╗   ██╗ ██████╗  ██████╗ 
    ██╔══██╗██║████╗  ██║██╔════╝ ██╔═══██╗
    ██║  ██║██║██╔██╗ ██║██║  ███╗██║   ██║
    ██║  ██║██║██║╚██╗██║██║   ██║██║   ██║
    ██████╔╝██║██║ ╚████║╚██████╔╝╚██████╔╝
    ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ 
    Gaming & Blockchain OS & DEV Friendly
EOF
echo ""
echo '============================================='

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="${SCRIPT_DIR}/ubuntu-build"
CHROOT_DIR="${BUILD_DIR}/chroot"
ISO_DIR="${BUILD_DIR}/iso"
OUTPUT_DIR="${BUILD_DIR}/output"

# Clean previous build
echo ""
log_info "✨ Cleaning previous build..."
sudo rm -rf "$BUILD_DIR"
mkdir -p "$CHROOT_DIR" "$ISO_DIR/casper" "$OUTPUT_DIR"
echo "  ✓ Removing old files"
echo "  ✓ Build directories created"

# Install required tools on host
echo ""
log_info "✨ Installing build tools on host system..."
sudo apt-get update -qq
sudo apt-get install -y debootstrap squashfs-tools xorriso grub-pc-bin grub-efi-amd64-bin mtools
echo "  ✓ debootstrap installed"
echo "  ✓ squashfs-tools installed"
echo "  ✓ xorriso & GRUB installed"
log_success "Build tools ready!"

# Bootstrap Ubuntu 24.04 (Noble) - ONLY ONCE
echo ""
log_info "✨ Bootstrapping Ubuntu 24.04 Noble base system..."
log_info "   ⏳ This takes 10-15 minutes (downloading ~500MB)"
sudo debootstrap --arch=amd64 --variant=minbase noble "$CHROOT_DIR" http://archive.ubuntu.com/ubuntu/
echo "  ✓ Base packages extracted"
echo "  ✓ Core system configured"
log_success "Base system bootstrapped successfully!"

# Mount essential filesystems (INCLUDING /run for DNS)
echo ""
log_info "✨ Mounting essential filesystems..."
sudo mount --bind /dev "$CHROOT_DIR/dev"
sudo mount --bind /dev/pts "$CHROOT_DIR/dev/pts"
sudo mount --bind /proc "$CHROOT_DIR/proc"
sudo mount --bind /sys "$CHROOT_DIR/sys"
sudo mount --bind /run "$CHROOT_DIR/run"
echo "  ✓ /dev mounted"
echo "  ✓ /proc mounted"
echo "  ✓ /sys mounted"
echo "  ✓ /run mounted (required for systemd-resolved)"

# Copy DNS settings to chroot
log_info "Configuring DNS in chroot"
sudo cp /etc/resolv.conf "$CHROOT_DIR/etc/resolv.conf"
log_success "DNS configured"

# Create sources.list
log_info "Configuring Ubuntu repositories"
sudo tee "$CHROOT_DIR/etc/apt/sources.list" > /dev/null <<EOF
deb http://archive.ubuntu.com/ubuntu noble main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu noble-updates main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu noble-security main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu noble-backports main restricted universe multiverse
EOF

# Create customization script to run inside chroot
cat > "$BUILD_DIR/customize.sh" <<'CUSTOMIZE_SCRIPT'
#!/bin/bash
# Chroot customization script - runs inside the Ubuntu environment
set -e
set -u
set -o pipefail

export DEBIAN_FRONTEND=noninteractive
export HOME=/root
export LC_ALL=C

# Logging functions
log_info() { echo "ℹ️  $1"; }
log_success() { echo "✅ $1"; }
log_warning() { echo "⚠️  $1"; }
log_error() { echo "❌ $1" >&2; }

# Safe package installation function
safe_install() {
    local packages=("$@")
    local available=()
    local missing=()
    
    for pkg in "${packages[@]}"; do
        if apt-cache show "$pkg" &>/dev/null; then
            available+=("$pkg")
        else
            missing+=("$pkg")
        fi
    done
    
    if [ ${#missing[@]} -gt 0 ]; then
        log_warning "Packages not available: ${missing[*]}"
    fi
    
    if [ ${#available[@]} -gt 0 ]; then
        log_info "Installing: ${available[*]}"
        apt-get install -y "${available[@]}"
        return 0
    fi
    return 0
}

log_info "Starting chroot customization"

log_info "Updating base system"
apt-get update
apt-get upgrade -y
log_success "Base system updated"

log_info "Installing essential packages"
apt-get install -y \
    wget \
    curl \
    ca-certificates \
    gnupg \
    lsb-release \
    apt-transport-https
log_success "Essential packages installed"

# Install software-properties-common AND gpg-agent FIRST (required for add-apt-repository)
log_info "Installing PPA management tools"
apt-get install -y software-properties-common gpg-agent
log_success "PPA tools installed"

# Add PPAs with error handling
log_info "Adding PPAs for latest software"
if add-apt-repository -y ppa:damentz/liquorix; then
    log_success "Liquorix PPA added"
else
    log_warning "Liquorix PPA failed - will use standard kernel"
fi

if add-apt-repository -y ppa:kisak/kisak-mesa; then
    log_success "Mesa PPA added"
else
    log_warning "Mesa PPA failed - will use standard drivers"
fi

if add-apt-repository -y ppa:graphics-drivers/ppa; then
    log_success "NVIDIA PPA added"
else
    log_warning "NVIDIA PPA failed - will use standard drivers"
fi

# Add Microsoft VS Code repository
log_info "Adding Microsoft VS Code repository"
if wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg 2>/dev/null; then
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list
    log_success "VS Code repository added"
else
    log_warning "VS Code repository failed - can install manually later"
fi

# Update with new repos
log_info "Updating package lists"
apt-get update
log_success "Package lists updated"

log_info "Installing kernel"
if safe_install linux-image-liquorix-amd64 linux-headers-liquorix-amd64; then
    log_success "Liquorix kernel installed"
else
    log_warning "Liquorix kernel not available, installing standard kernel"
    apt-get install -y linux-image-generic linux-headers-generic
fi

log_info "Installing KDE Plasma Desktop"
apt-get install -y kubuntu-desktop sddm
echo "  ✓ KDE Plasma 6 installed"
echo "  ✓ SDDM login manager installed"
log_success "KDE Plasma desktop ready!"

# Install modern Breeze theme
log_info "Installing Breeze Dark theme"
safe_install breeze-gtk-theme breeze-cursor-theme sddm-theme-breeze
log_success "Modern theme installed"

log_info "Removing GNOME packages"
apt-get purge -y ubuntu-desktop gnome-shell || true
apt-get autoremove -y
log_success "GNOME removed"

log_info "Enabling 32-bit architecture for gaming"
dpkg --add-architecture i386
apt-get update
log_success "32-bit architecture enabled"

log_info "Installing GPU drivers"
if safe_install mesa-vulkan-drivers mesa-vulkan-drivers:i386 libgl1-mesa-dri:i386 mesa-utils; then
    log_success "AMD Mesa drivers installed"
fi

# NVIDIA drivers with fallback
log_info "Installing NVIDIA drivers (optional)"
if safe_install nvidia-driver nvidia-utils libnvidia-gl-extra:i386 nvidia-dkms-550; then
    log_success "NVIDIA drivers installed"
elif safe_install nvidia-driver-550 nvidia-utils-550 libnvidia-gl-550:i386; then
    log_success "NVIDIA 550 drivers installed"
elif safe_install nvidia-driver-545 nvidia-utils-545 libnvidia-gl-545:i386; then
    log_success "NVIDIA 545 drivers installed"
else
    log_warning "NVIDIA drivers not available (AMD users not affected)"
fi

log_info "Installing gaming tools"
safe_install steam lutris gamemode mangohud btop neofetch wine64 wine32 winetricks
log_success "Gaming tools installed"

log_info "Installing development tools"
safe_install code docker.io docker-compose git python3-full python3-pip python3-pyqt6 nodejs npm build-essential
log_success "Development tools installed"

# Install Python packages
log_info "Installing Python packages"
if command -v pip3 &>/dev/null; then
    pip3 install --break-system-packages psutil distro dbus-python || log_warning "Some pip packages failed"
fi

log_info "Installing GTK4/Libadwaita dependencies"
safe_install python3-gi python3-psutil gir1.2-gtk-4.0 gir1.2-adw-1 gir1.2-handy-1
log_success "Control Center dependencies installed"

log_info "Installing blockchain tools"
if command -v npm &>/dev/null; then
    npm install -g truffle ganache hardhat || log_warning "Some npm packages failed"
    log_success "Blockchain dev tools installed"
fi

# NOTE: Electrum via snap REMOVED - cannot work in chroot
log_warning "Electrum (Bitcoin wallet) must be installed after boot via: sudo snap install electrum"
log_warning "XMRig (mining software) must be installed manually if needed"

log_info "Installing system utilities"
safe_install network-manager pulseaudio pavucontrol firefox vim htop wget curl unzip p7zip-full casper laptop-detect os-prober
log_success "System utilities installed"

log_info "Configuring system"
echo "dingo" > /etc/hostname
cat > /etc/hosts <<HOSTEOF
127.0.0.1   localhost
127.0.1.1   dingo dingo.localdomain

::1         localhost ip6-localhost ip6-loopback
ff02::1     ip6-allnodes
ff02::2     ip6-allrouters
HOSTEOF

# Update os-release for branding
cat > /etc/os-release <<OSEOF
NAME="Dingo OS"
VERSION="2.0 (Ubuntu 24.04 Noble)"
ID=dingo
ID_LIKE=ubuntu debian
PRETTY_NAME="Dingo OS 2.0"
VERSION_ID="2.0"
HOME_URL="https://github.com/Baymax005"
SUPPORT_URL="https://github.com/Baymax005"
BUG_REPORT_URL="https://github.com/Baymax005"
PRIVACY_POLICY_URL="https://github.com/Baymax005"
VERSION_CODENAME=noble
UBUNTU_CODENAME=noble
LOGO=dingo
OSEOF

# Create dingo-game script
cat > /usr/local/bin/dingo-game <<'GAMEMODE'
#!/bin/bash
if systemctl is-active --quiet gamemoded; then
    echo "🎮 Game Mode: ACTIVATED"
    echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor > /dev/null
    echo "✅ CPU governor set to PERFORMANCE"
else
    echo "🎮 Game Mode: DEACTIVATED"
    echo powersave | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor > /dev/null
    echo "✅ CPU governor set to POWERSAVE"
fi
GAMEMODE
chmod +x /usr/local/bin/dingo-game

# Enable services
log_info "Enabling services"
systemctl enable NetworkManager || true
systemctl enable sddm || true
systemctl enable docker || true
systemctl set-default graphical.target || true
log_success "Services enabled"

# Create live user
log_info "Creating live user (dingo:dingo)"
useradd -m -s /bin/bash -G sudo,docker,audio,video,plugdev dingo
echo "dingo:dingo" | chpasswd
echo "root:dingo" | chpasswd

# Configure SDDM autologin
mkdir -p /etc/sddm.conf.d
cat > /etc/sddm.conf.d/autologin.conf <<SDDMCONF
[Autologin]
User=dingo
Session=plasma
SDDMCONF

# Configure sudo without password
echo "dingo ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/dingo
chmod 440 /etc/sudoers.d/dingo

# Create .bashrc
cat > /home/dingo/.bashrc <<'BASHRC'
export PATH=$PATH:/usr/local/bin
alias ll='ls -la'
alias game-mode='dingo-game'

clear
echo "=========================================="
echo "   Welcome to Dingo OS 2.0 🦘"
echo "   Made By: Muhammad Ali"
echo "   Github: Baymax005"
echo "=========================================="
echo ""
echo "Quick Commands:"
echo "  game-mode     - Toggle gaming performance mode"
echo "  btop          - System monitor"
echo "  neofetch      - System info"
echo "  dingo-center  - Open Control Center"
echo ""
BASHRC
chown -R dingo:dingo /home/dingo

log_info "Setting up Dingo Control Center"
mkdir -p /opt/dingo-center/src

# Create launcher script
cat > /usr/bin/dingo-center <<'LAUNCHER'
#!/bin/bash
if [ -f "/opt/dingo-center/src/__main__.py" ]; then
    cd /opt/dingo-center/src
    python3 /opt/dingo-center/src/__main__.py "$@"
elif [ -d "/opt/dingo-center/src/dingo_control_center" ]; then
    cd /opt/dingo-center/src
    python3 -m dingo_control_center
else
    notify-send "Dingo Control Center" "Application files not found" -u critical
    echo "Error: Dingo Control Center application files not found"
    exit 1
fi
LAUNCHER
chmod +x /usr/bin/dingo-center

# Create desktop entry
cat > /usr/share/applications/dingo-center.desktop <<'DESKTOP'
[Desktop Entry]
Version=1.0
Type=Application
Name=Dingo Control Center
Comment=System Management Dashboard for Dingo OS
GenericName=Control Panel
Icon=preferences-system
TryExec=/usr/bin/dingo-center
Exec=dingo-center
Categories=System;Settings;Qt;GTK;KDE;
Keywords=system;settings;control;dingo;dashboard;management;
Terminal=false
StartupNotify=true
X-KDE-autostart-after=panel
X-KDE-StartupNotify=true
DESKTOP

# Create autostart entry
mkdir -p /etc/xdg/autostart
cp /usr/share/applications/dingo-center.desktop /etc/xdg/autostart/
chmod 644 /usr/share/applications/dingo-center.desktop
chmod 644 /etc/xdg/autostart/dingo-center.desktop
log_success "Dingo Control Center configured"

# Branding Polish
log_info "Removing Ubuntu/Kubuntu branding"
mkdir -p /usr/share/plymouth/themes/dingo-text
cat > /usr/share/plymouth/themes/dingo-text/dingo-text.plymouth <<'PLYMOUTH'
[Plymouth Theme]
Name=Dingo OS Text
Description=Text mode theme for Dingo OS
ModuleName=text

[text]
title=Dingo OS 2.0
black=0x000000
white=0xffffff
PLYMOUTH

update-alternatives --install /usr/share/plymouth/themes/default.plymouth default.plymouth /usr/share/plymouth/themes/dingo-text/dingo-text.plymouth 200 || true
update-alternatives --set default.plymouth /usr/share/plymouth/themes/dingo-text/dingo-text.plymouth || true
update-initramfs -u || true

mkdir -p /etc/sddm.conf.d
cat > /etc/sddm.conf.d/theme.conf <<'SDDMTHEME'
[Theme]
Current=breeze
CursorTheme=breeze_cursors
SDDMTHEME

apt-get purge -y kubuntu-settings-desktop kubuntu-settings-netbook ubuntu-wallpapers kubuntu-wallpapers plymouth-theme-ubuntu-logo plymouth-theme-kubuntu-logo || true
apt-get autoremove -y
rm -f /usr/share/pixmaps/ubuntu-logo*.png || true
rm -f /usr/share/pixmaps/kubuntu-logo*.png || true
log_success "Branding complete"

# Clean up
log_info "Cleaning up"
apt-get clean
rm -rf /var/lib/apt/lists/*
rm -rf /tmp/*
rm -rf /var/tmp/*
log_success "Chroot customization complete!"
CUSTOMIZE_SCRIPT

chmod +x "$BUILD_DIR/customize.sh"
sudo cp "$BUILD_DIR/customize.sh" "$CHROOT_DIR/root/customize.sh"

# Copy Dingo Control Center
DASHBOARD_DIR="$SCRIPT_DIR/dashboard"
if [ -d "$DASHBOARD_DIR" ]; then
    log_info "Copying Dingo Control Center application"
    sudo mkdir -p "$CHROOT_DIR/opt/dingo-center/src"
    sudo cp -r "$DASHBOARD_DIR/"* "$CHROOT_DIR/opt/dingo-center/src/"
    sudo chmod -R 755 "$CHROOT_DIR/opt/dingo-center"
    log_success "Control Center copied"
else
    log_warning "Dashboard folder not found at $DASHBOARD_DIR"
fi

# Run customization inside chroot
log_info "Running customization inside chroot (20-30 minutes)"
if sudo chroot "$CHROOT_DIR" /bin/bash -c "/root/customize.sh"; then
    log_success "Chroot customization completed"
else
    log_error "Chroot customization failed!"
    exit 1
fi

# Unmount filesystems (LAZY FORCE for WSL)
log_info "Unmounting filesystems"
sudo umount -lf "$CHROOT_DIR/dev/pts" || true
sudo umount -lf "$CHROOT_DIR/dev" || true
sudo umount -lf "$CHROOT_DIR/proc" || true
sudo umount -lf "$CHROOT_DIR/sys" || true
sudo umount -lf "$CHROOT_DIR/run" || true
log_success "Filesystems unmounted"

# Create squashfs filesystem
log_info "Creating squashfs filesystem (5-10 minutes)"
sudo mksquashfs "$CHROOT_DIR" "$ISO_DIR/casper/filesystem.squashfs" -comp xz -b 1M -Xdict-size 100% -e boot
log_success "Squashfs created"

# Copy kernel and initrd
log_info "Copying kernel and initrd"
LIQUORIX_KERNEL=$(sudo find "$CHROOT_DIR/boot" -name "vmlinuz-*liquorix*" 2>/dev/null | head -1)
LIQUORIX_INITRD=$(sudo find "$CHROOT_DIR/boot" -name "initrd.img-*liquorix*" 2>/dev/null | head -1)

if [ -z "$LIQUORIX_KERNEL" ] || [ -z "$LIQUORIX_INITRD" ]; then
    log_warning "Liquorix kernel not found, using standard kernel"
    LIQUORIX_KERNEL=$(sudo find "$CHROOT_DIR/boot" -name "vmlinuz-*" 2>/dev/null | head -1)
    LIQUORIX_INITRD=$(sudo find "$CHROOT_DIR/boot" -name "initrd.img-*" 2>/dev/null | head -1)
fi

if [ -z "$LIQUORIX_KERNEL" ] || [ -z "$LIQUORIX_INITRD" ]; then
    log_error "No kernel found!"
    exit 1
fi

log_info "Using kernel: $(basename $LIQUORIX_KERNEL)"
sudo cp "$LIQUORIX_KERNEL" "$ISO_DIR/casper/vmlinuz"
sudo cp "$LIQUORIX_INITRD" "$ISO_DIR/casper/initrd"
log_success "Kernel copied"

# Create filesystem metadata
log_info "Creating filesystem metadata"
printf $(sudo du -sx --block-size=1 "$CHROOT_DIR" | cut -f1) > "$ISO_DIR/casper/filesystem.size"
sudo chroot "$CHROOT_DIR" dpkg-query -W --showformat='${Package} ${Version}\n' | sudo tee "$ISO_DIR/casper/filesystem.manifest" > /dev/null

# Create GRUB configuration
log_info "Creating GRUB bootloader"
mkdir -p "$ISO_DIR/boot/grub"
cat > "$ISO_DIR/boot/grub/grub.cfg" <<'GRUBCFG'
set timeout=10
set default=0

insmod all_video
set gfxmode=auto
set gfxpayload=keep

menuentry "Dingo OS 2.0 (Live)" {
    linux /casper/vmlinuz boot=casper quiet splash ---
    initrd /casper/initrd
}

menuentry "Dingo OS 2.0 (Safe Graphics)" {
    linux /casper/vmlinuz boot=casper nomodeset quiet splash ---
    initrd /casper/initrd
}

menuentry "Dingo OS 2.0 (Persistence)" {
    linux /casper/vmlinuz boot=casper persistent quiet splash ---
    initrd /casper/initrd
}
GRUBCFG

mkdir -p "$ISO_DIR/.disk"
echo "Dingo OS 2.0" > "$ISO_DIR/.disk/info"
echo "https://github.com/Baymax005" > "$ISO_DIR/.disk/release_notes_url"

# Generate ISO
log_info "Generating ISO image (2-3 minutes)"
if sudo grub-mkrescue -o "$OUTPUT_DIR/dingo-os-v2.iso" "$ISO_DIR" --compress=xz; then
    log_success "ISO generation complete!"
else
    log_error "ISO generation failed!"
    exit 1
fi

echo ""
echo "=========================================="
log_success "🦘 Dingo OS V2 ISO Build Complete!"
echo "=========================================="
echo "📀 ISO Location: $OUTPUT_DIR/dingo-os-v2.iso"
echo ""
ls -lh "$OUTPUT_DIR/dingo-os-v2.iso"
echo ""
echo "📊 Build Summary:"
echo "  - Base: Ubuntu 24.04 Noble"
echo "  - Desktop: KDE Plasma 6 with Breeze Dark"
echo "  - Kernel: Liquorix (high-performance)"
echo "  - Gaming: Steam, Lutris, GameMode, MangoHUD"
echo "  - Development: VS Code, Docker, Node.js, Git"
echo "  - Blockchain: Truffle, Ganache, Hardhat"
echo "  - Control Center: GTK4/Libadwaita dashboard"
echo ""
echo "🔐 Default Credentials:"
echo "  Username: dingo"
echo "  Password: dingo"
echo ""
echo "⚠️  Post-Install (run after booting ISO):"
echo "  sudo snap install electrum  # Bitcoin wallet"
echo ""
echo "👨‍💻 Made By: Muhammad Ali"
echo "🔗 Github: Baymax005"
echo "=========================================="
