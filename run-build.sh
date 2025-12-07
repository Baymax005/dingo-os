#!/bin/bash
# Helper script to run build in WSL
# NOTE: This script MUST be run inside WSL (Windows Subsystem for Linux)
# or a native Linux environment.
#
# To use:
# 1. Open WSL terminal
# 2. Navigate to this directory
# 3. Run: sudo bash run-build.sh

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check if running on Linux
if [[ "$(uname -s)" != "Linux" ]]; then
    echo -e "${RED}ERROR: This script must be run in Linux (WSL or native)${NC}"
    echo "Open WSL and run: sudo bash run-build.sh"
    exit 1
fi

# Check if running as root
if [[ $EUID -ne 0 ]]; then
    echo -e "${RED}ERROR: This script must be run as root${NC}"
    echo "Run: sudo bash run-build.sh"
    exit 1
fi

echo -e "${GREEN}=== Dingo OS Build Script ===${NC}"
echo ""

# Copy to Linux filesystem (avoid Windows path issues)
BUILD_LOCATION="$HOME/dingo-build"
echo -e "${YELLOW}Copying files to Linux filesystem...${NC}"
mkdir -p "$BUILD_LOCATION"
cp -r ./* "$BUILD_LOCATION/" 2>/dev/null || true

# Go to Linux location
cd "$BUILD_LOCATION"

# Make scripts executable
chmod +x scripts/*.sh

# Clean old build
echo -e "${YELLOW}Cleaning old build...${NC}"
rm -rf build/

# Start build
echo -e "${GREEN}Starting ISO build...${NC}"
echo ""
bash scripts/build-iso.sh --clean

echo ""
echo -e "${GREEN}Build complete! Check ~/dingo-build/build/output/ for the ISO.${NC}"
