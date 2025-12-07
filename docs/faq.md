# ❓ Frequently Asked Questions

Common questions about Dingo OS.

---

## General

### What is Dingo OS?

Dingo OS is a custom Linux distribution based on Ubuntu LTS, designed for developers with optional features for gamers, blockchain enthusiasts, and security-conscious users.

### Is Dingo OS free?

Yes! Dingo OS is completely free and open source under the GPL-3.0 license.

### What is it based on?

Dingo OS is based on Ubuntu 24.04 LTS, providing a stable foundation with 5 years of support.

### Can I use it as my daily driver?

Absolutely! Dingo OS is designed to be a complete, polished desktop experience suitable for everyday use.

---

## Installation

### What are the minimum requirements?

- 64-bit CPU (2 cores, 2.0 GHz)
- 4 GB RAM (16 GB recommended)
- 50 GB storage (100 GB SSD recommended)
- Internet connection for updates

### Can I dual-boot with Windows?

Yes, Dingo OS supports dual-boot installations. Choose "Install alongside Windows" during installation.

### Does it work in virtual machines?

Yes! Dingo OS works well in VMware, VirtualBox, and QEMU/KVM.

---

## Software

### How do I install additional software?

```bash
# Using apt
sudo apt install package-name

# Using Dingo Control Center
dingo-control-center
```

### Are Flatpak and Snap supported?

Yes, both are supported:
```bash
flatpak install app-name
snap install app-name
```

### How do I update the system?

```bash
dingo update
# Or use the graphical update manager
```

---

## Developer Tools

### What languages are pre-installed?

Python 3.12, Node.js 20 LTS, Go 1.21, Rust, and Java 21.

### How do I install additional Node.js versions?

```bash
nvm install 18
nvm use 18
```

### How do I start a database?

```bash
dingo db start postgres
dingo db start mysql
dingo db start redis
```

---

## Gaming

### How do I install GPU drivers?

GPU drivers are auto-detected during installation. To manually install:
```bash
dingo gpu nvidia install  # For NVIDIA
dingo gpu amd install     # For AMD
```

### Why won't my game run?

1. Check [ProtonDB](https://protondb.com) for compatibility
2. Try a different Proton version
3. Check launch options
4. Run `dingo gaming doctor`

### How do I enable Game Mode?

```bash
dingo gaming on
# Or launch games with
gamemoderun ./game
```

---

## Blockchain

### How do I start a local testnet?

```bash
dingo blockchain testnet start
```

### How do I install a blockchain node?

```bash
dingo blockchain node install ethereum
dingo blockchain node start ethereum
```

---

## Security

### How secure is Dingo OS?

Dingo OS includes:
- UFW firewall (enabled by default)
- AppArmor enforcement
- Automatic security updates
- Fail2ban protection
- Full disk encryption option

### How do I check for vulnerabilities?

```bash
dingo security audit
dingo security scan
```

---

## Troubleshooting

### System won't boot

1. Try "Advanced Options" from GRUB menu
2. Boot in recovery mode
3. Check for disk errors

### No sound

```bash
# Check audio settings
pavucontrol

# Restart audio
pulseaudio --kill && pulseaudio --start
```

### Network not working

```bash
# Check network status
nmcli general status

# Restart NetworkManager
sudo systemctl restart NetworkManager
```

### Screen resolution issues

```bash
# List displays
xrandr

# Set resolution
xrandr --output HDMI-1 --mode 1920x1080
```

---

## Support

### Where can I get help?

- Check this FAQ
- Read the [Troubleshooting Guide](troubleshooting.md)
- Open an issue on GitHub
- Join our community chat

### How do I report a bug?

Open an issue on GitHub with:
- Clear description
- Steps to reproduce
- System information (`dingo status`)
- Relevant logs

---

*Didn't find your answer? Run `dingo help` or open an issue!*
