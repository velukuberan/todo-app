.SILENT:

# Build and run
build:
	docker-compose build

up:
	docker-compose up

up-d:
	docker-compose up -d

down:
	docker-compose down

# Utilities
pyv:
	docker-compose exec web python --version

bash:
	docker-compose exec web bash

frontend-bash:
	docker-compose exec frontend sh

db:
	docker-compose exec db bash

# Linting
.PHONY: lint lint-fix

lint:
	docker-compose exec web ruff check .

lint-fix:
	docker-compose exec web ruff check . --fix
