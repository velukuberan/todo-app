.SILENT:

# Build and run
build:
	docker-compose build

up:
	docker-compose up

# Utilities
pyv:
	docker-compose exec web python --version

bash:
	docker-compose exec web bash

db:
	docker-compose exec db bash

# Linting
.PHONY: lint lint-fix

lint:
	docker-compose exec web ruff check .

lint-fix:
	docker-compose exec web ruff check . --fix
