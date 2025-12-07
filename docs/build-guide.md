# 🔨 Build Guide

Complete instructions for building Dingo OS 2.0 ISO from source.

---

## Prerequisites

### Build System Requirements

- **Ubuntu 24.04** host system (or WSL2 with Ubuntu 24.04)
- **20 GB** free disk space (build artifacts ~10GB, final ISO ~3.5GB)
- **4 GB RAM** minimum (8GB recommended for faster builds)
- **Internet connection** (downloads ~2-3GB of packages)
- **sudo privileges**

### Required Tools

The build script will install these automatically, but you can pre-install:

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install build tools
sudo apt install -y \
    debootstrap \
    squashfs-tools \
    xorriso \
    grub-pc-bin \
    grub-efi-amd64-bin \
    mtools
```

### For WSL2 Users

**Important**: Build must happen in Linux filesystem, NOT on Windows mount (`/mnt/c/`)

```bash
# ✅ Good: Native Linux filesystem
~/dingo-ubuntu/build-ubuntu-v2-FIXED.sh

# ❌ Bad: Windows NTFS mount (will cause tar extraction errors)
/mnt/c/Users/.../build-ubuntu-v2-FIXED.sh
```

---

## Getting the Source

```bash
# Clone the repository
git clone https://github.com/Baymax005/dingo-os.git
cd dingo-os
```

---

## Build Process

### Quick Build (Single Command)

```bash
# Create build directory in Linux filesystem
mkdir -p ~/dingo-ubuntu
cd ~/dingo-ubuntu

# Copy dashboard and build script
cp -r ~/dingo-os/dashboard ./
cp ~/dingo-os/scripts/build-ubuntu-v2-FIXED.sh ./

# Make executable
chmod +x build-ubuntu-v2-FIXED.sh

# Run build (takes 30-60 minutes)
sudo ./build-ubuntu-v2-FIXED.sh
```

---

## Build Stages

### Stage 1: Bootstrap Ubuntu 24.04 Noble (10-15 min)

Downloads and extracts minimal Ubuntu 24.04 base system (~500MB):

```bash
sudo debootstrap --arch=amd64 --variant=minbase noble chroot/ \
    http://archive.ubuntu.com/ubuntu/
```

**What's installed**: Essential system packages (bash, coreutils, apt, systemd, etc.)

### Stage 2: Mount Essential Filesystems

Prepares chroot environment:

```bash
sudo mount --bind /dev chroot/dev
sudo mount --bind /proc chroot/proc
sudo mount --bind /sys chroot/sys
sudo mount --bind /run chroot/run  # Required for DNS
```

**Note**: `/run` mount is critical for systemd-resolved DNS in Ubuntu 24.04

### Stage 3: Chroot Customization (20-30 min)

Enters chroot and installs all packages:

#### 3.1 System Update
```bash
apt-get update && apt-get upgrade -y
```

#### 3.2 Add PPAs
- **Liquorix** - High-performance kernel
- **Kisak Mesa** - Latest AMD drivers
- **Graphics Drivers** - NVIDIA drivers
- **Microsoft** - VS Code official repo

#### 3.3 Install Kernel
```bash
# Liquorix (high-performance) or fallback to generic
apt-get install -y linux-image-liquorix-amd64 linux-headers-liquorix-amd64
```

#### 3.4 Install KDE Plasma Desktop
```bash
apt-get install -y kubuntu-desktop sddm
apt-get install -y breeze-gtk-theme breeze-cursor-theme sddm-theme-breeze
```

**Total size**: ~5GB with KDE Plasma 6, themes, applications

#### 3.5 Enable 32-bit Architecture (for Gaming)
```bash
dpkg --add-architecture i386
apt-get update
```

#### 3.6 Install GPU Drivers
- **AMD**: mesa-vulkan-drivers, mesa-vulkan-drivers:i386, libgl1-mesa-dri:i386
- **NVIDIA**: nvidia-driver-550 or 545 with i386 support

#### 3.7 Install Gaming Tools
```bash
apt-get install -y steam lutris gamemode mangohud wine64 wine32 winetricks
```

#### 3.8 Install Development Tools
```bash
apt-get install -y code docker.io docker-compose git python3-full \
    python3-pip python3-pyqt6 nodejs npm build-essential
