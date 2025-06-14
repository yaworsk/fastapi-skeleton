# FastAPI Skeleton Generator

A production-ready project generator for FastAPI applications with Vue.js frontend, PostgreSQL database, and complete development tooling. Think "rails new" but for FastAPI!

## 🚀 Quick Start

### Generate a New Project

```bash
# Clone the generator
git clone <your-repo-url> fastapi-skeleton
cd fastapi-skeleton

# Create a new project
./fastapi-init my-awesome-api

# Or use make command
make init PROJECT=my-blog-api
```

Your new project will be created with:
- ✅ Clean MVC architecture
- ✅ Docker containerization 
- ✅ Real database testing (no mocking)
- ✅ Comprehensive linting setup
- ✅ Auto-generated secure configurations
- ✅ Git repository initialized
- ✅ Development environment started

## 🎯 Generator Features

### Rails-like Experience
```bash
./fastapi-init my-project        # Create new project
./fastapi-init .                 # Initialize current directory
./fastapi-init ../company/api    # Create in specific location
```

### Smart Configuration
- **Unique Ports**: Automatically finds available ports to avoid conflicts
- **Secure Secrets**: Generates random SECRET_KEY for each project
- **Custom Names**: Project-specific container and database names
- **No Overwrites**: Prevents accidental re-initialization

### Flexible Options
```bash
./fastapi-init my-api --port 8001              # Custom backend port
./fastapi-init my-api --frontend 3001          # Custom frontend port
./fastapi-init my-api --db 5433                # Custom database port
./fastapi-init my-api --no-git                 # Skip git initialization
./fastapi-init my-api --no-start               # Skip auto-start
```

## 📁 Generated Project Structure

```
my-awesome-api/
├── .env                         # Customized environment
├── .gitignore                   # Git ignore rules
├── README.md                    # Project-specific documentation
├── Makefile                     # Development commands
├── fastapi-init.lock            # Prevents re-initialization
├── docker-compose.yml           # Main services (custom ports/names)
├── docker-compose.test.yml      # Test environment
├── backend/                     # FastAPI application
│   ├── Dockerfile
│   ├── requirements.txt         # Production dependencies
│   ├── requirements-dev.txt     # Development dependencies
│   ├── alembic.ini             # Database migration config
│   ├── pytest.ini             # Test configuration
│   ├── pyproject.toml          # Python tooling config
│   ├── app/
│   │   ├── main.py             # FastAPI app entry
│   │   ├── config.py           # Application settings
│   │   ├── database.py         # Database connection
│   │   ├── api/                # API routes (versioned)
│   │   ├── controllers/        # Business logic layer
│   │   ├── models/             # SQLAlchemy models
│   │   ├── repositories/       # Data access layer
│   │   ├── schemas/            # Pydantic schemas
│   │   └── seed.py             # Sample data seeding
│   ├── alembic/                # Database migrations
│   └── tests/                  # Comprehensive test suite
├── frontend/                   # Vue.js application
│   ├── package.json            # Customized project name
│   ├── .eslintrc.js           # ESLint configuration
│   ├── .prettierrc            # Prettier configuration
│   └── src/                   # Vue.js source code
└── postgres/
    └── init.sql               # Database initialization
```

## 🏗️ Architecture

### MVC Pattern Implementation

The generated projects follow a strict MVC architecture:

**Models** (`backend/app/models/`)
- SQLAlchemy ORM models
- Database schema definitions
- Entity relationships

**Views** (`backend/app/api/`)
- FastAPI route handlers
- HTTP request/response handling
- API versioning (v1, v2, etc.)

**Controllers** (`backend/app/controllers/`)
- Business logic orchestration
- Service coordination
- Data transformation

**Repositories** (`backend/app/repositories/`)
- Data access abstraction
- Database query encapsulation
- CRUD operations

**Schemas** (`backend/app/schemas/`)
- Pydantic models for validation
- API contracts definition
- Serialization/deserialization

## 🧪 Testing Infrastructure

Every generated project includes:

### Real Database Testing
- **No Mocking**: Uses actual PostgreSQL for tests
- **Isolation**: Each test runs in a rollback transaction
- **Performance**: Fast execution with proper cleanup
- **Reliability**: Tests real database interactions

### Test Configuration
- **pytest**: Comprehensive test framework
- **Coverage**: Built-in coverage reporting
- **Fixtures**: Reusable test data
- **Separation**: Unit and integration test markers

### Test Commands
```bash
make test           # Run all tests
make test-cov       # Run with coverage report
make test-watch     # Watch mode for development
```

## 🎨 Code Quality

### Python (Backend)
- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Style guide enforcement
- **mypy**: Type checking (optional)

### JavaScript/Vue (Frontend)
- **ESLint**: Code linting with Vue plugin
- **Prettier**: Code formatting

### Quality Commands
```bash
make lint           # Check all code quality
make format         # Auto-fix formatting issues
make type-check     # Run type checking
```

## 🐳 Docker Development

### Service Architecture
Each generated project gets:
- **Unique Container Names**: `myproject_backend`, `myproject_postgres`
- **Custom Ports**: Auto-detected available ports
- **Isolated Networks**: No conflicts with other projects
- **Volume Mounts**: Hot reload for development

### Development Workflow
```bash
make dev            # Complete environment setup
make up             # Start services
make down           # Stop services
make logs           # View service logs
make shell-backend  # Access backend container
```

## 📋 Available Commands

