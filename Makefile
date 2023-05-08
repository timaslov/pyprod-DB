rebuild-docker:
	docker compose build --pull

prod:
	docker compose up -d

infra:
	docker compose up -d postgres nginx

back:
	docker compose up back --build

front:
	docker compose up front --build

back-exec:
	docker compose exec back bash

down:
	docker compose down
