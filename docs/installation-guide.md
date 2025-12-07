# 🔧 Dingo OS Installation Guide

This guide will walk you through installing Dingo OS on your computer or virtual machine.

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Downloading Dingo OS](#downloading-dingo-os)
3. [Creating Bootable Media](#creating-bootable-media)
4. [Installation Steps](#installation-steps)
5. [Post-Installation Setup](#post-installation-setup)
6. [Virtual Machine Installation](#virtual-machine-installation)

---

## Prerequisites

### Minimum System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU | 2 cores, 2.0 GHz | 4+ cores, 3.0 GHz |
| RAM | 4 GB | 16 GB |
| Storage | 50 GB | 100 GB SSD |
| GPU | Integrated | Dedicated NVIDIA/AMD |
| Display | 1024x768 | 1920x1080+ |

### Recommended for Specific Use Cases

**Gaming:**
- NVIDIA GTX 1060 / AMD RX 580 or better
- 16 GB RAM minimum
- SSD for game storage

**Blockchain Development:**
- 8 GB RAM minimum (16 GB for running full nodes)
- 500 GB+ SSD for blockchain data

**Development:**
- 16 GB RAM for container workloads
- Fast SSD for project files

---

## Downloading Dingo OS

### Official Download

1. Visit the [GitHub Releases](https://github.com/Baymax005/dingo-os/releases) page
2. Download the latest ISO:
   - **dingo-os-v2.iso** - Full edition with all features (~3.5 GB)
3. Verify the download using SHA256 checksum (provided in release notes)

```bash
# Linux/macOS
sha256sum dingo-os-v2.iso

# Windows PowerShell
Get-FileHash dingo-os-v2.iso -Algorithm SHA256
```

---

## Creating Bootable Media

### Using Balena Etcher (Recommended)

1. Download [Balena Etcher](https://www.balena.io/etcher/)
2. Insert USB drive (4 GB minimum, 8 GB recommended)
3. Select the Dingo OS ISO
4. Select your USB drive
5. Click "Flash!"

### Using dd (Linux)

```bash
sudo dd if=dingo-os-v2.iso of=/dev/sdX bs=4M status=progress
sudo sync
```

> ⚠️ **Warning**: Replace `/dev/sdX` with your actual USB device. Use `lsblk` to identify it.

### Using Rufus (Windows)

1. Download [Rufus](https://rufus.ie/)
2. Select your USB drive
3. Select the Dingo OS ISO
4. Use GPT partition scheme for UEFI
5. Click "Start"

---

## Installation Steps

### Step 1: Boot from USB

1. Insert the bootable USB drive
2. Restart your computer
3. Enter boot menu (usually F12, F2, or ESC)
4. Select USB drive

### Step 2: Choose Installation Mode

- **Try Dingo OS** - Test without installing
- **Install Dingo OS** - Full installation
- **Advanced Options** - Custom installation

### Step 3: Language and Keyboard

1. Select your language
2. Choose keyboard layout
3. Click "Continue"

### Step 4: Installation Type

| Option | Description |
|--------|-------------|
| **Erase disk** | Clean install, removes all data |
| **Dual boot** | Install alongside existing OS |
| **Something else** | Manual partitioning |

#### Recommended Partition Layout

```
/boot/efi   - 512 MB  (EFI System Partition)
/           - 50 GB   (Root filesystem, ext4)
/home       - Rest    (User data, ext4)
swap        - 8-16 GB (Or use swap file)
```

### Step 5: User Configuration

1. Enter your name
2. Choose username
3. Set computer name
4. Create password
5. Enable disk encryption (recommended)

### Step 6: Installation Progress

The installation will:
1. Copy files to disk
2. Install bootloader
3. Configure system
4. Install packages

This takes approximately 15-30 minutes.

### Step 7: Reboot

1. Remove USB drive when prompted
2. Reboot into Dingo OS
3. Complete first-run setup

---

## Post-Installation Setup

### First Login

Dingo OS boots with auto-login enabled:
- **Username**: dingo
- **Password**: dingo (for sudo operations)

KDE Plasma 6 desktop loads automatically.

### Recommended First Steps

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Launch Dingo Control Center (if installed)
python3 /opt/dingo-center/dingo_control_center/main.py

# Install Electrum Bitcoin wallet (requires manual install)
sudo snap install electrum

# Check system info
neofetch
```

---

## Virtual Machine Installation

### VMware Workstation/Player

1. Create new VM with these settings:
   - OS: Ubuntu 64-bit
   - RAM: 8 GB minimum
   - Disk: 80 GB
   - Enable 3D acceleration
   - CPUs: 4 cores

2. Mount Dingo OS ISO
3. Follow normal installation steps
4. Install VMware Tools:

```bash
sudo apt install open-vm-tools open-vm-tools-desktop
```

### VirtualBox

1. Create new VM:
   - Type: Linux
   - Version: Ubuntu (64-bit)
   - RAM: 8192 MB
   - Disk: 80 GB VDI

2. VM Settings:
   - System → Enable EFI
   - Display → 128 MB Video Memory
   - Display → Enable 3D Acceleration

3. Install Guest Additions:

```bash
sudo apt install virtualbox-guest-utils virtualbox-guest-x11
```

### QEMU/KVM

```bash
# Create VM
virt-install \
  --name dingo-os \
  --ram 8192 \
  --vcpus 4 \
  --disk size=80 \
  --cdrom dingo-os-v2.iso \
  --os-variant ubuntu24.04 \
  --graphics spice \
  --video virtio

# Or quick test boot with QEMU
qemu-system-x86_64 -m 4G -enable-kvm \
  -cdrom dingo-os-v2.iso \
  -boot d
```

---

## Troubleshooting

### Boot Issues

**Problem**: Can't boot from USB
- Ensure Secure Boot is disabled (or use signed ISO)
- Try different USB port
- Recreate bootable USB

**Problem**: Black screen after boot
- Add `nomodeset` to kernel parameters
- Check GPU compatibility

### Installation Issues

**Problem**: Installation freezes
- Check ISO integrity
- Try minimal installation
- Disable secure boot

### Post-Installation Issues

**Problem**: No network connection
- Check if drivers are loaded: `lspci -k`
- Install additional drivers: `sudo ubuntu-drivers autoinstall`
- Restart NetworkManager: `sudo systemctl restart NetworkManager`

**Problem**: Dingo Control Center doesn't launch
- Check if installed: `ls /opt/dingo-center/`
- Install dependencies: `sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adw-1 python3-psutil`

---

## Next Steps

- [Quick Start Guide](quick-start.md) - Get productive immediately
- [User Manual](user-manual.md) - Complete user guide
- [Developer Tools](guides/developer-tools.md) - Configure your dev environment

---

*Need help? Check our [FAQ](faq.md) or [Troubleshooting Guide](troubleshooting.md)*