```

#### 3.9 Install Blockchain Tools (npm global)
```bash
npm install -g truffle ganache hardhat
```

#### 3.10 System Configuration
- Hostname: `dingo`
- OS branding in `/etc/os-release`
- Create user `dingo:dingo` with sudo access
- SDDM auto-login configuration
- Docker group membership
- Custom `dingo-game` performance script

#### 3.11 Copy Control Center
```bash
cp -r dashboard/src/dingo_control_center /opt/dingo-center/
```

Creates launcher at `/usr/bin/dingo-center` with autostart

#### 3.12 De-branding
- Custom Plymouth boot theme (Dingo OS text)
- Remove kubuntu-settings, ubuntu-wallpapers
- Remove plymouth-theme-ubuntu-logo, plymouth-theme-kubuntu-logo
- Clean SDDM to Breeze theme only

### Stage 4: Unmount & Create SquashFS (5-10 min)

```bash
# Unmount filesystems (lazy force for WSL compatibility)
umount -lf chroot/dev chroot/proc chroot/sys chroot/run

# Compress root filesystem (xz compression, ~3.5GB output)
mksquashfs chroot/ iso/casper/filesystem.squashfs \
    -comp xz -b 1M -Xdict-size 100% -e boot
```

**Compression ratio**: ~10GB chroot → ~3.5GB squashfs

### Stage 5: Copy Kernel & Initrd

```bash
# Find Liquorix kernel (or fallback to generic)
cp chroot/boot/vmlinuz-*liquorix* iso/casper/vmlinuz
cp chroot/boot/initrd.img-*liquorix* iso/casper/initrd
```

### Stage 6: Create Filesystem Metadata

```bash
# Size file for live installer
du -sx --block-size=1 chroot/ | cut -f1 > iso/casper/filesystem.size

# Package manifest (for debugging)
chroot chroot/ dpkg-query -W > iso/casper/filesystem.manifest
```

### Stage 7: Generate ISO (2-3 min)

Creates GRUB bootloader and packages ISO:

```bash
grub-mkrescue -o output/dingo-os-v2.iso iso/ --compress=xz
```

**Boot modes**:
- UEFI (recommended)
- Legacy BIOS
- Secure Boot compatible

---

## Build Output

### Success Message

```
==========================================
✅ 🦘 Dingo OS V2 ISO Build Complete!
==========================================
📀 ISO Location: ~/dingo-ubuntu/ubuntu-build/output/dingo-os-v2.iso

-rw-r--r-- 1 user user 3.5G Dec  7 05:07 dingo-os-v2.iso

📊 Build Summary:
  - Base: Ubuntu 24.04 Noble
  - Desktop: KDE Plasma 6 with Breeze Dark
  - Kernel: Liquorix (high-performance)
  - Gaming: Steam, Lutris, GameMode, MangoHud
  - Development: VS Code, Docker, Node.js, Git
  - Blockchain: Truffle, Ganache, Hardhat
  - Control Center: GTK4/Libadwaita dashboard

🔐 Default Credentials:
  Username: dingo
  Password: dingo
```

### Directory Structure

```
~/dingo-ubuntu/ubuntu-build/
├── chroot/                          # Full Ubuntu system (10GB)
│   ├── boot/                        # Kernels and initrd
│   ├── etc/                         # System configuration
│   ├── home/dingo/                  # User home
│   ├── opt/dingo-center/            # Control Center
│   └── usr/                         # Installed packages
├── iso/                             # ISO staging area
│   ├── boot/grub/                   # GRUB bootloader config
│   ├── casper/
│   │   ├── filesystem.squashfs      # Compressed root (3.5GB)
│   │   ├── filesystem.size          # Size metadata
│   │   ├── vmlinuz                  # Kernel
│   │   └── initrd                   # Initial ramdisk
│   └── .disk/                       # ISO metadata
└── output/
    └── dingo-os-v2.iso              # Final bootable ISO (3.5GB)
```

---

## Verification

### Check ISO Integrity

```bash
# File info
ls -lh ~/dingo-ubuntu/ubuntu-build/output/dingo-os-v2.iso

# Verify it's a valid ISO
file ~/dingo-ubuntu/ubuntu-build/output/dingo-os-v2.iso
# Output: ISO 9660 CD-ROM filesystem data 'dingo-os-v2'

# Generate checksum
sha256sum ~/dingo-ubuntu/ubuntu-build/output/dingo-os-v2.iso > dingo-os-v2.iso.sha256
```

### Test Boot

#### QEMU (Quick Test)
```bash
qemu-system-x86_64 \
    -cdrom ~/dingo-ubuntu/ubuntu-build/output/dingo-os-v2.iso \
    -m 4096 \
    -enable-kvm \
    -boot d \
    -cpu host \
    -smp 2
