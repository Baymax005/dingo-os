# 🔒 Security Guide

Complete guide to security features in Dingo OS.

---

## Overview

Dingo OS implements security at multiple layers:

| Layer | Features |
|-------|----------|
| **Network** | UFW firewall, fail2ban |
| **System** | AppArmor, secure defaults |
| **Storage** | Full disk encryption, secure delete |
| **Application** | Sandboxing, automatic updates |
| **User** | Strong password policies, 2FA |

---

## Security Profiles

### Choose Security Level

```bash
# Standard (balanced)
dingo security profile standard

# High (stricter)
dingo security profile high

# Paranoid (maximum)
dingo security profile paranoid
```

### Profile Comparison

| Feature | Standard | High | Paranoid |
|---------|----------|------|----------|
| Firewall | ✓ | ✓ (strict) | ✓ (lockdown) |
| Auto-updates | Security only | All | All + kernel |
| AppArmor | Enforce | Enforce | Enforce |
| USB | Enabled | Authorized | Disabled |
| Webcam/Mic | Enabled | Ask | Disabled |

---

## Firewall (UFW)

### Basic Usage

```bash
# Check status
dingo security firewall status

# Enable/Disable
dingo security firewall enable
dingo security firewall disable

# Default: deny incoming, allow outgoing
```

### Managing Rules

```bash
# Allow port
dingo security firewall allow 22
dingo security firewall allow 80/tcp

# Deny port
dingo security firewall deny 23

# Allow from specific IP
dingo security firewall allow from 192.168.1.100

# Delete rule
dingo security firewall delete allow 80
```

### Application Profiles

```bash
# List available apps
dingo security firewall app list

# Allow application
dingo security firewall allow OpenSSH
dingo security firewall allow "Nginx Full"
```

### View Rules

```bash
# Numbered list
dingo security firewall status numbered

# Verbose
dingo security firewall status verbose
```

---

## Disk Encryption

### Full Disk Encryption (LUKS)

Set up during installation or:

```bash
# Check encryption status
dingo security encryption status

# Encrypt home directory (post-install)
dingo security encryption home
```

### Encrypted Containers

```bash
# Create encrypted container
dingo security encryption create vault 1G

# Mount container
dingo security encryption mount vault

# Unmount
dingo security encryption unmount vault
```

### Secure Key Management

```bash
# Add recovery key
dingo security encryption add-key

# Change encryption password
dingo security encryption change-password

# Backup LUKS header
dingo security encryption backup-header
```

---

## AppArmor

### Overview

AppArmor confines applications to limited resources.

```bash
# Check status
aa-status

# Dingo command
dingo security apparmor status
```

### Managing Profiles

```bash
# List profiles
dingo security apparmor list

# Set profile to enforce mode
dingo security apparmor enforce firefox

# Set profile to complain mode (logging only)
dingo security apparmor complain firefox

# Disable profile
dingo security apparmor disable firefox
```

### Pre-configured Profiles

Dingo OS includes AppArmor profiles for:
- Firefox
- Chrome/Chromium
- Docker
- System services

---

## Fail2ban

### Overview

Fail2ban protects against brute-force attacks.

```bash
# Check status
dingo security fail2ban status

# Check specific jail
dingo security fail2ban status sshd
```

### Configuration

```bash
# View banned IPs
dingo security fail2ban banned

# Unban IP
dingo security fail2ban unban 192.168.1.100

# Ban IP manually
dingo security fail2ban ban 192.168.1.100
```

### Default Jails

| Jail | Protects |
|------|----------|
| sshd | SSH brute-force |
| nginx-http-auth | Nginx auth |
| postfix | Mail server |

---

## Automatic Updates

### Configuration

```bash
# Check auto-update status
dingo security updates status

# Enable automatic security updates
dingo security updates auto enable

# Disable automatic updates
dingo security updates auto disable
```

### Manual Updates

```bash
# Check for security updates
dingo security updates check

# Install security updates only
dingo security updates install

# Full system update
dingo update
```

### Unattended Upgrades

```bash
# Configure
sudo dpkg-reconfigure unattended-upgrades

# Logs
cat /var/log/unattended-upgrades/unattended-upgrades.log
```

