# 🔧 Troubleshooting Guide

Solutions to common issues in Dingo OS.

---

## Quick Diagnostics

```bash
# Run system diagnostics
dingo doctor

# Check system status
dingo status

# View recent logs
journalctl -xe
```

---

## Boot Issues

### System Won't Boot

**Symptoms:** Black screen, boot loop, GRUB errors

**Solutions:**

1. **Try recovery mode:**
   - Hold Shift during boot
   - Select "Advanced options" → "Recovery mode"

2. **Check filesystem:**
   ```bash
   # From recovery mode
   fsck -y /dev/sda1
   ```

3. **Reinstall GRUB:**
   ```bash
   sudo grub-install /dev/sda
   sudo update-grub
   ```

### Black Screen After Login

**Solutions:**

1. **Switch to TTY:**
   - Press `Ctrl + Alt + F3`
   - Login and run:
   ```bash
   dingo gpu reset
   ```

2. **Disable Wayland:**
   ```bash
   sudo sed -i 's/#WaylandEnable=false/WaylandEnable=false/' /etc/gdm3/custom.conf
   sudo systemctl restart gdm
   ```

---

## Graphics Issues

### NVIDIA Driver Not Working

```bash
# Check driver status
nvidia-smi

# Reinstall driver
dingo gpu nvidia install

# If still not working
sudo apt purge nvidia-*
sudo ubuntu-drivers autoinstall
sudo reboot
```

### AMD Graphics Issues

```bash
# Check AMD GPU
dingo gpu amd info

# Reset configuration
dingo gpu amd reset
```

### Screen Tearing

```bash
# For NVIDIA
sudo nvidia-settings
# Enable "Force Full Composition Pipeline"

# For AMD/Intel
# Edit /etc/X11/xorg.conf.d/20-amd.conf
# Add: Option "TearFree" "true"
```

---

## Audio Issues

### No Sound

```bash
# Check audio devices
pactl list sinks

# Select correct output
pavucontrol

# Restart audio
pulseaudio --kill && pulseaudio --start

# If using PipeWire
systemctl --user restart pipewire
```

### Microphone Not Working

```bash
# Check input devices
pactl list sources

# Unmute microphone
amixer set Capture cap
amixer set Capture 100%
```

---

## Network Issues

### No Internet Connection

```bash
# Check network status
nmcli general status

# List connections
nmcli connection show

# Restart NetworkManager
sudo systemctl restart NetworkManager

# Reset network
sudo nmcli networking off
sudo nmcli networking on
```

### Wi-Fi Not Detected

```bash
# Check if driver is loaded
lspci -k | grep -A3 -i network

# Install Broadcom drivers (if needed)
sudo apt install bcmwl-kernel-source

# Restart
sudo modprobe -r bcmwl
sudo modprobe bcmwl
```

### Slow DNS

```bash
# Use faster DNS
dingo security dns servers 1.1.1.1 8.8.8.8
```

---

## Developer Tools Issues

### Docker Permission Denied

```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Apply changes
newgrp docker

# Or reboot
```

### Node.js Version Wrong

```bash
# Use nvm to switch
nvm list
nvm use 20

# Set default
nvm alias default 20
```

### Python Virtual Environment Issues

```bash
# Create new environment
python3 -m venv .venv

# Activate
source .venv/bin/activate

# If packages missing
pip install -r requirements.txt --force-reinstall
```

### Database Won't Start

```bash
# Check status
dingo db status

# View logs
dingo db logs postgres

# Reset database
dingo db reset postgres
```

---

## Gaming Issues

### Game Won't Launch

```bash
# Verify game files in Steam

# Try different Proton version
# Steam → Game → Properties → Compatibility

# Run with logging
PROTON_LOG=1 %command%

# Check ProtonDB for fixes
```

### Low FPS

```bash
# Enable Game Mode
dingo gaming on

# Check if GPU is being used
nvidia-smi  # NVIDIA
radeontop   # AMD

# Set performance mode
dingo profile gaming
```

### Controller Not Detected

```bash
# Check if detected
lsusb | grep -i controller

# Test controller
jstest /dev/input/js0

# Fix permissions
sudo usermod -aG input $USER
sudo udevadm control --reload-rules
```

### Wine/Proton Crashes

```bash
# Install missing dependencies
winetricks vcrun2019 dxvk d3d11

# Create new Wine prefix
WINEPREFIX=~/.wine-new wineboot

# Reset Proton
rm -rf ~/.steam/steam/steamapps/compatdata/GAMEID
```

---

## Security Issues

### Firewall Blocking Connections

```bash
# Check rules
dingo security firewall status verbose

# Allow port
dingo security firewall allow PORT

# Allow application
dingo security firewall allow "Application Name"
```

### Locked Out of System

```bash
# Boot into recovery mode
# Choose "root" option
# Reset password
passwd username
```

### Can't Install Packages

```bash
# Fix APT
sudo apt --fix-broken install
sudo dpkg --configure -a

# Update package lists
sudo apt update
```

---

## System Issues

### System Running Slow

```bash
# Check resource usage
htop

# Check disk usage
df -h

# Clear package cache
sudo apt clean
sudo apt autoclean

# Clear journal logs
sudo journalctl --vacuum-time=7d
```

### Disk Full

```bash
# Find large files
du -h --max-depth=1 / | sort -hr | head -20

# Clear old kernels
sudo apt autoremove

# Clear snap cache
sudo rm -rf /var/lib/snapd/cache/*

# Clear docker
docker system prune -a
```

### High CPU Usage

```bash
# Identify process
top

# Kill process
kill -9 PID

# Disable startup applications
gnome-session-properties
```

---

## Control Center Issues

### Control Center Won't Open

```bash
# Run from terminal to see errors
dingo-control-center --debug

# Reinstall
dingo repair control-center
```

### Settings Not Saving

```bash
# Reset configuration
rm -rf ~/.config/dingo
dingo-control-center
```

---

## Recovery Commands

### System Repair

```bash
# Run full repair
dingo repair full

# Reset to defaults
dingo reset --preserve-home

# Reinstall packages
dingo repair packages
```

### Backup Before Repair

```bash
# Create backup
dingo backup create

# Restore if needed
dingo backup restore
```

---

## Getting More Help

### Collect System Information

```bash
# Generate report
dingo report > system-report.txt
```

### Log Locations

| Log | Location |
|-----|----------|
| System | `/var/log/syslog` |
| Dingo | `/var/log/dingo/` |
| Xorg | `/var/log/Xorg.0.log` |
| Journal | `journalctl -xe` |

### Contact Support

1. Check [FAQ](faq.md)
2. Search existing issues
3. Open new issue with:
   - System report
   - Steps to reproduce
   - Screenshots if applicable

---

*Still having issues? Run `dingo doctor` and open an issue with the output!*
