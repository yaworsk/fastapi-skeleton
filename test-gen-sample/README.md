# Test Gen Sample

A FastAPI application with Vue.js frontend, PostgreSQL database, and complete development tooling.

## 🚀 Quick Start

1. **Copy environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env file with your configurations if needed
   ```

2. **Start development environment:**
   ```bash
   make dev
   ```

3. **Access applications:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Database: localhost:5432

## 📋 Available Commands

### Development
```bash
make help           # Show all available commands
make dev            # Start complete development environment
make up             # Start all services
make down           # Stop all services
make clean          # Clean up containers and volumes
```

### Database
```bash
make migrate        # Apply pending migrations
make migrate-create MSG="description"  # Create new migration
make shell-db       # Access PostgreSQL shell
```

### Testing
```bash
make test           # Run all backend tests
make test-cov       # Run tests with coverage report
make test-watch     # Run tests in watch mode
```

### Code Quality
```bash
make lint           # Run all linters
make format         # Auto-format all code
```

## 🏗️ Architecture

This project follows a clean MVC architecture:

- **Models** (`backend/app/models/`): Database models
- **Views** (`backend/app/api/`): API endpoints
- **Controllers** (`backend/app/controllers/`): Business logic
- **Repositories** (`backend/app/repositories/`): Data access layer
- **Schemas** (`backend/app/schemas/`): API validation

## 🧪 Testing

The project includes comprehensive testing with:
- Real PostgreSQL database (no mocking)
- Transaction-based test isolation
- Coverage reporting
- Separate test database container

## 📚 Adding Features

1. Create model in `backend/app/models/`
2. Create schema in `backend/app/schemas/`
3. Create repository in `backend/app/repositories/`
4. Create controller in `backend/app/controllers/`
5. Create endpoints in `backend/app/api/v1/endpoints/`
6. Register routes in `backend/app/api/v1/api.py`
7. Create migration: `make migrate-create MSG="Add new feature"`
8. Write tests in `backend/tests/`

## 🚀 Deployment

For production deployment:
1. Set `ENVIRONMENT=production` in environment variables
2. Configure production database
3. Set secure `SECRET_KEY`
4. Enable HTTPS
5. Set up reverse proxy

---

Generated with [FastAPI Skeleton Generator](https://github.com/your-repo/fastapi-skeleton)
