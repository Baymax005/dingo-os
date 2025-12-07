# 📝 Changelog

All notable changes to Dingo OS will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0.0] - 2025-12-07

### 🎉 Major Release - Ubuntu 24.04 Base

#### Changed
- **BREAKING**: Migrated from Arch Linux to Ubuntu 24.04 LTS Noble for better stability
- Switched from GNOME to KDE Plasma 6 desktop environment
- Replaced linux-zen with Liquorix high-performance kernel
- Updated branding with modern Breeze Dark theme

#### Added
- ✅ **KDE Plasma 6** desktop with Breeze Dark theme (zero Ubuntu branding)
- ✅ **Liquorix Kernel** for gaming and low-latency performance
- ✅ **Custom Control Center** (GTK4/Libadwaita) with system monitoring
- ✅ **Auto-login** configured for instant desktop (dingo:dingo)
- ✅ **Gaming Suite**: Steam, Lutris, GameMode, MangoHud, Wine 64/32-bit
- ✅ **Development Tools**: VS Code (Microsoft repo), Docker, Docker Compose
- ✅ **Languages**: Python 3.12, Node.js 18, npm, PyQt6
- ✅ **Blockchain Tools**: Truffle, Ganache, Hardhat (npm global packages)
- ✅ **GPU Drivers**: AMD Mesa (Kisak PPA) with i386 support, NVIDIA 550/545 with fallback
- ✅ **Network Tools**: NetworkManager, PulseAudio, pavucontrol
- ✅ **System Utilities**: btop, neofetch, htop, Firefox
- ✅ **Build System**: Single debootstrap script with error handling
- ✅ **Custom Commands**: dingo-game script for performance tuning
- ✅ **Plymouth Theme**: Custom boot splash (Dingo OS branding)
- ✅ **SDDM Theme**: Breeze with auto-login

#### Developer Module
- VS Code from official Microsoft repository
- Docker with user in docker group (no sudo needed)
- Python 3.12 with pip (psutil, distro, dbus-python)
- Node.js 18 LTS with npm
- Git version control
- build-essential (gcc, g++, make)
- PyQt6 for GUI development

#### Gaming Module
- Steam Installer pre-configured
- Lutris game manager
- GameMode daemon with custom dingo-game script
- Wine 64-bit and 32-bit with Winetricks
- AMD Mesa drivers with Vulkan (i386 support)
- NVIDIA drivers 550/545 with 3-tier fallback
- MangoHud for FPS monitoring
- btop for system stats

#### Blockchain Module
- Truffle framework (npm global)
- Ganache local blockchain (npm global)
- Hardhat development environment (npm global)
- Electrum wallet (post-install via snap)
- XMRig support (manual installation)

#### System Features
- Ubuntu 24.04 LTS base (5 years support until 2029)
- KDE Plasma 6 with Breeze Dark theme
- SDDM login manager with auto-login
- NetworkManager for network configuration
- PulseAudio for audio
- Complete de-branding (no Ubuntu/Kubuntu logos)
- Custom os-release file (Dingo OS identification)

#### Build Process
- Reproducible build with debootstrap
- WSL2-compatible build script
- Native Linux filesystem requirement (no NTFS)
- Lazy force umount for WSL compatibility
- /run mount for systemd-resolved DNS
- PPA management with error handling
- Safe package installation with existence checking
- ASCII art banner during build
- Production error handling (set -e, set -u, set -o pipefail)

### Fixed
- DNS resolution in chroot (cp resolv.conf + /run mount)
- PPA installation order (software-properties-common first)
- 32-bit architecture enabled before GPU drivers
- Double kernel conflict (Liquorix-only filter)
- WSL filesystem compatibility (lazy force umount)
- Snap packages removed from chroot (documented as post-install)
- Missing packages removed (lupin-casper, discover-overlay)
- Broken heredocs and syntax errors eliminated

### Removed
- Arch Linux base (switched to Ubuntu 24.04)
- GNOME desktop (switched to KDE Plasma 6)
- linux-zen kernel (switched to Liquorix)
- Snap installation in chroot (moved to post-install notes)
- Ubuntu/Kubuntu branding packages
- Plymouth Ubuntu themes
- All system user conflicts

### Known Issues
- Electrum Bitcoin wallet requires post-install: `sudo snap install electrum`
- XMRig not in Ubuntu repositories (manual install required)
- GameMode status check requires user session (works after login)

### Build Stats
- ISO Size: ~3.5GB
- Build Time: 30-60 minutes (depends on internet speed)
- Chroot Size: ~10GB during build
- Base System: Ubuntu 24.04 Noble (~500MB download)

---

## [1.0.0] - 2024-XX-XX (Deprecated - Arch Build)

### Initial Release
- Arch Linux base with linux-zen kernel
- KDE Plasma 6 desktop
- Multiple boot failures resolved
- Switch Root errors (system user conflicts)
- Deprecated due to persistent boot issues

### Lessons Learned
- Arch Linux packaging too bleeding-edge for stable ISO
- System user management critical for boot
- Switched to Ubuntu for LTS stability

---

*For upgrade instructions, see [Installation Guide](installation-guide.md)*
*For build instructions, see [docs/build-guide.md](build-guide.md)*
