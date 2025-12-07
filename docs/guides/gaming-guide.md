# 🎮 Gaming Guide

Complete guide to gaming on Dingo OS.

---

## Overview

Dingo OS comes optimized for gaming with:

| Feature | Description |
|---------|-------------|
| Steam | Pre-installed and configured |
| Lutris | Game library manager |
| GPU Drivers | Auto-detected and installed |
| Game Mode | Performance optimization |
| Proton/Wine | Windows game compatibility |

---

## GPU Setup

### Check Your GPU

```bash
# Dingo GPU info
dingo gpu info

# Detailed information
lspci | grep -i vga
```

### NVIDIA Drivers

```bash
# Auto-install recommended driver
dingo gpu nvidia install

# Install specific version
dingo gpu nvidia install 535

# Check driver status
nvidia-smi
```

### AMD Drivers

```bash
# AMD drivers (AMDGPU) are included in kernel
dingo gpu amd info

# For older cards (AMDGPU-PRO)
dingo gpu amd install-pro
```

### Intel Graphics

```bash
# Intel drivers are included
dingo gpu intel info
```

### Hybrid Graphics (Laptops)

```bash
# Switch to NVIDIA
dingo gpu switch nvidia

# Switch to integrated
dingo gpu switch integrated

# Check current mode
dingo gpu current
```

---

## Steam

### First Launch

```bash
# Launch Steam
steam
```

Steam is pre-configured with:
- Proton enabled by default
- Download optimizations
- Shader cache enabled

### Enable Proton for All Games

1. Open Steam → Settings
2. Steam Play → Enable Steam Play for all titles
3. Select Proton version

### Proton Versions

```bash
# Install additional Proton versions
# In Steam: Steam → Settings → Compatibility

# Proton-GE (community version)
# Download from: https://github.com/GloriousEggroll/proton-ge-custom
```

### Game Compatibility

Check compatibility at [ProtonDB](https://www.protondb.com/)

---

## Lutris

### Overview

Lutris manages games from:
- GOG
- Epic Games Store
- Origin
- Ubisoft Connect
- Wine games

### Launch

```bash
lutris
```

### Install Games

1. Open Lutris
2. Search for game
3. Click Install
4. Follow installation wizard

### Wine Configuration

```bash
# Pre-installed Wine versions
wine --version

# Lutris manages Wine versions automatically
# Or install specific version:
# Lutris → Manage Runners → Wine
```

---

## Game Mode

### What is Game Mode?

Game Mode optimizes system for gaming:
- CPU governor set to performance
- GPU optimization
- Disable compositing
- Priority scheduling

### Enable Game Mode

```bash
# Automatically with Steam
# Games use gamemoderun automatically

# For other games
gamemoderun ./game

# Enable system-wide
dingo gaming on

# Disable
dingo gaming off
```

### Verify Game Mode

```bash
# Check if active
gamemoded -s
```

---

## Performance Monitoring

### MangoHud

On-screen overlay showing:
- FPS
- CPU/GPU usage
- Temperature
- Frame time

```bash
# Enable for any game
mangohud ./game

# Or set environment variable
MANGOHUD=1 ./game

# With Steam
# Add to launch options: mangohud %command%
```

### Configuration

```bash
# Edit MangoHud config
vim ~/.config/MangoHud/MangoHud.conf

# Example configuration
fps
cpu_stats
gpu_stats
frame_timing
```

### Other Monitoring

```bash
# System monitoring
dingo monitor gaming

# GPU temperature
nvidia-smi  # NVIDIA
sensors     # AMD/Intel
```

---

## Performance Optimization

### System Tweaks (Pre-applied)

Dingo OS includes:
- Optimized kernel parameters
- GameMode integration
- Disabled swap for gaming profile
- Reduced input latency

### Additional Tweaks

```bash
# Apply gaming profile
dingo profile gaming

# This sets:
# - CPU governor to performance
# - Disables power saving
# - Optimizes memory
```

### Per-Game Settings

```bash
# Steam launch options examples:

# Force Vulkan
PROTON_USE_VULKAN=1 %command%

# Force DirectX 11
PROTON_USE_DXVK_D3D11=1 %command%

# Disable DXVK (use WineD3D)
PROTON_USE_WINED3D=1 %command%
```

---

## Controller Support

### Supported Controllers

| Controller | Support |
|------------|---------|
| Xbox 360/One/Series | Native |
| PlayStation 4/5 | Native |
| Nintendo Switch Pro | Native |
| Steam Controller | Steam |
| Generic USB | Usually works |

### Controller Setup

```bash
# Check if detected
lsusb | grep -i controller

# Or
dingo gaming controller list
```

### Steam Input

Steam Input provides:
- Custom button mapping
- Gyro support
- Per-game profiles

---

## Wine and Proton

### Wine Prefixes

```bash
# Default Wine prefix
~/.wine

# Create new prefix
WINEPREFIX=~/.wine-game wineboot

# Install game
WINEPREFIX=~/.wine-game wine setup.exe
```

### Winetricks

```bash
# Install dependencies
winetricks vcrun2019 dxvk d3d11

# GUI mode
winetricks --gui
```

### DXVK (DirectX to Vulkan)

Pre-installed and configured:

```bash
# Check DXVK version
cat ~/.local/share/dxvk/dxvk.log

# Update DXVK
dingo gaming dxvk update
```

---

## Streaming

### Game Streaming (Host)

```bash
# Steam Remote Play
# Enabled in Steam settings

# Sunshine (Moonlight host)
dingo gaming streaming start sunshine
```

### Game Streaming (Client)

```bash
# Moonlight client
moonlight
```

---

## Emulation

### RetroArch

```bash
# Launch RetroArch
retroarch

# Download cores
# Settings → Online Updater → Core Downloader
```

### Other Emulators

| System | Emulator |
|--------|----------|
| PlayStation 2 | PCSX2 |
| GameCube/Wii | Dolphin |
| Switch | Yuzu/Ryujinx |
| PlayStation 3 | RPCS3 |

---

## Troubleshooting

### Common Issues

**Game won't launch:**
```bash
# Check Proton compatibility
# Try different Proton version
# Check ProtonDB for fixes
```

**Low FPS:**
```bash
# Enable Game Mode
dingo gaming on

# Check GPU driver
dingo gpu info

# Update drivers
dingo gpu nvidia install
```

**Controller not detected:**
```bash
# Check permissions
sudo usermod -aG input $USER

# Restart udev
sudo udevadm control --reload-rules
```

**Wine game crashes:**
```bash
# Install dependencies
winetricks vcrun2019 dotnet48

# Check Wine prefix
WINEPREFIX=~/.wine-game wine uninstaller
```

### Performance Issues

```bash
# Check if Game Mode is active
gamemoded -s

# Check GPU performance level
cat /sys/class/drm/card*/device/power_dpm_force_performance_level

# Set to high
echo "high" | sudo tee /sys/class/drm/card0/device/power_dpm_force_performance_level
```

---

## Resources

- [ProtonDB](https://www.protondb.com/) - Game compatibility
- [Lutris](https://lutris.net/) - Game installers
- [Wine AppDB](https://appdb.winehq.org/) - Wine compatibility
- [r/linux_gaming](https://reddit.com/r/linux_gaming) - Community

---

*Need help? Run `dingo gaming help` or check our FAQ*
