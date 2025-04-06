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