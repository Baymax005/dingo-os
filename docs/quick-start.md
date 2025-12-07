# 🚀 Quick Start Guide

Get up and running with Dingo OS in minutes.

---

## First Boot

After installation, Dingo OS will:

1. ✅ Detect your hardware
2. ✅ Configure GPU drivers
3. ✅ Set up network
4. ✅ Launch Welcome Wizard

---

## Welcome Wizard

### Step 1: Choose Your Profile

Select your primary use case:

```
┌─────────────────────────────────────────┐
│     Welcome to Dingo OS! 🦘             │
│                                         │
│  Choose your primary profile:           │
│                                         │
│  ○ 🛠️  Developer                        │
│  ○ 🎮 Gamer                             │
│  ○ ⛓️  Blockchain                        │
│  ○ 🔒 Security-Focused                  │
│  ○ 🎯 All Features                      │
│                                         │
│              [Continue →]               │
└─────────────────────────────────────────┘
```

### Step 2: Configure Tools

Based on your profile, select additional tools.

### Step 3: Complete Setup

```bash
# Your system is ready!
```

---

## Quick Commands

### Check System Status

```bash
dingo status
```

Output:
```
🦘 Dingo OS v1.0.0
─────────────────────
System: ✓ Healthy
Updates: 5 available
Profile: Developer
GPU: NVIDIA RTX 3080
Security: High
```

### Open Control Center

```bash
dingo-control-center
```

Or press `Super` and search "Dingo Control Center"

### Update Everything

```bash
dingo update
```

---

## For Developers

### Quick Setup

```bash
# Check available tools
dingo dev tools list

# Create a new project
dingo dev new node myproject
cd myproject
npm install
```

### Start Databases

```bash
# Start PostgreSQL
dingo db start postgres

# Check running databases
dingo db status
```

### Docker Ready

```bash
# Docker is pre-configured
docker run hello-world

# Compose example
docker-compose up -d
```

---

## For Gamers

### Quick Setup

```bash
# Check GPU status
dingo gpu info

# Enable gaming mode
dingo gaming on
```

### Launch Games

```bash
# Steam is pre-installed
steam

# Or Lutris for other games
lutris
```

---

## For Blockchain

### Quick Setup

```bash
# Start local testnet
dingo blockchain testnet start

# Check status
dingo blockchain status
```

---

## Essential Shortcuts

| Shortcut | Action |
|----------|--------|
| `Super` | Open Activities |
| `Super + T` | Terminal |
| `Super + E` | File Manager |
| `Ctrl + Alt + T` | New Terminal Window |

---

## Next Steps

- 📖 Read the [User Manual](user-manual.md)
- 🛠️ Explore [Developer Tools](guides/developer-tools.md)
- 🎮 Configure [Gaming](guides/gaming-guide.md)
- 🔒 Review [Security Settings](guides/security-guide.md)

---

*Need help? Run `dingo help` or visit our documentation.*