---

## Security Scanning

### System Audit

```bash
# Full security audit
dingo security audit

# Quick check
dingo security audit quick
```

### Vulnerability Scanning

```bash
# Scan for vulnerabilities
dingo security scan

# Scan specific package
dingo security scan --package openssl

# Check CVEs
dingo security cve check
```

### Rootkit Detection

```bash
# Run rkhunter
dingo security scan rootkit

# Run chkrootkit
dingo security scan chkrootkit
```

### File Integrity

```bash
# Initialize integrity database
dingo security integrity init

# Check file integrity
dingo security integrity check

# Update database
dingo security integrity update
```

---

## Network Security

### DNS Security

```bash
# Use encrypted DNS (DoH)
dingo security dns doh enable

# Use DNS over TLS
dingo security dns dot enable

# Configure DNS servers
dingo security dns servers 1.1.1.1 8.8.8.8
```

### VPN Support

```bash
# WireGuard (pre-installed)
dingo vpn wireguard setup

# OpenVPN
dingo vpn openvpn connect config.ovpn
```

### Network Monitoring

```bash
# Monitor network connections
dingo security network monitor

# Check for suspicious connections
dingo security network suspicious
```

---

## SSH Security

### Secure Configuration

Pre-configured secure defaults:

```
# /etc/ssh/sshd_config
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
X11Forwarding no
MaxAuthTries 3
```

### SSH Key Management

```bash
# Generate secure key
dingo security ssh keygen

# Copy key to server
dingo security ssh copy-id user@server

# Manage authorized keys
dingo security ssh authorized
```

---

## Browser Security

### Firefox Hardening

Pre-configured with:
- HTTPS-Only Mode
- Enhanced Tracking Protection
- uBlock Origin
- Privacy extensions

### Additional Hardening

```bash
# Apply privacy profile
dingo security browser harden firefox

# Reset to defaults
dingo security browser reset firefox
```

---

## Password Management

### Password Policies

```bash
# Check password strength
dingo security password check

# Generate secure password
dingo security password generate
```

### Password Managers

Pre-installed:
- **KeePassXC** - Local password database
- **Bitwarden** - Cloud sync (optional)

```bash
# Launch KeePassXC
keepassxc
```

---

## Privacy Features

### Data Cleaning

```bash
# Clear temp files
dingo security clean temp

# Clear browser data
dingo security clean browser

# Secure delete file
dingo security shred /path/to/file

# Wipe free space
dingo security wipe-free /home
```

### Metadata Removal

```bash
# Remove metadata from file
dingo security metadata remove photo.jpg

# Check metadata
dingo security metadata check document.pdf
```

---

## Secure Defaults

### Applied by Default

| Setting | Value |
|---------|-------|
| Firewall | Enabled (deny incoming) |
| Auto-updates | Security updates enabled |
| SSH root | Disabled |
| Password complexity | Required |
| Screen lock | 5 minutes |
| Secure boot | Supported |

---

## Security Checklist

### Initial Setup

- [ ] Enable full disk encryption
- [ ] Set strong password
- [ ] Configure firewall
- [ ] Enable automatic security updates
- [ ] Set up backup encryption keys

### Regular Maintenance

- [ ] Check for updates weekly
- [ ] Review firewall rules monthly
- [ ] Run security audit monthly
- [ ] Check for CVEs on critical software
- [ ] Review failed login attempts

---

## Emergency Response

### If Compromised

```bash
# 1. Disconnect network
dingo security emergency disconnect

# 2. Capture system state
dingo security emergency capture

# 3. Run forensic analysis
dingo security emergency analyze

# 4. Reset compromised credentials
dingo security emergency reset-creds
```

### Recovery

```bash
# Restore from clean backup
dingo backup restore --verify

# Reset security settings
dingo security reset-defaults
```

---

## Resources

- [Ubuntu Security Guide](https://ubuntu.com/security)
- [CIS Benchmarks](https://www.cisecurity.org/benchmark/ubuntu_linux)
- [NIST Guidelines](https://csrc.nist.gov/)
- [CVE Database](https://cve.mitre.org/)

---

*Need help? Run `dingo security help` or check our FAQ*