```

#### VMware Workstation
1. Create new VM → **Ubuntu 64-bit**
2. Firmware: **UEFI** (recommended) or BIOS
3. RAM: **4GB** minimum (8GB for full experience)
4. Disk: **20GB+** (if installing to disk)
5. CD/DVD → Use ISO image → Browse to `dingo-os-v2.iso`
6. Start VM → Boot from CD

#### VirtualBox
1. New → Name: Dingo OS → Type: **Linux** → Version: **Ubuntu (64-bit)**
2. RAM: **4096 MB**
3. Create virtual hard disk: **20GB VDI** (if installing)
4. Settings → Storage → Controller: IDE → Add CD/DVD → Choose `dingo-os-v2.iso`
5. Settings → System → Enable EFI
6. Start

---

## Troubleshooting

### Build Errors

#### DNS Resolution Failed in Chroot
```bash
# Symptom: "Temporary failure in name resolution"
# Fix: Ensure /run is mounted and resolv.conf copied
sudo mount --bind /run chroot/run
sudo cp /etc/resolv.conf chroot/etc/resolv.conf
```

#### PPA Addition Failed
```bash
# Symptom: "add-apt-repository: command not found"
# Fix: Install software-properties-common first
apt-get install -y software-properties-common gpg-agent
```

#### Tar Extraction Error in debootstrap
```bash
# Symptom: "E: Tried to extract package, but tar failed"
# Cause: Building on Windows NTFS mount in WSL
# Fix: Build in native Linux filesystem
mkdir -p ~/dingo-ubuntu  # NOT /mnt/c/...
```

#### Kernel Not Found
```bash
# Symptom: "No kernel found!" during ISO generation
# Check: Look for any kernel
ls -la chroot/boot/vmlinuz-*
# If missing, kernel installation failed - check apt logs
```

#### Control Center Missing
```bash
# Symptom: "Dashboard folder not found"
# Fix: Ensure dashboard/ is in build directory
cp -r ~/dingo-os/dashboard ~/dingo-ubuntu/
```

### Runtime Issues

#### ISO Won't Boot
- Check UEFI/BIOS settings
- Try alternate firmware mode
- Verify ISO checksum matches

#### Black Screen After Boot
- Try "Safe Graphics" boot option in GRUB
- NVIDIA users: nomodeset kernel parameter may be needed

#### Auto-login Not Working
- Check `/etc/sddm.conf.d/autologin.conf` in live session
- Verify User=dingo and Session=plasma

---

## Advanced Configuration

### Custom Package List

Edit the chroot customization section in `build-ubuntu-v2-FIXED.sh`:

```bash
# Add your packages here
safe_install your-package-name another-package

# Or remove unwanted ones
# Comment out: apt-get install -y steam lutris
```

### Custom Branding

Replace branding files before build:

```bash
# Custom Plymouth theme
cp your-theme.plymouth branding/plymouth/dingo.plymouth

# Custom wallpapers
cp your-wallpaper.jpg branding/imgs/
```

### Rebuild After Changes

```bash
# Clean previous build
sudo rm -rf ~/dingo-ubuntu/ubuntu-build

# Re-run build script
sudo ./build-ubuntu-v2-FIXED.sh
```

---

## Build Performance

| Stage | Time | Notes |
|-------|------|-------|
| Bootstrap Ubuntu | 10-15 min | Depends on download speed (~500MB) |
| Install packages | 15-20 min | Depends on internet (downloads ~2GB) |
| GPU drivers | 2-5 min | NVIDIA takes longer than AMD |
| Blockchain tools | 1-2 min | npm global installs |
| Create squashfs | 5-10 min | CPU-intensive (uses all cores) |
| Generate ISO | 2-3 min | Packaging with GRUB |
| **Total** | **30-60 min** | Varies by hardware and internet speed |

**Disk space usage**:
- During build: ~15GB peak
- Final ISO: ~3.5GB
- After cleanup: ~3.5GB (just ISO)

---

## Next Steps

After successful build:

1. **Test in VM** - Verify all features work
2. **Create USB** - Use Rufus (Windows) or dd (Linux)
3. **Share ISO** - Upload to GitHub Releases
4. **Document changes** - Update CHANGELOG.md

---

**Build script**: `scripts/build-ubuntu-v2-FIXED.sh`  
**Expected output**: `~/dingo-ubuntu/ubuntu-build/output/dingo-os-v2.iso`  
**Size**: ~3.5GB  
**Build time**: 30-60 minutes
