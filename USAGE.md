# FastAPI Generator - Quick Usage Guide

## 🚀 Getting Started

### 1. Make Scripts Executable
```bash
cd /home/Workspace/fastapi-skeleton
chmod +x fastapi-init scripts/*.py scripts/*.sh
```

### 2. Create Your First Project
```bash
# Basic project creation
./fastapi-init my-awesome-api

# Or with custom configuration
./fastapi-init my-blog-api --port 8001 --frontend 3001
```

### 3. Generated Project Commands
```bash
cd my-awesome-api

# Start development environment
make dev

# Run tests
make test

# Check code quality
make lint

# Database operations
make migrate-create MSG="Add new feature"
make migrate
```

## 📁 What Gets Generated

```
my-awesome-api/
├── .env                    # Customized environment
├── fastapi-init.lock      # Prevents re-initialization
├── Makefile               # Development commands
├── README.md              # Project documentation
├── backend/               # FastAPI app with MVC architecture
├── frontend/              # Vue.js application
└── docker-compose.yml     # Containerized services
```

## 🎯 Key Features

- **Unique Configuration**: Each project gets its own ports, database names, containers
- **Real Database Testing**: No mocking - uses actual PostgreSQL with transaction rollback
- **Complete Linting**: Python (Black, isort, flake8) + JavaScript (ESLint, Prettier)
- **MVC Architecture**: Clean separation of concerns
- **Hot Reload**: Both backend and frontend support live editing

## 🔧 Testing the Generator
```bash
# Test the generator itself
make test-generator

# Clean up test projects
make clean-test
```

## 🎉 Example Workflow

```bash
# 1. Generate new project
./fastapi-init blog-api

# 2. Development starts automatically, or:
cd blog-api
make dev

# 3. Access your application
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs

# 4. Add a new feature (example: Posts)
# - Create model: backend/app/models/post.py
# - Create schema: backend/app/schemas/post.py  
# - Create repository: backend/app/repositories/post_repository.py
# - Create controller: backend/app/controllers/post_controller.py
# - Create endpoints: backend/app/api/v1/endpoints/posts.py
# - Register routes: update backend/app/api/v1/api.py
# - Create migration: make migrate-create MSG="Add posts"
# - Write tests: backend/tests/api/test_posts.py

# 5. Quality checks
make lint format test
```

Happy coding! 🎉
