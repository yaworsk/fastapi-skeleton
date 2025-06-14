#!/bin/bash

# Cleanup script for FastAPI skeleton projects
# Usage: ./cleanup-project.sh [project-name]

set -e

PROJECT_NAME="$1"

if [[ -z "$PROJECT_NAME" ]]; then
    echo "Usage: $0 <project-name>"
    echo ""
    echo "Examples:"
    echo "  $0 test-gen-sample"
    echo "  $0 my-blog-api"
    echo ""
    echo "This script will:"
    echo "  • Stop and remove Docker containers"
    echo "  • Remove Docker volumes"
    echo "  • Remove project directory"
    exit 1
fi

echo "🧹 Cleaning up project: $PROJECT_NAME"
echo "=================================="

# Check if project directory exists
if [[ ! -d "$PROJECT_NAME" ]]; then
    echo "⚠️  Project directory '$PROJECT_NAME' not found"
    echo "Will still attempt to clean up containers..."
fi

# Generate container names (same logic as in generator)
CONTAINER_PREFIX=$(echo "$PROJECT_NAME" | sed 's/[^a-zA-Z0-9_-]//g' | sed 's/[-_]\+/_/g' | tr '[:upper:]' '[:lower:]')

# Stop and remove containers
echo "🐳 Stopping containers..."
docker stop "${CONTAINER_PREFIX}_backend" "${CONTAINER_PREFIX}_frontend" "${CONTAINER_PREFIX}_postgres" 2>/dev/null || true
docker rm "${CONTAINER_PREFIX}_backend" "${CONTAINER_PREFIX}_frontend" "${CONTAINER_PREFIX}_postgres" 2>/dev/null || true

# Remove volumes
echo "💾 Removing volumes..."
docker volume rm "${PROJECT_NAME}_postgres_data" 2>/dev/null || true

# Change to project directory and run make down if Makefile exists
if [[ -d "$PROJECT_NAME" && -f "$PROJECT_NAME/Makefile" ]]; then
    echo "📦 Running project cleanup..."
    cd "$PROJECT_NAME"
    make down 2>/dev/null || true
    cd ..
fi

# Remove project directory
if [[ -d "$PROJECT_NAME" ]]; then
    echo "📁 Removing project directory..."
    rm -rf "$PROJECT_NAME"
    echo "✅ Project directory removed"
else
    echo "ℹ️  Project directory was already removed"
fi

echo ""
echo "✅ Cleanup completed for: $PROJECT_NAME"
echo ""
echo "Remaining containers:"
docker ps --format "table {{.Names}}\t{{.Status}}" | grep -E "(backend|frontend|postgres)" || echo "  (none)"
