#!/bin/bash
# Development helper script for Dingo OS

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

show_help() {
    cat << EOF
Dingo OS Development Helper

Usage: $0 <command> [options]

Commands:
    setup       Setup development environment
    run         Run the Control Center in development mode
    test        Run all tests
    lint        Run linters on Python code
    docs        Generate documentation
    clean       Clean build artifacts
    build       Build the ISO (requires root)

Examples:
    $0 setup        # Install dependencies
    $0 run          # Launch Control Center
    $0 test         # Run test suite
    $0 build        # Build ISO image
EOF
}

setup_dev() {
    echo -e "${BLUE}Setting up development environment...${NC}"
    
    # Install Python dependencies
    echo "Installing Python dependencies..."
    cd "$PROJECT_ROOT/dashboard"
    pip3 install -r requirements.txt
    
    # Install pre-commit hooks if available
    if command -v pre-commit &> /dev/null; then
        pre-commit install
        echo -e "${GREEN}✓ Pre-commit hooks installed${NC}"
    fi
    
    echo -e "${GREEN}✓ Development environment ready${NC}"
}

run_app() {
    echo -e "${BLUE}Starting Dingo Control Center...${NC}"
    cd "$PROJECT_ROOT/dashboard/src"
    python3 -m dingo_control_center
}

run_tests() {
    echo -e "${BLUE}Running tests...${NC}"
    cd "$PROJECT_ROOT"
    bash scripts/test.sh
}

run_lint() {
    echo -e "${BLUE}Running linters...${NC}"
    
    cd "$PROJECT_ROOT/dashboard/src"
    
    # Flake8
    if command -v flake8 &> /dev/null; then
        echo "Running flake8..."
        flake8 dingo_control_center/ || true
    fi
    
    # Black (check only)
    if command -v black &> /dev/null; then
        echo "Running black..."
        black --check dingo_control_center/ || true
    fi
    
    # MyPy
    if command -v mypy &> /dev/null; then
        echo "Running mypy..."
        mypy dingo_control_center/ || true
    fi
}

generate_docs() {
    echo -e "${BLUE}Generating documentation...${NC}"
    
    # Generate API docs if sphinx is available
    if command -v sphinx-build &> /dev/null; then
        cd "$PROJECT_ROOT/docs"
        make html
        echo -e "${GREEN}✓ Documentation generated in docs/_build/html${NC}"
    else
        echo -e "${YELLOW}Sphinx not installed. Skipping API documentation.${NC}"
    fi
}

clean_project() {
    echo -e "${BLUE}Cleaning build artifacts...${NC}"
    
    cd "$PROJECT_ROOT"
    
    # Python cache
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
    find . -type f -name "*.pyo" -delete 2>/dev/null || true
    
    # Build artifacts
    rm -rf build/ dist/ *.egg-info 2>/dev/null || true
    
    echo -e "${GREEN}✓ Cleaned${NC}"
}

build_iso() {
    echo -e "${BLUE}Building Dingo OS ISO...${NC}"
    
    if [ "$EUID" -ne 0 ]; then
        echo -e "${YELLOW}Warning: ISO build requires root privileges${NC}"
        echo "Run: sudo $0 build"
        exit 1
    fi
    
    cd "$PROJECT_ROOT"
    bash scripts/build-iso.sh
}

# Main
case "${1:-help}" in
    setup)
        setup_dev
        ;;
    run)
        run_app
        ;;
    test)
        run_tests
        ;;
    lint)
        run_lint
        ;;
    docs)
        generate_docs
        ;;
    clean)
        clean_project
        ;;
    build)
        build_iso
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo "Unknown command: $1"
        echo ""
        show_help
        exit 1
        ;;
esac
