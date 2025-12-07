# 🛠️ Developer Tools Guide

Complete guide to using Dingo OS development tools.

---

## Overview

Dingo OS comes pre-configured with a comprehensive development environment:

| Category | Tools |
|----------|-------|
| Languages | Python, Node.js, Go, Rust, Java |
| Containers | Docker, Podman, Docker Compose |
| Editors | VS Code, Neovim, JetBrains Toolbox |
| Databases | PostgreSQL, MySQL, Redis, MongoDB |
| Version Control | Git, GitHub CLI, GitLab CLI |

---

## Programming Languages

### Python

**Installed Version:** Python 3.12

```bash
# Check version
python3 --version

# Package managers
pip3 install package-name
pipenv install package-name
poetry add package-name

# Create virtual environment
python3 -m venv myenv
source myenv/bin/activate
```

**Pre-installed Tools:**
- pip, pipenv, poetry
- virtualenv
- pylint, black, mypy
- ipython, jupyter

### Node.js

**Installed Version:** Node.js 20 LTS

```bash
# Check version
node --version
npm --version

# Package managers
npm install package-name
yarn add package-name
pnpm add package-name

# Version management with nvm
nvm install 18
nvm use 18
```

**Pre-installed Tools:**
- npm, yarn, pnpm
- nvm (Node Version Manager)
- nodemon, pm2
- typescript, ts-node

### Go

**Installed Version:** Go 1.21

```bash
# Check version
go version

# Install package
go install github.com/user/package@latest

# Create new module
go mod init myproject
```

### Rust

**Installed Version:** Latest stable

```bash
# Check version
rustc --version
cargo --version

# New project
cargo new myproject
cargo build
cargo run
```

### Java

**Installed Version:** OpenJDK 21 LTS

```bash
# Check version
java --version
javac --version

# Build tools
mvn --version
gradle --version
```

---

## Editors and IDEs

### Visual Studio Code

Pre-installed with extensions:
- Python
- JavaScript/TypeScript
- Go
- Rust Analyzer
- Docker
- GitLens
- Prettier

```bash
# Launch
code .

# Open specific folder
code /path/to/project
```

### Neovim

Custom configuration included:
- LSP support
- Auto-completion
- File explorer (NvimTree)
- Fuzzy finder (Telescope)

```bash
# Launch
nvim

# Configuration location
~/.config/nvim/
```

### JetBrains Toolbox

Install JetBrains IDEs:

```bash
# Launch Toolbox
jetbrains-toolbox

# Available IDEs:
# - IntelliJ IDEA
# - PyCharm
# - WebStorm
# - GoLand
# - Rider
```

---

## Containers

### Docker

```bash
# Check status
docker --version
systemctl status docker

# Run container
docker run -it ubuntu bash

# Docker Compose
docker-compose up -d
docker-compose down
```

### Podman

Docker-compatible alternative:

```bash
# Run container (rootless)
podman run -it ubuntu bash

# Docker compatibility
alias docker=podman
```

### Kubernetes Tools

```bash
# kubectl
kubectl version
kubectl get pods

# Minikube (local cluster)
minikube start
minikube dashboard

# k9s (TUI dashboard)
k9s
```

---

## Databases

### Quick Start

```bash
# Dingo database manager
dingo db list              # List available DBs
dingo db start postgres    # Start PostgreSQL
dingo db stop postgres     # Stop PostgreSQL
dingo db status            # Show running DBs
```

### PostgreSQL

```bash
# Start
dingo db start postgres

# Connect
psql -U postgres -h localhost

# Default credentials:
# User: postgres
# Password: postgres
# Port: 5432
```

### MySQL

```bash
# Start
dingo db start mysql

# Connect
mysql -u root -p

# Default credentials:
# User: root
# Password: mysql
# Port: 3306
```

### Redis

```bash
# Start
dingo db start redis

# Connect
redis-cli

# Port: 6379
```

### MongoDB

```bash
# Start
dingo db start mongodb

# Connect
mongosh

# Port: 27017
```

### Database GUI

**DBeaver** - Universal database client:
```bash
dbeaver
```

---

## Version Control

### Git Configuration

```bash
# Check configuration
git config --list

# Pre-configured aliases
git st     # status
git co     # checkout
git br     # branch
git ci     # commit
git lg     # pretty log
```

### GitHub CLI

```bash
# Authenticate
gh auth login

# Create repo
gh repo create myrepo

# Create PR
gh pr create

# Check issues
gh issue list
```

### GitLab CLI

```bash
# Authenticate
glab auth login

# Create MR
glab mr create
```

---

## Project Templates

### Create New Project

```bash
# Node.js project
dingo dev new node myapp
# Options: express, fastify, nest, next

# Python project
dingo dev new python myproject
# Options: flask, django, fastapi

# Go project
dingo dev new go myservice
# Options: gin, fiber, echo

# Full-stack project
dingo dev new fullstack myapp
# Options: react-express, vue-fastapi, next-prisma
```

### Template Structure

```bash
dingo dev new node myapp
```

Creates:
```
myapp/
├── src/
├── tests/
├── package.json
├── .gitignore
├── .eslintrc.js
├── README.md
└── docker-compose.yml
```

---

## Development Workflow

### 1. Start Development Environment

```bash
# Open Dingo Control Center
dingo-control-center

# Or from terminal
dingo dev env
```

### 2. Start Required Services

```bash
# Start databases
dingo db start postgres redis

# Start Docker services
docker-compose up -d
```

### 3. Develop

```bash
# Open editor
code .

# Run tests
npm test
# or
pytest
# or
go test ./...
```

### 4. Commit Changes

```bash
git add .
git commit -m "feat: add new feature"
git push
```

---

## Performance Tips

### Faster Builds

```bash
# Use ccache for C/C++
export CC="ccache gcc"
export CXX="ccache g++"

# Parallel builds
make -j$(nproc)
npm run build --parallel
```

### Development Optimization

```bash
# Enable development profile
dingo profile dev

# This optimizes:
# - File system caching
# - Memory allocation
# - Swap usage
```

---

## Troubleshooting

### Common Issues

**Docker permission denied:**
```bash
sudo usermod -aG docker $USER
newgrp docker
```

**Node modules issues:**
```bash
rm -rf node_modules package-lock.json
npm install
```

**Python environment issues:**
```bash
# Use pipenv or poetry instead of pip
pipenv install
poetry install
```

---

*For more details, see individual language documentation or run `dingo dev help`*
