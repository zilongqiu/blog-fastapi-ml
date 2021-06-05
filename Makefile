.PHONY: up
up:
	docker compose up --force-recreate --build

.PHONY: down
down:
	docker compose down

.PHONY: logs
logs:
	docker compose logs -f

.PHONY: enter
enter:
	docker exec -it blog-fastapi-ml bash

.PHONY: test
test:
	docker compose exec blog-fastapi-ml pytest