include .env

.PHONY: up build create_db down stop prune ps bash bash_db logs

default: up

up:
	@echo "Starting up containers for $(PROJECT_NAME)..."
	docker-compose  up -d

create_django_app:
	@echo "Starting up containers for $(PROJECT_NAME)..."
	docker-compose -f docker-compose.yml -f docker-compose-django.yml up web

build:
	@echo "Building and starting up containers for $(PROJECT_NAME)..."
	docker-compose build

down: stop
stop:
	@echo "Stopping containers for $(PROJECT_NAME)..."
	@docker-compose stop

prune:
	@echo "Removing containers for $(PROJECT_NAME)..."
	@docker-compose down -v

ps:
	@docker ps --filter name='$(PROJECT_NAME)*'

bash:
	docker exec -i -t '$(PROJECT_NAME)_web' /bin/bash

bash_db:
	docker exec -i -t '$(PROJECT_NAME)_db' /bin/bash

logs:
	@docker-compose logs -f $(filter-out $@,$(MAKECMDGOALS))

%:
	@: