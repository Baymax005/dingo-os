# 🤝 Contributing to Dingo OS

Thank you for your interest in contributing to Dingo OS!

---

## How to Contribute

### Reporting Bugs

1. Check if the issue already exists
2. Create a new issue with:
   - Clear title
   - Steps to reproduce
   - Expected vs actual behavior
   - System information
   - Screenshots if applicable

### Suggesting Features

1. Check existing feature requests
2. Create a feature request with:
   - Clear use case
   - Proposed solution
   - Alternatives considered

### Code Contributions

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

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
