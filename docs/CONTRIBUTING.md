# 🤝 Contributing to Dingo OS

Thank you for your interest in contributing to Dingo OS! This guide will help you get started with contributing code, documentation, bug reports, and feature requests.

---

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing Requirements](#testing-requirements)
- [Pull Request Process](#pull-request-process)
- [Community Guidelines](#community-guidelines)

---

## 🚀 Getting Started

### Prerequisites

- Ubuntu 24.04 host system (or WSL2)
- Git installed and configured
- Basic knowledge of Bash scripting
- Familiarity with debootstrap/chroot (for ISO contributions)
- Python 3.12+ (for Control Center contributions)

### Fork and Clone

```bash
# Fork the repository on GitHub first, then:
git clone https://github.com/YOUR_USERNAME/dingo-os.git
cd dingo-os

# Add upstream remote
git remote add upstream https://github.com/Baymax005/dingo-os.git

# Create development branch
git checkout -b feature/my-contribution
```

---

## 🔄 Development Workflow

### 1. Issue Creation

Before starting work:

1. **Search existing issues** to avoid duplicates
2. **Create new issue** with:
   - Clear, descriptive title
   - Detailed description of the problem/feature
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior (for bugs)
   - System information (Ubuntu version, kernel, hardware)
   - Screenshots/logs if applicable

### 2. Branch Naming

Use descriptive branch names following this convention:

```
feature/add-flatpak-support
fix/boot-splash-screen-error
docs/improve-build-guide
refactor/simplify-chroot-process
test/add-vm-boot-tests
```

### 3. Making Changes

**For Build Script Changes:**
```bash
# Edit scripts/build-ubuntu-v2-FIXED.sh
vim scripts/build-ubuntu-v2-FIXED.sh

# Test build in clean environment
sudo ./scripts/build-ubuntu-v2-FIXED.sh

# Verify ISO boots in VM
qemu-system-x86_64 -m 4G -cdrom ~/dingo-ubuntu/ubuntu-build/output/dingo-os-v2.iso
```

**For Control Center Changes:**
```bash
# Install development dependencies
pip install -r dashboard/requirements.txt

# Run linting
black dashboard/src/
pylint dashboard/src/

# Test application
python3 dashboard/dingo-control-center-kde.py
```

**For Documentation Changes:**
```bash
# Edit markdown files
vim docs/build-guide.md

# Check for broken links
markdown-link-check docs/**/*.md
```

### 4. Commit Guidelines

Follow **Conventional Commits** specification:

```
feat(build): add support for custom kernel parameters
fix(dashboard): resolve CPU usage calculation error
docs(README): update installation instructions for WSL2
style(configs): format KDE Plasma config files
refactor(services): simplify dingod daemon startup logic
test(iso): add VMware boot verification test
chore(deps): update Python dependencies to latest versions
```

**Commit Message Structure:**
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Example:**
```
feat(gaming): add MangoHud configuration profiles

Implements three MangoHud preset configurations:
- Minimal: FPS counter only
- Standard: FPS + GPU/CPU temps
- Full: All metrics including frame times

Configs placed in /etc/mangohud/ for system-wide access.

Closes #42
```

### 5. Testing Requirements

**Before submitting PR:**

- [ ] Code follows project style guidelines
- [ ] All existing tests pass
- [ ] New tests added for new features
- [ ] Documentation updated (if applicable)
- [ ] CHANGELOG.md updated with changes
- [ ] ISO builds successfully (for build script changes)
- [ ] ISO boots in QEMU/VMware/VirtualBox (for system changes)
- [ ] No regression bugs introduced

---

## 📝 Coding Standards

### Shell Scripts (Bash)

**Style Guidelines:**

- Follow [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html)
- Use `shellcheck` for linting: `shellcheck script.sh`
- Always quote variables: `"${variable}"` not `$variable`
- Use `set -euo pipefail` at script start
- Add error handling for critical operations
- Document complex logic with comments

**Example:**
```bash
#!/bin/bash
set -euo pipefail

# Install package with error handling
install_package() {
    local package="$1"
    if apt-cache show "${package}" &>/dev/null; then
        apt-get install -y "${package}" || {
            echo "Error: Failed to install ${package}"
            return 1
        }
    else
        echo "Warning: Package ${package} not found"
        return 0
    fi
}
```

### Python (Control Center)

**Style Guidelines:**

- Follow **PEP 8** style guide
- Use **Black** formatter: `black --line-length 88 file.py`
- Use **type hints** for function signatures
- Use **docstrings** for all public functions/classes
- Run **pylint**: `pylint --rcfile=.pylintrc file.py`

**Example:**
```python
import psutil
from typing import Dict, Optional

def get_cpu_stats() -> Dict[str, float]:
    """Retrieve current CPU usage statistics.
    
    Returns:
        Dict containing 'usage_percent' and 'frequency_mhz'.
    
    Raises:
        RuntimeError: If psutil fails to read CPU data.
    """
    try:
        return {
            "usage_percent": psutil.cpu_percent(interval=1),
            "frequency_mhz": psutil.cpu_freq().current
        }
    except Exception as e:
        raise RuntimeError(f"CPU stats error: {e}") from e
```

### Configuration Files

**INI/CONF files:**
- Use lowercase keys with underscores
- Add comments explaining non-obvious settings
- Group related settings together

**Example:**
```ini
# Dingo Daemon Configuration

[daemon]
enabled = true
auto_start = true
log_level = info

[gaming]
# Enable GameMode for performance optimization
gamemode_enabled = true
gpu_governor = performance
```

---

## ✅ Testing Requirements

### Build Script Testing

**Required Tests:**

1. **Clean Build**: Test on fresh Ubuntu 24.04 install
   ```bash
   sudo ./scripts/build-ubuntu-v2-FIXED.sh 2>&1 | tee build.log
   ```

2. **ISO Boot**: Verify bootability
   ```bash
   qemu-system-x86_64 -m 4G -enable-kvm \
     -cdrom ~/dingo-ubuntu/ubuntu-build/output/dingo-os-v2.iso
   ```

3. **Package Verification**: Check all packages installed
   ```bash
   # After booting ISO in VM:
   dpkg -l | grep steam
   dpkg -l | grep docker
   code --version
   ```

4. **Network Connectivity**: Verify DNS and internet access
   ```bash
   ping -c 3 8.8.8.8
   curl -I https://google.com
   ```

### Control Center Testing

**Required Tests:**

1. **Unit Tests**: Run pytest suite
   ```bash
   cd dashboard
   pytest tests/ -v --cov=src
   ```

2. **UI Testing**: Manual verification
   - Launch application
   - Navigate all tabs
   - Verify data displays correctly
   - Test button actions

3. **Resource Usage**: Check performance
   ```bash
   # Monitor while app runs
   ps aux | grep dingo-control-center
   # Should use < 100MB RAM
   ```

---

## 🔀 Pull Request Process

### Before Submitting

1. **Update Documentation**
   - Update README.md if adding features
   - Update docs/ if changing architecture
   - Add entry to CHANGELOG.md

2. **Sync with Upstream**
   ```bash
   git fetch upstream
   git rebase upstream/main
   git push origin feature/my-contribution --force-with-lease
   ```

3. **Self-Review Checklist**
   - [ ] Code is clean and well-commented
   - [ ] No debug print statements left in code
   - [ ] No hardcoded paths (use variables)
   - [ ] Error handling added for failure points
   - [ ] Commit messages follow convention

### Submitting PR

1. **Create PR on GitHub**
2. **Fill PR Template**:
   ```markdown
   ## Description
   Brief description of changes

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Refactoring

   ## Testing Done
   - [ ] Tested on Ubuntu 24.04
   - [ ] ISO boots successfully
   - [ ] All tests pass

   ## Screenshots (if applicable)
   [Add screenshots]

   ## Related Issues
   Closes #123
   ```

3. **Wait for Review**
   - Maintainers will review within 3-5 days
   - Address feedback promptly
   - Be respectful in discussions

### Review Process

**Reviewers will check:**

- Code quality and style compliance
- Test coverage and passing status
- Documentation completeness
- No breaking changes (or properly documented)
- Security implications
- Performance impact

**Approval Criteria:**

- Minimum 1 maintainer approval
- All CI checks passing
- No unresolved review comments
- CHANGELOG.md updated

---

## 👥 Community Guidelines

### Code of Conduct

All contributors must adhere to our [Code of Conduct](CODE_OF_CONDUCT.md).

**Key Principles:**

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Provide constructive feedback
- Focus on technical merit
- Assume good intentions

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Pull Requests**: Code review and technical discussions

### Getting Help

**For Contributors:**

- Read existing documentation first
- Search closed issues for similar problems
- Ask clear, specific questions
- Provide context and code examples

**Maintainer Response Times:**

- Critical bugs: < 24 hours
- Feature requests: < 1 week
- Documentation: < 3 days
- General questions: < 5 days

---

## 🎯 Contribution Ideas

**Good First Issues:**

- Fix typos in documentation
- Add missing package descriptions
- Improve error messages in build script
- Add screenshots to user guides
- Test ISO on different hardware

**Advanced Contributions:**

- Implement new Control Center features
- Optimize build script performance
- Add automated testing infrastructure
- Create additional profile configurations
- Develop installer improvements

---

## 📄 License

By contributing to Dingo OS, you agree that your contributions will be licensed under the GPL-3.0 License.

---

**Thank you for contributing to Dingo OS!**

Questions? Open an issue or start a discussion on GitHub

---

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/dingo-os.git
cd dingo-os

# Set up development environment
./scripts/setup-dev.sh

# Create feature branch
git checkout -b feature/my-feature
```

---

## Code Standards

### Shell Scripts

- Follow [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html)
- Use shellcheck for linting
- Always quote variables

### Python

- Follow PEP 8
- Use black for formatting
- Use type hints

### Commits

Follow Conventional Commits:
```
feat(module): add new feature
fix(module): fix bug
docs: update documentation
style: formatting changes
refactor: code restructuring
test: add tests
chore: maintenance
```

---

## Pull Request Process

1. Update documentation if needed
2. Add tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Request review

---

## Community

- Be respectful and inclusive
- Follow our [Code of Conduct](CODE_OF_CONDUCT.md)
- Help others in discussions
- Share knowledge and feedback

---

*Thank you for contributing!*
