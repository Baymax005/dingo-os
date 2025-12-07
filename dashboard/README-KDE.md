# Dingo Control Center - KDE Plasma Edition

**Made By: Muhammad Ali (Github: Baymax005)**

## Overview

Dingo Control Center is a unified system management dashboard for Dingo OS, designed with KDE Plasma styling using PyQt6.

## Features

### 🏠 Dashboard
- Real-time CPU, Memory, and Disk monitoring
- System information display
- Kernel version and uptime
- Quick actions (Terminal, Settings, Updates)

### 🎮 Gaming Mode
- One-click gaming mode toggle
- GPU detection and driver information
- Game platform launchers (Steam, Lutris)
- Performance optimization

### 🛠️ Developer Tools
- Quick launch for VS Code
- Docker management
- Git GUI access
- Terminal shortcuts

### ⛓️ Blockchain & Mining
- XMRig mining controls
- Electrum wallet integration
- Mining status monitoring

### 🔒 Security
- Firewall management
- Security settings
- System protection

## Installation

### Requirements
```bash
# Install dependencies
sudo apt install python3-pyqt6 python3-pip
pip3 install psutil distro dbus-python
```

### Run
```bash
python3 dingo-control-center-kde.py
```

Or use the desktop launcher:
- Press Super key → Search "Dingo Control Center"

## Integration with Dingo OS Build

The control center is automatically included when building Dingo OS using `build-ubuntu-v2.sh`.

### Manual Integration
```bash
# Copy to system
sudo cp dingo-control-center-kde.py /opt/dingo-control-center/
sudo chmod +x /opt/dingo-control-center/dingo-control-center-kde.py

# Create symlink
sudo ln -s /opt/dingo-control-center/dingo-control-center-kde.py /usr/local/bin/dingo-control-center

# Install desktop entry (already included in build script)
```

## Design

- **Framework:** PyQt6
- **Style:** KDE Plasma Breeze Dark
- **Colors:** 
  - Background: #31363b (Breeze Dark)
  - Accent: #3daee9 (Plasma Blue)
  - Text: #eff0f1 (Breeze Light)
- **Layout:** Sidebar navigation + stacked content area

## Architecture

```
DingoControlCenter (QMainWindow)
├── Sidebar (QFrame)
│   ├── Logo/Branding
│   ├── Navigation List
│   └── Status Display
└── Content Stack (QStackedWidget)
    ├── Dashboard View
    ├── Gaming View
    ├── Developer View
    ├── Blockchain View
    └── Security View
```

## Commands Available

- `dingo-control-center` - Launch control center
- `dingo-game` - Toggle gaming mode (via control center or CLI)

## Shortcuts

- **Gaming Mode:** Click "Enable Gaming Mode" in Gaming tab
- **Terminal:** Dashboard → Open Terminal button
- **Update System:** Dashboard → Update System button
- **Steam:** Gaming → Launch Steam button

## Development

### Adding New Views

1. Create method in `DingoControlCenter` class:
```python
def create_my_view(self):
    widget = QWidget()
    layout = QVBoxLayout()
    widget.setLayout(layout)
    # Add your widgets
    return widget
```

2. Add to content stack in `init_ui()`:
```python
self.content_stack.addWidget(self.create_my_view())
```

3. Add navigation item in `create_sidebar()`:
```python
("🎯  My View", index),
```

### Styling

All styling is done via Qt StyleSheets in `__init__()`. Follow KDE Plasma Breeze color scheme.

## License

GPL-3.0 - Part of Dingo OS Project

## Credits

**Made By:** Muhammad Ali  
**Github:** [Baymax005](https://github.com/Baymax005)  
**Project:** Dingo OS - Gaming & Blockchain Linux Distribution
