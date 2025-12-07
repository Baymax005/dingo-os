# 📖 Dingo OS User Manual

Complete guide to using Dingo OS and all its features.

## 📋 Table of Contents

1. [Introduction](#introduction)
2. [Desktop Environment](#desktop-environment)
3. [Dingo Control Center](#dingo-control-center)
4. [Developer Tools](#developer-tools)
5. [Gaming Features](#gaming-features)
6. [Blockchain Tools](#blockchain-tools)
7. [Security Features](#security-features)
8. [System Management](#system-management)
9. [Customization](#customization)

---

## Introduction

Welcome to Dingo OS! This manual covers everything you need to know to get the most out of your system.

### What is Dingo OS?

Dingo OS is a Ubuntu-based Linux distribution designed for:
- **Developers** - Pre-configured development environment
- **Gamers** - Optimized gaming with Steam, Lutris, and GPU drivers
- **Blockchain Enthusiasts** - Safe blockchain tools and node management
- **Security-Conscious Users** - Hardened security defaults

### Getting Help

- **Control Center**: Access help from `dingo-control-center --help`
- **Terminal**: Use `man` pages or `--help` flags
- **Online**: Visit our documentation site

---

## Desktop Environment

Dingo OS uses a customized GNOME desktop with additional extensions and themes.

### Default Layout

```
┌─────────────────────────────────────────────────────────────┐
│ Activities | Dingo OS     [Date/Time]     [Tray] [Power]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                                                             │
│                       Desktop                               │
│                                                             │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ [Files] [Terminal] [VS Code] [Browser] [Dingo CC] [...]    │
└─────────────────────────────────────────────────────────────┘
```

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Super` | Open Activities |
| `Super + T` | Open Terminal |
| `Super + E` | Open File Manager |
| `Super + D` | Show Desktop |
| `Super + L` | Lock Screen |
| `Ctrl + Alt + T` | New Terminal |
| `Super + Shift + S` | Screenshot |

### Pre-installed Extensions

- **Dash to Dock** - Persistent dock
- **AppIndicator** - System tray support
- **GSConnect** - Phone integration
- **Dingo Quick Settings** - Quick access to Dingo features

---

## Dingo Control Center

The central hub for managing all Dingo OS features.

### Launching

```bash
# From terminal
dingo-control-center

# Or use Super key and search "Dingo"
```

### Main Dashboard

```
┌─────────────────────────────────────────────────────────────┐
│  🦘 Dingo Control Center                           [─][□][×]│
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│  │   System    │ │  Developer  │ │   Gaming    │           │
│  │   Status    │ │    Tools    │ │    Mode     │           │
│  │    ✓ OK     │ │  12 Active  │ │    OFF      │           │
│  └─────────────┘ └─────────────┘ └─────────────┘           │
│                                                             │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│  │ Blockchain  │ │  Security   │ │   Updates   │           │
│  │    Tools    │ │   Level     │ │  Available  │           │
│  │  3 Running  │ │   HIGH      │ │     5       │           │
│  └─────────────┘ └─────────────┘ └─────────────┘           │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  [Developer] [Gaming] [Blockchain] [Security] [Settings]   │
└─────────────────────────────────────────────────────────────┘
```

### Profile Modes

| Mode | Description | Optimizations |
|------|-------------|---------------|
| **Developer** | Focus on dev tools | IDE optimizations, Docker ready |
| **Gaming** | Maximum performance | GPU optimization, Game Mode |
| **Blockchain** | Node-ready | Network optimizations, monitoring |
| **Security** | Maximum security | Strict firewall, encryption |

---

## Developer Tools

### Pre-installed Languages

| Language | Version | Package Manager |
|----------|---------|-----------------|
| Python | 3.12 | pip, pipenv, poetry |
| Node.js | 20 LTS | npm, yarn, pnpm |
| Go | 1.21 | go modules |
| Rust | Latest | cargo |
| Java | 21 LTS | maven, gradle |

### IDEs and Editors

- **Visual Studio Code** - Full-featured IDE
- **Neovim** - Terminal editor with custom config
- **JetBrains Toolbox** - Install JetBrains IDEs

### Container Tools

```bash
# Docker (pre-installed)
docker --version
docker-compose --version

# Podman alternative
podman --version

# Kubernetes tools
kubectl version
minikube version
k9s
```

### Database Tools

```bash
# Start databases
dingo db start postgres
dingo db start mysql
dingo db start redis
dingo db start mongodb

# Database GUIs included
dbeaver        # Universal DB client
pgadmin4       # PostgreSQL admin
mongosh        # MongoDB shell
```

### Development Workflow

```bash
# Create new project
dingo new python-project myproject
dingo new node-project myapp
dingo new go-project myservice

# Development environment
dingo env setup  # Setup virtual environment
dingo env shell  # Enter development shell
```

---

## Gaming Features

### Steam and Lutris

Steam and Lutris come pre-installed and configured:

```bash
# Launch Steam
steam

# Launch Lutris
lutris
```

### GPU Drivers

GPU drivers are auto-detected during installation. To manually manage:

```bash
# Check current GPU
dingo gpu info

# Install/Update NVIDIA drivers
dingo gpu nvidia install

# Install/Update AMD drivers
dingo gpu amd install

# Switch between GPUs (laptops)
dingo gpu switch nvidia
dingo gpu switch integrated
```

### Game Mode

Game Mode optimizes system performance for gaming:

```bash
# Enable Game Mode
gamemoderun ./game

# Or enable globally
dingo gaming on

# Disable
dingo gaming off
```

### Performance Monitoring

```bash
# Launch MangoHud overlay
mangohud ./game

# System monitoring
dingo monitor gaming
```

---

## Blockchain Tools

### Wallet Management

```bash
# List available wallets
dingo blockchain wallets list

# Setup wallet
dingo blockchain wallets setup metamask
dingo blockchain wallets setup ledger
```

### Node Management

```bash
# Install blockchain node
dingo blockchain node install ethereum
dingo blockchain node install bitcoin

# Start/Stop nodes
dingo blockchain node start ethereum
dingo blockchain node stop ethereum

# Check sync status
dingo blockchain node status
```

### Development Networks

```bash
# Start local testnet
dingo blockchain testnet start hardhat
dingo blockchain testnet start ganache

# Deploy contracts
dingo blockchain deploy ./contracts --network testnet
```

### Monitoring

```bash
# Launch blockchain monitor
dingo blockchain monitor

# View transaction history
dingo blockchain transactions
```

---

## Security Features

### Firewall Management

```bash
# Check firewall status
dingo security firewall status

# Enable/Disable
dingo security firewall enable
dingo security firewall disable

# Allow/Block ports
dingo security firewall allow 8080
dingo security firewall block 23
```

### Encryption

```bash
# Check disk encryption status
dingo security encryption status

# Encrypt home directory (if not done during install)
dingo security encryption home

# Create encrypted container
dingo security encryption create vault 1G
```

### Security Scanning

```bash
# Full system scan
dingo security scan full

# Quick scan
dingo security scan quick

# Check for vulnerabilities
dingo security audit
```

### Secure Updates

```bash
# Check for security updates
dingo security updates check

# Install security updates only
dingo security updates install

# Enable automatic security updates
dingo security updates auto enable
```

---

## System Management

### Updates

```bash
# Full system update
dingo update

# Update specific components
dingo update system
dingo update apps
dingo update security
```

### Backup

```bash
# Create system backup
dingo backup create

# Restore from backup
dingo backup restore

# List backups
dingo backup list
```

### Performance

```bash
# System overview
dingo status

# Detailed performance
dingo performance

# Optimize system
dingo optimize
```

### Logs

```bash
# View system logs
dingo logs system

# View application logs
dingo logs apps

# View security logs
dingo logs security
```

---

## Customization

### Themes

```bash
# List available themes
dingo theme list

# Apply theme
dingo theme apply nordic
dingo theme apply dracula
dingo theme apply dingo-dark
dingo theme apply dingo-light
```

### Wallpapers

Pre-installed Dingo OS wallpapers are in `/usr/share/backgrounds/dingo/`

### Terminal

The default terminal uses a custom configuration:

```bash
# Change terminal theme
dingo terminal theme list
dingo terminal theme apply gruvbox

# Change shell
dingo shell zsh    # Switch to Zsh
dingo shell fish   # Switch to Fish
dingo shell bash   # Switch to Bash
```

### Fonts

Developer-friendly fonts pre-installed:
- **Fira Code** - With ligatures
- **JetBrains Mono** - IDE font
- **Cascadia Code** - Microsoft font
- **Hack** - Terminal font

---

## Command Reference

### Quick Command Reference

```bash
dingo status              # System status
dingo update              # Update system
dingo help                # Show help
dingo doctor              # Diagnose issues
dingo control-center      # Open GUI dashboard

# Developer commands
dingo dev new <type> <name>
dingo dev env
dingo db <command>

# Gaming commands
dingo gaming on/off
dingo gpu <command>

# Blockchain commands
dingo blockchain <command>

# Security commands
dingo security <command>
```

---

*For more detailed information, see specific guides in the [docs](README.md) directory.*
