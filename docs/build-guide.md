# 🔨 Build Guide

Instructions for building Dingo OS ISO from source.

---

## Prerequisites

### Build System Requirements

- Linux system with Docker installed (or WSL2 with Docker)
- 8 GB RAM minimum
- 20 GB free disk space
- Internet connection

### Install Docker

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER

# Arch Linux
sudo pacman -S docker
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

---

## Getting the Source

```bash
# Clone the repository
git clone https://github.com/dingo-os/dingo-os.git
cd dingo-os
```

---

## Build Process

### Quick Build (Docker Method - Recommended)

```bash
# Make script executable
chmod +x scripts/build-arch-docker.sh

# Build the ISO
./scripts/build-arch-docker.sh
```

This will:
1. Pull the latest Arch Linux Docker image
2. Install archiso inside the container
3. Create a custom profile with KDE Plasma 6
4. Build the ISO with all packages
5. Output to `arch-build/out/DingoOS-1.0.0-x86_64.iso`

### What's Included

| Category | Packages |
|----------|----------|
| **Base** | linux-zen, linux-zen-headers, linux-firmware |
| **Desktop** | plasma-desktop, sddm, konsole, dolphin, kate |
| **NVIDIA** | nvidia-dkms, nvidia-utils, nvidia-settings |
| **Gaming** | steam, lutris, gamemode, wine, mangohud |
| **Dev** | git, docker, python, nodejs, npm, base-devel |
| **Apps** | firefox, fastfetch, htop, ark, spectacle |

---

## Build Stages

### Stage 1: Create Profile

Creates the archiso profile with:
- `packages.x86_64` - list of packages to install
- `profiledef.sh` - ISO metadata and boot modes
- `airootfs/` - custom files for the live system

### Stage 2: Install Packages

Using pacstrap, installs:
- KDE Plasma 6 desktop environment
- linux-zen kernel with headers
- NVIDIA drivers (nvidia-dkms)
- Gaming stack (Steam, Lutris, Wine)
- Developer tools (Git, Docker, Python, Node.js)

### Stage 3: Configure System

Applies Dingo OS customizations:
- `/etc/os-release` - Dingo OS branding
- SDDM auto-login for live session
- NetworkManager enabled
- Dingo CLI tool installed
- Custom wallpapers from branding/

### Stage 4: Create SquashFS

Compresses the root filesystem:

```bash
mksquashfs airootfs/ airootfs.sfs -comp xz -b 1M
```

### Stage 5: Build ISO

Creates UEFI-bootable ISO with GRUB:

```bash
mkarchiso -v -w work/ -o out/ profile/
```

---

## Build Output

After successful build:

```
arch-build/
├── out/
│   └── DingoOS-1.0.0-x86_64.iso    # Bootable ISO (~3 GB)
├── work/                            # Build working directory
└── profile/                         # archiso profile
```

### Verify Build

```bash
# Check ISO exists and size
ls -lh arch-build/out/DingoOS-1.0.0-x86_64.iso

# Verify it's a valid ISO
file arch-build/out/DingoOS-1.0.0-x86_64.iso
# Should show: ISO 9660 CD-ROM filesystem data ... 'DINGO_OS' (bootable)
```

---

## Testing the Build

### Test in QEMU

```bash
qemu-system-x86_64 \
    -boot d \
    -cdrom arch-build/out/DingoOS-1.0.0-x86_64.iso \
    -m 4096 \
    -enable-kvm \
    -cpu host \
    -smp 4
```

### Test in VirtualBox

1. Create new VM (Linux, Arch Linux 64-bit)
2. Enable EFI: Settings → System → Enable EFI
3. RAM: 4096 MB minimum
4. Video Memory: 128 MB, enable 3D acceleration
5. Attach ISO as optical drive
6. Boot and enjoy!

### Test in VMware

1. Create new VM (Linux, Other Linux 5.x kernel 64-bit)
2. Firmware: UEFI
3. RAM: 4096 MB minimum
4. Attach ISO and boot

---

## Customizing the Build

### Add Custom Packages

Edit `scripts/build-arch-docker.sh` and add packages to the `packages.x86_64` section:

```bash
# Add your packages here
your-package
another-package
```

### Modify Configurations

Edit files in the airootfs section of the build script:

- `/etc/os-release` - OS branding
- `/etc/hostname` - System hostname
- `/etc/sddm.conf.d/` - Login manager settings
- `/usr/local/bin/` - Custom scripts

### Add Branding

Place files in `branding/imgs/`:

```
branding/
├── imgs/            # Logo images and wallpapers
├── grub/            # GRUB theme
├── plymouth/        # Boot splash
└── sddm/            # Login screen theme
```

---

## Technical Details

### ISO Specifications

| Property | Value |
|----------|-------|
| Base | Arch Linux (rolling) |
| Desktop | KDE Plasma 6 |
| Kernel | linux-zen 6.x |
| Init | systemd |
| Boot | UEFI (GRUB) |
| Filesystem | SquashFS (xz) |
| Size | ~3 GB |

---

## Troubleshooting

### Common Issues

**Issue**: Docker permission denied
```bash
# Add user to docker group
sudo usermod -aG docker $USER
# Log out and back in
```

**Issue**: Build fails with package not found
```bash
# Some packages may be renamed or removed in Arch
# Check https://archlinux.org/packages/ for correct names
```

**Issue**: ISO won't boot (drops to GRUB shell)
```bash
# Ensure UEFI boot mode is enabled in VM settings
# Verify grub.cfg has correct paths
```

### Clean Build

```bash
# Remove build artifacts
rm -rf arch-build/

# Rebuild from scratch
./scripts/build-arch-docker.sh
```

---

## Live Session Details

- **Username**: dingo
- **Password**: dingo
- **Root access**: `sudo` (no password required)
- **Auto-login**: Enabled for live session

---

## Included Software

### Desktop Environment
- KDE Plasma 6 with Wayland
- SDDM login manager
- Konsole, Dolphin, Kate, Ark

### System
- NetworkManager for networking
- PipeWire for audio
- BlueZ for Bluetooth

### Gaming
- Steam (native)
- Lutris
- Wine + Winetricks
- GameMode + MangoHud

### Development
- Git, Docker, Docker Compose
- Python 3, pip
- Node.js, npm
- base-devel (gcc, make, etc.)

---

*For more details, see the [Developer Guide](developer-guide.md)*
