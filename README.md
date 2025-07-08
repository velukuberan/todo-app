# Todo App using FastAPI

A simple todo app using FastAPI, Postgres, and React with full Docker support.

## 🚀 Quick Start with Docker

### Prerequisites
- Docker
- Docker Compose

### Running the Application

1. **Clone and navigate to the project:**
   ```bash
   cd todo-app
   ```

2. **Build and start all services:**
   ```bash
   make build
   make up
   ```

   Or run in detached mode:
   ```bash
   make up-d
   ```

3. **Access the applications:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/documentations
   - Database: localhost:5432

### Development Commands

```bash
# Start all services
make up

# Start in detached mode
make up-d

# Stop all services
make down

# Access containers
make bash          # Backend shell
make frontend-bash # Frontend shell
make db            # Database shell

# Linting
make lint          # Check code
make lint-fix      # Fix linting issues
```

## 🏗️ Architecture

- **Frontend**: React app running on port 3000
- **Backend**: FastAPI app running on port 8000
- **Database**: PostgreSQL running on port 5432

## 🔧 Development

### Frontend Development
- Hot reload enabled
- Connected to backend API
- Environment variables configured for API communication

### Backend Development
- Hot reload enabled with uvicorn
- CORS configured for frontend communication
- PostgreSQL database with persistent storage

### Database
- PostgreSQL 15
- Persistent data storage
- Accessible from host machine for debugging

## 📁 Project Structure

```
todo-app/
├── frontend/          # React application
├── app/              # FastAPI application modules
├── main.py           # FastAPI entry point
├── docker-compose.yml # Docker services configuration
├── Dockerfile        # Backend Docker configuration
├── frontend/Dockerfile # Frontend Docker configuration
└── Makefile          # Development commands
```

## 🌐 API Endpoints

- `GET /` - Health check
- `GET /shipments` - Get all shipments
- `GET /shipments/{id}` - Get shipment by ID
- `POST /shipments` - Create new shipment
- `GET /documentations` - API documentation

## 🔄 Environment Variables

### Backend
- `DATABASE_URL` - PostgreSQL connection string
- `CORS_ORIGINS` - Allowed CORS origins

### Frontend
- `REACT_APP_API_URL` - Backend API URL
- `CHOKIDAR_USEPOLLING` - Enable file watching in Docker

## 🐳 Docker Services

1. **frontend** - React development server
2. **web** - FastAPI backend server
3. **db** - PostgreSQL database

All services are configured with proper networking and volume mounts for development. 

