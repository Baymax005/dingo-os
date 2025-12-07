# 👩‍💻 Developer Guide

Contributing to Dingo OS development.

---

## Development Setup

### 1. Fork and Clone

```bash
# Fork on GitHub, then clone
git clone https://github.com/YOUR_USERNAME/dingo-os.git
cd dingo-os

# Add upstream remote
git remote add upstream https://github.com/dingo-os/dingo-os.git
```

### 2. Set Up Development Environment

```bash
# Install development dependencies
./scripts/setup-dev.sh

# This installs:
# - Build tools
# - Linters
# - Testing frameworks
# - Pre-commit hooks
```

### 3. Create Feature Branch

```bash
git checkout -b feature/my-new-feature
```

---

## Repository Structure

```
dingo-os/
├── .github/              # GitHub Actions, templates
│   ├── workflows/        # CI/CD pipelines
│   ├── ISSUE_TEMPLATE/   # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md
├── branding/             # Visual assets
│   ├── backgrounds/      # Wallpapers
│   ├── icons/            # Icon themes
│   ├── logos/            # Logo files
│   └── plymouth/         # Boot splash
├── configs/              # System configurations
│   ├── apt/              # APT sources and preferences
│   ├── dconf/            # GNOME/dconf settings
│   ├── dingo/            # Dingo-specific configs
│   ├── security/         # Firewall, AppArmor, etc.
│   └── systemd/          # Service files
├── dashboard/            # Dingo Control Center
│   ├── src/              # Source code
│   ├── ui/               # GTK UI files
│   └── tests/            # Unit tests
├── docs/                 # Documentation
├── iso-builder/          # ISO generation
│   ├── profiles/         # Build profiles
│   ├── hooks/            # Build hooks
│   └── templates/        # Template files
├── packages/             # Package definitions
│   ├── dev-packages.list
│   ├── gaming-packages.list
│   ├── blockchain-packages.list
│   └── security-packages.list
├── scripts/              # Build and utility scripts
│   ├── build-iso.sh
│   ├── test-vm.sh
│   └── setup-dev.sh
└── tests/                # Integration tests
```

---

## Development Guidelines

### Code Style

**Shell Scripts:**
```bash
# Use shellcheck
shellcheck scripts/*.sh

# Follow Google Shell Style Guide
# - Use snake_case for variables
# - Use UPPER_CASE for constants
# - Always quote variables
```

**Python (Dashboard):**
```bash
# Use black for formatting
black dashboard/src/

# Use flake8 for linting
flake8 dashboard/src/

# Use mypy for type checking
mypy dashboard/src/
```

### Commit Messages

Follow Conventional Commits:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

**Examples:**
```
feat(dashboard): add system monitoring widget
fix(gaming): correct GPU detection for AMD cards
docs(installation): update VM instructions
```

### Branch Naming

```
feature/short-description
fix/issue-number-description
docs/what-is-being-documented
chore/maintenance-task
```

---

## Component Development

### Adding New Packages

1. Determine the package category:
   - `packages/base-packages.list` - Essential packages
   - `packages/dev-packages.list` - Developer tools
   - `packages/gaming-packages.list` - Gaming tools
   - `packages/blockchain-packages.list` - Blockchain tools

2. Add the package:
```bash
echo "package-name" >> packages/dev-packages.list
```

3. Test the build:
```bash
sudo ./scripts/build-iso.sh --test-packages
```

### Adding Configuration Files

1. Create the config in `configs/`:
```bash
mkdir -p configs/myapp
vim configs/myapp/config.conf
```

2. Add to the install manifest:
```bash
# In configs/manifest.yaml
- source: configs/myapp/config.conf
  dest: /etc/myapp/config.conf
  mode: 0644
```

### Developing the Dashboard

```bash
cd dashboard

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run in development mode
python -m dingo_control_center --debug

# Run tests
pytest tests/

# Build for release
python setup.py build
```

### Adding Dingo CLI Commands

1. Create command script in `scripts/commands/`:
```bash
#!/bin/bash
# scripts/commands/mycommand.sh

mycommand_main() {
    echo "My custom command"
}
```

2. Register in `scripts/dingo`:
```bash
# Add to command dispatch
case "$1" in
    mycommand) shift; mycommand_main "$@" ;;
esac
```

---

## Testing

### Unit Tests

```bash
# Run all tests
./scripts/run-tests.sh

# Run specific test
./scripts/run-tests.sh --filter dashboard
```

### Integration Tests

```bash
# Build and test ISO
sudo ./scripts/build-iso.sh
sudo ./scripts/integration-test.sh
```

### Manual Testing Checklist

- [ ] ISO boots successfully
- [ ] Installation completes
- [ ] Desktop loads correctly
- [ ] Control Center launches
- [ ] Developer tools work
- [ ] Gaming mode activates (if included)
- [ ] Network connectivity works
- [ ] Updates install correctly

---

## Pull Request Process

### 1. Prepare Your Changes

```bash
# Update from upstream
git fetch upstream
git rebase upstream/main

# Run tests
./scripts/run-tests.sh

# Run linters
./scripts/lint.sh
```

### 2. Push and Create PR

```bash
git push origin feature/my-feature
```

Then create Pull Request on GitHub.

### 3. PR Requirements

- [ ] Tests pass
- [ ] Linting passes
- [ ] Documentation updated
- [ ] Changelog entry added
- [ ] Commit messages follow convention

### 4. Review Process

1. Automated checks run
2. Maintainer reviews code
3. Address feedback
4. Squash and merge

---

## Release Process

### Version Numbering

We use Semantic Versioning (SemVer):
- `MAJOR.MINOR.PATCH`
- Example: `1.2.3`

### Creating a Release

```bash
# 1. Update version
./scripts/bump-version.sh 1.1.0

# 2. Update changelog
vim docs/CHANGELOG.md

# 3. Create release commit
git add .
git commit -m "chore: release v1.1.0"
git tag v1.1.0

# 4. Push
git push origin main --tags
```

### Release Checklist

- [ ] Version bumped
- [ ] Changelog updated
- [ ] All tests pass
- [ ] ISO builds successfully
- [ ] ISO tested in VM
- [ ] Documentation updated
- [ ] Release notes written

---

## Troubleshooting Development

### Common Issues

**Build fails with missing dependencies:**
```bash
./scripts/setup-dev.sh --reinstall
```

**Tests fail locally but pass in CI:**
```bash
# Clean environment
./scripts/clean.sh --all
./scripts/build-iso.sh --clean
```

**Dashboard won't start:**
```bash
cd dashboard
pip install -r requirements.txt --force-reinstall
```

---

## Resources

- [Ubuntu Packaging Guide](https://packaging.ubuntu.com/)
- [GNOME Developer Documentation](https://developer.gnome.org/)
- [Live CD Customization](https://help.ubuntu.com/community/LiveCDCustomization)
- [Debootstrap Manual](https://wiki.debian.org/Debootstrap)

---

*Questions? Open an issue or join our community chat!*
