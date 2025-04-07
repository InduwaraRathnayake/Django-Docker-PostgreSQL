# Django PostgreSQL User Management System

A complete user management system built with Django and PostgreSQL, containerized with Docker for easy setup and deployment

## Project Overview
This project demonstrates a full-stack web application with:

- PostgreSQL database running in Docker
- pgAdmin for database management
- Django REST API for user management operations
- Makefile for streamlined development workflow

## Prerequisites
- Python 3.8+
- Docker and Docker Compose
- Make

## Installation
1. Clone the repository
```bash
git clone https://github.com/InduwaraRathnayake/Django-Docker-PostgreSQL.git
cd Django
```

2. Create and activate a virtual environment
```bash
python -m venv virtualEnv
cd virtualEnv/scripts
source activate  # For Windows: activate.bat
cd ../..
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Start PostgreSQL database
Make sure in the Django/ (root)

```bash
make run
```

5. Run the Django server
```bash
make run-server
```

## Project Structure
```text
Django/
├── django/
│   └── mainProject/
│       ├── userApp/
│       ├── mainProject/
│       │   └── .env           # Django environment variables
├── postgres/
│   ├── docker-compose.yml     # Docker services configuration
│   ├── init.sql               # Database initialization script
│   └── .env                   # Database environment variables
├── Makefile                   # Command shortcuts
└── README.md                  # Project documentation
```

## Database Setup
The PostgreSQL database is automatically initialized with:

- A users table with columns for id, username, email, password, and creation timestamp
- 10 sample user records

## API Endpoints

| Endpoint             | Method | Description       |
|----------------------|--------|-------------------|
| /users               | GET    | Get all users     |
| /users/<id>/         | GET    | Get user by ID    |
| /users/create/       | POST   | Create a new user |
| /users/update/<id>/  | PUT    | Update a user     |
| /users/delete/<id>/  | DELETE | Delete a user     |

## Available Commands

### Docker Operations

```bash

# Start PostgreSQL and pgAdmin containers
make run

# Stop all containers
make stop

# View container logs
make logs

# List running containers
make ps

# Access PostgreSQL shell
make psql

# Rebuild containers
make build

# Remove containers, volumes, and data directories
make clean

# Restart containers
make restart

```

### Django Operations
```bash
# Run Django development server
make run-server

# When syncing with an existing DB to avoid duplication
make run-server-fake 

# Open Django shell
make shell

# Run tests
make test

# Clear and recreate migrations
make clear-migrations

```

## Environment Variables

### PostgreSQL (.env)

```text
POSTGRES_PASSWORD=
POSTGRES_USER=
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=
PGADMIN_DEFAULT_EMAIL=
PGADMIN_DEFAULT_PASSWORD=
```

### Django (.env)

```text
DB_PASSWORD=
DB_USER=
DB_HOST=localhost
DB_PORT=5432
DB_NAME=
DB_DRIVER=django.db.backends.postgresql
```

- Match Database Name, User and Password in both .env files

## Accessing the Application

- Django API: http://localhost:8000/
- pgAdmin: http://localhost:15433/ (login with credentials from .env)

## Troubleshooting
If you encounter issues with the Makefile, ensure:

1. Your Makefile is saved without a file extension (not MakeFile)
2. Commands are indented with tabs, not spaces
3. You're running in a bash-compatible environment

For database connection issues, check:

1. The database container is running (`make ps`)
2. Environment variables match between Django and PostgreSQL
3. PostgreSQL user has proper permissions
