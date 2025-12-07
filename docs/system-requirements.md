# 💻 System Requirements

Complete hardware and software requirements for Dingo OS.

---

## Hardware Requirements

### Minimum Requirements

| Component | Specification |
|-----------|---------------|
| **Processor** | 64-bit dual-core CPU @ 2.0 GHz |
| **Memory** | 4 GB RAM |
| **Storage** | 50 GB available disk space |
| **Graphics** | Integrated GPU with OpenGL 3.3 support |
| **Display** | 1024 × 768 resolution |
| **Network** | Ethernet or Wi-Fi adapter |

### Recommended Requirements

| Component | Specification |
|-----------|---------------|
| **Processor** | 64-bit quad-core CPU @ 3.0 GHz |
| **Memory** | 16 GB RAM |
| **Storage** | 100 GB SSD |
| **Graphics** | NVIDIA GTX 1060 / AMD RX 580 or better |
| **Display** | 1920 × 1080 resolution |
| **Network** | Gigabit Ethernet |

---

## Use-Case Specific Requirements

### Developer Workstation

| Component | Recommended |
|-----------|-------------|
| **Processor** | 6+ cores for compilation and containers |
| **Memory** | 16-32 GB RAM |
| **Storage** | 256 GB NVMe SSD |
| **Graphics** | Any (integrated sufficient) |

**Why these specs?**
- Multiple Docker containers
- Running databases and services
- Compiling large projects
- Multiple IDE instances

### Gaming Setup

| Component | Recommended |
|-----------|-------------|
| **Processor** | 6+ cores @ 3.5 GHz |
| **Memory** | 16-32 GB RAM |
| **Storage** | 500 GB+ SSD |
| **Graphics** | NVIDIA RTX 3060 / AMD RX 6600 or better |

**Supported GPUs:**
- NVIDIA: GeForce 700 series and newer
- AMD: Radeon HD 7000 series and newer
- Intel: HD 4000 and newer (limited)

### Blockchain Node

| Component | Recommended |
|-----------|-------------|
| **Processor** | 4+ cores |
| **Memory** | 16 GB RAM minimum |
| **Storage** | 1 TB+ SSD (for full nodes) |
| **Network** | Stable broadband, preferably unmetered |

**Storage by Chain:**
| Blockchain | Approximate Storage |
|------------|---------------------|
| Bitcoin | ~500 GB (full node) |
| Ethereum | ~800 GB (full node) |
| Polygon | ~2 TB (archive node) |
| Testnet | ~50 GB |

---

## Virtual Machine Requirements

### VMware Workstation / Player

| Setting | Minimum | Recommended |
|---------|---------|-------------|
| RAM | 4 GB | 8 GB |
| CPUs | 2 cores | 4 cores |
| Disk | 60 GB | 100 GB |
| Video RAM | 128 MB | 256 MB |
| 3D Acceleration | Required | Required |

### VirtualBox

| Setting | Minimum | Recommended |
|---------|---------|-------------|
| RAM | 4096 MB | 8192 MB |
| CPUs | 2 | 4 |
| Disk | 60 GB VDI | 100 GB VDI |
| Video RAM | 128 MB | 256 MB |
| Graphics Controller | VMSVGA | VMSVGA |

### QEMU/KVM

```bash
virt-install \
  --ram 8192 \
  --vcpus 4 \
  --disk size=100 \
  --os-variant ubuntu24.04
```

---

## Software Requirements

### For Building ISO

| Software | Version |
|----------|---------|
| Ubuntu | 22.04 or 24.04 |
| debootstrap | Latest |
| squashfs-tools | 4.4+ |
| xorriso | 1.5+ |
| grub-pc-bin | Latest |
| mtools | Latest |

### For Development

| Software | Included |
|----------|----------|
| Git | Latest |
| Docker | 24.x |
| Python | 3.12 |
| Node.js | 20 LTS |

---

## BIOS/UEFI Settings

### Required Settings

- **Virtualization**: Enable VT-x (Intel) or AMD-V
- **Boot Mode**: UEFI recommended (Legacy BIOS supported)
- **Secure Boot**: Supported (signed kernel)

### Recommended Settings

- **Fast Boot**: Disable for installation
- **CSM**: Disable for UEFI-only boot

---

## Network Requirements

### Minimum Bandwidth

| Activity | Bandwidth |
|----------|-----------|
| Basic updates | 1 Mbps |
| Development | 10 Mbps |
| Gaming | 25 Mbps |
| Blockchain sync | 50+ Mbps |

### Firewall Ports

| Service | Port | Protocol |
|---------|------|----------|
| SSH | 22 | TCP |
| HTTP | 80 | TCP |
| HTTPS | 443 | TCP |
| Bitcoin | 8333 | TCP |
| Ethereum | 30303 | TCP/UDP |

---

## Compatibility

### Tested Hardware

**Laptops:**
- Dell XPS 13/15
- Lenovo ThinkPad X1 Carbon
- HP Spectre x360
- System76 laptops
- Framework Laptop

**Desktops:**
- Custom builds with AMD/Intel CPUs
- System76 desktops
- HP/Dell workstations

### Known Issues

| Hardware | Issue | Workaround |
|----------|-------|------------|
| Some Broadcom Wi-Fi | Driver not included | Install `bcmwl-kernel-source` |
| NVIDIA Optimus | Hybrid graphics | Use `dingo gpu switch` |
| Fingerprint readers | Limited support | Some work with `fprintd` |

---

*For specific hardware compatibility, check our [Hardware Compatibility List](hcl.md)*
