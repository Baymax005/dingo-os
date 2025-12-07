# 🦘 Dingo OS

**A Developer-Focused, Multi-Purpose Linux Distribution**

![Version](https://img.shields.io/badge/version-2.0-blue)
![Base](https://img.shields.io/badge/base-Ubuntu%2024.04%20Noble-E95420)
![Desktop](https://img.shields.io/badge/desktop-KDE%20Plasma%206-1D99F3)
![Kernel](https://img.shields.io/badge/kernel-Liquorix-00D084)
![License](https://img.shields.io/badge/license-GPL--3.0-green)

---

## 🎯 Overview

Dingo OS is a custom Linux distribution based on Ubuntu 24.04 LTS Noble, designed for developers, gamers, and blockchain enthusiasts. It provides a stable, polished environment with cutting-edge software packages while maintaining Ubuntu's reliability.

### Why Ubuntu 24.04 LTS?
- **LTS Support**: 5 years of security updates until 2029
- **KDE Plasma 6**: Modern, beautiful desktop with Breeze Dark theme
- **Liquorix Kernel**: High-performance, low-latency kernel optimized for gaming
- **Latest GPU Drivers**: AMD Mesa + NVIDIA drivers with 32-bit gaming support
- **Stability + Performance**: Ubuntu's reliability meets gaming-grade performance

## ✨ Key Features

### 🛠️ Developer Tools
- **Languages**: Python 3.12, Node.js 18, npm
- **Containers**: Docker, Docker Compose (user in docker group)
- **Version Control**: Git
- **IDEs**: Visual Studio Code (official Microsoft repo)
- **Build Tools**: build-essential (gcc, make, g++)
- **Python GUI**: PyQt6 for desktop app development

### 🎮 Gaming Suite
- **Platforms**: Steam, Lutris pre-installed
- **Compatibility**: Wine 64/32-bit, Winetricks
- **GPU Drivers**: AMD Mesa (Kisak PPA) + NVIDIA 550/545 with i386 support
- **Performance**: GameMode daemon, custom dingo-game script
- **Monitoring**: MangoHud for FPS/temps, btop for system stats

### ⛓️ Blockchain Tools
- **Development**: Truffle, Ganache, Hardhat (npm global packages)
- **Wallet**: Electrum (install via snap after boot)
- **Mining**: XMRig (manual installation supported)
- **Testing**: Local blockchain networks ready to deploy

### 🔒 Security Hardening
- UFW firewall with secure defaults
- Full disk encryption support
- AppArmor/SELinux profiles
- Automatic security updates
- Secure boot compatibility

### 🎛️ Dingo Control Center
- **GTK4/Libadwaita** modern UI design
- **Dashboard**: Real-time CPU, RAM, Disk monitoring (psutil)
- **Gaming View**: Steam/Lutris launchers, GameMode toggle, GPU info
- **Developer View**: VS Code, Docker, Terminal shortcuts
- **Blockchain View**: XMRig controls, Electrum wallet integration
- **Auto-start**: Launches on login automatically

## 📁 Repository Structure

```
dingo-os/
├── docs/                    # Documentation
├── scripts/                 # Build and automation scripts
├── configs/                 # System configurations
├── packages/                # Package lists and definitions
├── branding/                # Logos, wallpapers, themes
├── dashboard/               # Dingo Control Center source
├── iso-builder/             # ISO generation tools
└── tests/                   # Testing scripts
```

## 🚀 Quick Start

### Prerequisites
- Ubuntu 24.04 host system (or WSL2 with Ubuntu 24.04)
- 20GB free disk space
- Internet connection
- sudo privileges

### Building the ISO
```bash
# Clone repository
git clone https://github.com/Baymax005/dingo-os.git
cd dingo-os

# Copy dashboard to build location (if running from WSL)
mkdir -p ~/dingo-ubuntu
cp -r dashboard ~/dingo-ubuntu/
cp scripts/build-ubuntu-v2-FIXED.sh ~/dingo-ubuntu/

# Run build script (takes 30-60 minutes)
cd ~/dingo-ubuntu
chmod +x build-ubuntu-v2-FIXED.sh
sudo ./build-ubuntu-v2-FIXED.sh
```

### Testing in VM
```bash
# Boot ISO in VMware/VirtualBox:
# - Guest OS: Ubuntu 64-bit
# - Firmware: UEFI or BIOS (both work)
# - RAM: 4GB minimum (8GB recommended)
# - Disk: 20GB+

# Default credentials:
# Username: dingo
# Password: dingo
```

### ISO Location
After building: `~/dingo-ubuntu/ubuntu-build/output/dingo-os-v2.iso` (~3.5 GB)

## 📖 Documentation

- [Installation Guide](docs/installation-guide.md)
- [User Manual](docs/user-manual.md)
- [Developer Guide](docs/developer-guide.md)
- [Architecture Overview](docs/architecture/README.md)

## 🤝 Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

## 📄 License

Dingo OS is released under the GPL-3.0 License. See [LICENSE](LICENSE) for details.

---

**Made with ❤️ by the Dingo OS Team**
