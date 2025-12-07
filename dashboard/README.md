# Dingo Control Center

The graphical dashboard for managing Dingo OS.

## Overview

Dingo Control Center is a GTK4 application that provides a unified interface for:
- System monitoring
- Profile switching
- Tool management
- Updates and maintenance

## Development

### Requirements
- Python 3.11+
- GTK4
- libadwaita

### Setup

```bash
cd dashboard
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run

```bash
python -m dingo_control_center
```

### Build

```bash
python setup.py build
```

## Structure

```
dashboard/
├── src/
│   └── dingo_control_center/
│       ├── __init__.py
│       ├── __main__.py
│       ├── app.py
│       ├── window.py
│       └── views/
├── ui/
│   └── *.ui
├── tests/
├── requirements.txt
└── setup.py
```
