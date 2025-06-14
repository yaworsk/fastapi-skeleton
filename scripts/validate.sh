#!/bin/bash
# Validation helper functions for fastapi-init

validate_project_name() {
    local name="$1"
    
    # Check if name is empty
    if [[ -z "$name" ]]; then
        echo "❌ Project name cannot be empty"
        return 1
    fi
    
    # Check length
    if [[ ${#name} -lt 2 ]]; then
        echo "❌ Project name must be at least 2 characters long"
        return 1
    fi
    
    if [[ ${#name} -gt 50 ]]; then
        echo "❌ Project name must be less than 50 characters long"
        return 1
    fi
    
    # Check for valid characters (alphanumeric, hyphens, underscores)
    if [[ ! "$name" =~ ^[a-zA-Z0-9_-]+$ ]]; then
        echo "❌ Project name can only contain letters, numbers, hyphens, and underscores"
        return 1
    fi
    
    # Check if it starts with a letter
    if [[ ! "$name" =~ ^[a-zA-Z] ]]; then
        echo "❌ Project name must start with a letter"
        return 1
    fi
    
    return 0
}

validate_directory() {
    local dir="$1"
    
    # Check if directory already exists and is not empty
    if [[ -d "$dir" && "$(ls -A "$dir" 2>/dev/null)" ]]; then
        echo "❌ Directory '$dir' already exists and is not empty"
        return 1
    fi
    
    # Check if we can create the directory
    local parent_dir=$(dirname "$dir")
    if [[ ! -w "$parent_dir" ]]; then
        echo "❌ Cannot write to parent directory '$parent_dir'"
        return 1
    fi
    
    return 0
}

check_existing_project() {
    local dir="$1"
    
    # Check for lock file
    if [[ -f "$dir/fastapi-init.lock" ]]; then
        echo "❌ Directory already contains a FastAPI project (found fastapi-init.lock)"
        return 1
    fi
    
    # Check for FastAPI project files
    if [[ -f "$dir/docker-compose.yml" && -f "$dir/backend/app/main.py" ]]; then
        echo "❌ Directory already contains a FastAPI project"
        return 1
    fi
    
    return 0
}

is_port_available() {
    local port="$1"
    
    # Check if port is in valid range
    if [[ "$port" -lt 1024 || "$port" -gt 65535 ]]; then
        return 1
    fi
    
    # Check if port is in use (basic check)
    if command -v lsof >/dev/null 2>&1; then
        if lsof -i ":$port" >/dev/null 2>&1; then
            return 1
        fi
    elif command -v netstat >/dev/null 2>&1; then
        if netstat -tuln | grep ":$port " >/dev/null 2>&1; then
            return 1
        fi
    fi
    
    return 0
}

find_available_ports() {
    local base_backend_port="$1"
    local base_frontend_port="$2"
    local base_db_port="$3"
    
    # Find available ports starting from base ports
    local backend_port=$base_backend_port
    local frontend_port=$base_frontend_port
    local db_port=$base_db_port
    local test_db_port=$((base_db_port + 1000))
    
    # Find available backend port
    while ! is_port_available "$backend_port"; do
        backend_port=$((backend_port + 1))
        if [[ "$backend_port" -gt 9000 ]]; then
            echo "❌ Cannot find available backend port"
            return 1
        fi
    done
    
    # Find available frontend port
    while ! is_port_available "$frontend_port" || [[ "$frontend_port" == "$backend_port" ]]; do
        frontend_port=$((frontend_port + 1))
        if [[ "$frontend_port" -gt 4000 ]]; then
            echo "❌ Cannot find available frontend port"
            return 1
        fi
    done
    
    # Find available database port
    while ! is_port_available "$db_port" || [[ "$db_port" == "$backend_port" ]] || [[ "$db_port" == "$frontend_port" ]]; do
        db_port=$((db_port + 1))
        if [[ "$db_port" -gt 6000 ]]; then
            echo "❌ Cannot find available database port"
            return 1
        fi
    done
    
    # Find available test database port
    while ! is_port_available "$test_db_port" || [[ "$test_db_port" == "$backend_port" ]] || [[ "$test_db_port" == "$frontend_port" ]] || [[ "$test_db_port" == "$db_port" ]]; do
        test_db_port=$((test_db_port + 1))
        if [[ "$test_db_port" -gt 7000 ]]; then
            echo "❌ Cannot find available test database port"
            return 1
        fi
    done
    
    echo "$backend_port $frontend_port $db_port $test_db_port"
    return 0
}

check_dependencies() {
    local missing_deps=()
    
    # Check for required commands
    if ! command -v docker >/dev/null 2>&1; then
        missing_deps+=("docker")
    fi
    
    if ! command -v docker-compose >/dev/null 2>&1; then
        missing_deps+=("docker-compose")
    fi
    
    if ! command -v python3 >/dev/null 2>&1; then
        missing_deps+=("python3")
    fi
    
    if [[ ${#missing_deps[@]} -gt 0 ]]; then
        echo "❌ Missing required dependencies: ${missing_deps[*]}"
        echo "   Please install the missing dependencies and try again."
        return 1
    fi
    
    return 0
}
