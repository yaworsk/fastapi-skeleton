#!/usr/bin/env python3
"""
FastAPI Project Customization Script

This script customizes template files by replacing placeholder variables
with project-specific values.
"""

import os
import re
import sys
import secrets
import string
from pathlib import Path
from typing import Dict, Any

def generate_secret_key(length: int = 32) -> str:
    """Generate a secure random secret key."""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def sanitize_project_name(name: str) -> str:
    """Convert project name to a valid identifier."""
    # Remove special characters and spaces, convert to lowercase
    sanitized = re.sub(r'[^a-zA-Z0-9_-]', '', name.replace(' ', '_'))
    # Remove consecutive underscores/hyphens
    sanitized = re.sub(r'[-_]+', '_', sanitized)
    # Ensure it doesn't start with a number
    if sanitized and sanitized[0].isdigit():
        sanitized = f"project_{sanitized}"
    return sanitized.lower()

def create_project_title(name: str) -> str:
    """Create a human-readable project title."""
    # Convert snake_case or kebab-case to Title Case
    title = name.replace('_', ' ').replace('-', ' ')
    return ' '.join(word.capitalize() for word in title.split())

def get_next_available_port(start_port: int, taken_ports: set) -> int:
    """Find the next available port starting from start_port."""
    port = start_port
    while port in taken_ports:
        port += 1
    return port

def replace_in_file(file_path: Path, replacements: Dict[str, str]) -> None:
    """Replace template variables in a file."""
    try:
        if not file_path.exists():
            print(f"❌ File does not exist: {file_path}")
            return
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for placeholder, value in replacements.items():
            content = content.replace(f"{{{{{placeholder}}}}}", str(value))
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"✅ Customized {file_path}")
        
    except Exception as e:
        print(f"❌ Error customizing {file_path}: {e}")

def customize_project(project_path: Path, config: Dict[str, Any]) -> None:
    """Customize all template files in the project."""
    
    # Files that need customization
    template_files = [
        'docker-compose.yml',
        'docker-compose.test.yml',
        '.env.example',
        'frontend/package.json',
        'backend/tests/conftest.py',
    ]
    
    # Files that need renaming from .template
    template_renames = {
        'README.md.template': 'README.md',
        'Makefile.template': 'Makefile',
    }
    
    replacements = {
        'PROJECT_NAME': config['project_name'],
        'PROJECT_TITLE': config['project_title'],
        'DATABASE_NAME': config['database_name'],
        'CONTAINER_PREFIX': config['container_prefix'],
        'SECRET_KEY': config['secret_key'],
        'BACKEND_PORT': config['backend_port'],
        'FRONTEND_PORT': config['frontend_port'],
        'DB_PORT': config['db_port'],
        'TEST_DB_PORT': config['test_db_port'],
    }
    
    # Customize template files
    for file_path in template_files:
        full_path = project_path / file_path
        if full_path.exists():
            replace_in_file(full_path, replacements)
    
    # Rename and customize template files
    for template_name, final_name in template_renames.items():
        template_path = project_path / template_name
        final_path = project_path / final_name
        
        if template_path.exists():
            # Copy content and customize
            replace_in_file(template_path, replacements)
            # Rename file
            template_path.rename(final_path)
            print(f"✅ Created {final_name} from template")

def main():
    """Main customization function."""
    if len(sys.argv) != 8:
        print("Usage: customize.py <project_path> <project_name> <backend_port> <frontend_port> <db_port> <test_db_port> <container_prefix>")
        sys.exit(1)
    
    project_path = Path(sys.argv[1])
    project_name = sys.argv[2]
    backend_port = sys.argv[3]
    frontend_port = sys.argv[4]
    db_port = sys.argv[5]
    test_db_port = sys.argv[6]
    container_prefix = sys.argv[7]
    
    # Generate project configuration
    config = {
        'project_name': project_name,
        'project_title': create_project_title(project_name),
        'database_name': f"{project_name}_db",
        'container_prefix': container_prefix,
        'secret_key': generate_secret_key(),
        'backend_port': backend_port,
        'frontend_port': frontend_port,
        'db_port': db_port,
        'test_db_port': test_db_port,
    }
    
    print(f"🔧 Customizing project: {config['project_title']}")
    print(f"📁 Project path: {project_path}")
    print(f"🔑 Generated secret key: {config['secret_key'][:8]}...")
    print(f"🐳 Container prefix: {container_prefix}")
    print(f"🌐 Ports - Backend: {backend_port}, Frontend: {frontend_port}, DB: {db_port}")
    print()
    
    customize_project(project_path, config)
    
    print()
    print("✅ Project customization completed!")

if __name__ == "__main__":
    main()
