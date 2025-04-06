# Run docker-compose up from postgres directory
run:
	cd postgres && docker-compose up -d

# Stop and remove containers from postgres directory
stop:
	cd postgres && docker-compose down

# View logs of running containers
logs:
	cd postgres && docker-compose logs -f

# List running containers
ps:
	cd postgres && docker-compose ps

# Access PostgreSQL shell
psql:
	cd postgres && docker-compose exec database psql -U induwara -d initial_db

# Rebuild containers
build:
	cd postgres && docker-compose build

# Clean up volumes and networks (full cleanup)
clean:
	cd postgres && docker-compose down -v --remove-orphans
	rm -rf postgres/db-data
	rm -rf postgres/pgadmin-data
    
# Restart containers
restart:
	cd postgres && docker-compose restart

# Django Commands
run-server:
	cd django/mainProject && \
	echo "Starting Django server..." && \
	echo "Create migrations" && \
	python manage.py makemigrations userApp && \
	echo "==========================" && \
	echo "Migrate" && \
	python manage.py migrate && \
	echo "==========================" && \
	echo "Run server" && \
	python manage.py runserver 0.0.0.0:8000

shell:
	cd django/mainProject && python manage.py shell

test:
	cd django/mainProject && python manage.py test userApp

clear-migrations:
	@echo "WARNING: This will delete all migrations (except __init__.py)!" && \
	read -p "Are you sure? (y/N): " confirm && \
	if [ "$$confirm" = "y" ]; then \
		cd django/mainProject && \
		echo "Clearing migrations..." && \
		find . -path "*/migrations/*.py" -not -name "__init__.py" -delete && \
		find . -path "*/migrations/*.pyc"  -delete && \
		echo "==========================" && \
		echo "Create migrations" && \
		python manage.py makemigrations userApp && \
		echo "==========================" && \
		echo "Migrate" && \
		python manage.py migrate; \
	else \
		echo "Aborted."; \
	fi