### Generator Commands
```bash
# Using the generator
./fastapi-init --help              # Show usage
make init PROJECT=name             # Create via Makefile
make test-generator                # Test the generator
make clean-test                    # Clean test projects
make cleanup-project PROJECT=name # Clean specific project

# Manual cleanup
./cleanup-project.sh my-project   # Clean specific project

# Generated project commands (run in project directory)
make dev                          # Start development environment
make test                         # Run test suite
make lint                         # Code quality checks
make migrate                      # Database migrations
make seed                         # Populate sample data
make down                         # Stop project containers
```

## 🚀 Examples

### Basic Project Creation
```bash
# Simple project with defaults
./fastapi-init blog-api

# Result:
# - Backend: http://localhost:8000
# - Frontend: http://localhost:3000  
# - Database: localhost:5432
```

### Custom Ports (Multiple Projects)
```bash
# First project (defaults)
./fastapi-init user-service

# Second project (auto-detected ports)
./fastapi-init inventory-service
# - Backend: http://localhost:8001 (auto-incremented)
# - Frontend: http://localhost:3001
# - Database: localhost:5433
```

### Corporate/Team Setup
```bash
# Create in specific directory with custom config
./fastapi-init ../company-apis/payment-service \
  --port 8010 \
  --frontend 3010 \
  --db 5440

# Skip git if using corporate git workflow
./fastapi-init enterprise-api --no-git --no-start
```

### Development Workflow
```bash
# 1. Generate project
./fastapi-init my-startup-api

# 2. Project automatically starts, or manually:
cd my-startup-api
make dev

# 3. Develop with hot reload
# Edit files in backend/app/ and frontend/src/

# 4. Run tests during development
make test-watch

# 5. Check code quality before commit
make lint format

# 6. Create database changes
make migrate-create MSG="Add user profiles"
make migrate
```

## 🔧 Customization

### Environment Variables
Each project gets a customized `.env` file:
```env
# Automatically customized for your project
POSTGRES_DB=myproject_db
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/myproject_db
SECRET_KEY=<randomly-generated-secure-key>
BACKEND_CORS_ORIGINS=["http://localhost:3001"]  # Matches frontend port
```

### Container Configuration
Docker services are automatically customized:
```yaml
# docker-compose.yml (example for "blog-api" project)
services:
  postgres:
    container_name: blog_api_postgres
    environment:
      POSTGRES_DB: blog_api_db
    ports:
      - "5432:5432"  # Or auto-detected available port

  backend:
    container_name: blog_api_backend
    ports:
      - "8000:8000"  # Or auto-detected available port
```

## 🛡️ Safety Features

### Prevention Mechanisms
- **Lock File**: `fastapi-init.lock` prevents re-initialization
- **Directory Check**: Won't overwrite existing projects
- **Port Validation**: Ensures ports are available
- **Name Validation**: Enforces valid project names

### Validation Rules
```bash
# Valid project names
./fastapi-init my-api           ✅
./fastapi-init user_service     ✅
./fastapi-init blog-2024        ✅

# Invalid project names  
./fastapi-init "my api"         ❌ (spaces)
./fastapi-init 123-api          ❌ (starts with number)
./fastapi-init my@api           ❌ (special characters)
```

## 🔍 Troubleshooting

### Common Issues

**Port Conflicts**
```bash
# Generator automatically finds available ports
./fastapi-init my-api --port 8000  # If 8000 busy, uses 8001
```

**Permission Errors**
```bash
# Make scripts executable
chmod +x fastapi-init scripts/*.py scripts/*.sh
# Or use make command
make update-permissions
```

**Docker Issues**
```bash
# Check Docker is running
docker --version
docker-compose --version

# Clean up if needed
make clean-test  # Clean test projects
```

**Generator Testing**
```bash
# Test the generator itself
make test-generator    # Creates test-project-sample
make clean-test       # Removes test projects
```

## 📚 Adding Features to Generated Projects

When working with a generated project, follow the MVC pattern:

1. **Add Model** (`app/models/post.py`)
2. **Add Schema** (`app/schemas/post.py`) 
3. **Add Repository** (`app/repositories/post_repository.py`)
4. **Add Controller** (`app/controllers/post_controller.py`)
5. **Add Endpoints** (`app/api/v1/endpoints/posts.py`)
6. **Register Routes** (update `app/api/v1/api.py`)
7. **Create Migration** (`make migrate-create MSG="Add posts"`)
8. **Write Tests** (`tests/api/test_posts.py`)

## 🤝 Contributing

### Generator Development
1. Modify templates in `skeleton/`
2. Update customization logic in `scripts/customize.py`
3. Test with `make test-generator`
4. Update documentation

### Generated Project Development  
1. Follow MVC architecture
2. Write tests for new features
3. Run `make lint` before committing
4. Use conventional commit messages

## 🐛 Troubleshooting

### Common Issues

**Port conflicts:**
```bash
# Generator automatically finds available ports
./fastapi-init my-api --port 8000  # If 8000 busy, uses 8001
```

**Permission errors:**
```bash
# Make scripts executable
chmod +x fastapi-init scripts/*.py scripts/*.sh
# Or use make command
make update-permissions
```

**Docker issues:**
```bash
# Check Docker is running
docker --version
docker-compose --version

# Clean up test projects
make clean-test

# Clean up specific project
make cleanup-project PROJECT=my-project
# or manually:
./cleanup-project.sh my-project

# Stop all containers for a project
cd my-project && make down
```

**Generator testing:**
```bash
# Test the generator itself
make test-generator    # Creates test-project-sample
make clean-test       # Removes test projects
```

## 📄 License

This project is licensed under the MIT License.

---

**Happy coding with FastAPI! 🚀**

Generate your next project in seconds, not hours.
