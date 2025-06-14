#!/bin/bash

# Quick test script for the FastAPI generator
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "🧪 Testing FastAPI Generator"
echo "============================"

# Clean up any existing test project
echo "🧹 Cleaning up previous test..."
rm -rf test-gen-sample || true

# Make scripts executable
echo "🔧 Making scripts executable..."
chmod +x fastapi-init scripts/*.py scripts/*.sh

# Test the generator
echo "🚀 Testing generator..."
./fastapi-init test-gen-sample --no-start --no-git

# Verify the project was created
if [[ -d "test-gen-sample" ]]; then
    echo "✅ Test project directory created"
    
    # Check for key files
    echo "🔍 Checking generated files..."
    
    key_files=(
        ".env.example"
        ".env" 
        "docker-compose.yml"
        "Makefile"
        "README.md"
        "fastapi-init.lock"
        "backend/app/main.py"
        "frontend/package.json"
    )
    
    all_good=true
    
    for file in "${key_files[@]}"; do
        if [[ -f "test-gen-sample/$file" ]]; then
            echo "  ✅ $file"
        else
            echo "  ❌ $file MISSING"
            all_good=false
        fi
    done
    
    if $all_good; then
        echo ""
        echo "🎉 Generator test PASSED!"
        echo "📁 Test project location: $(pwd)/test-gen-sample"
        echo ""
        echo "To test the generated project:"
        echo "  cd test-gen-sample"
        echo "  make dev"
    else
        echo ""
        echo "❌ Generator test FAILED - some files are missing"
        exit 1
    fi
else
    echo "❌ Test project directory not created"
    exit 1
fi

echo ""
echo "🧹 To clean up: make clean-test"
echo "    or manually: cd test-gen-sample && make down && cd .. && rm -rf test-gen-sample"
