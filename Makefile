build:
	docker compose build
start:
	docker compose up -d
collectstatic:
	docker compose exec django uv run python manage.py collectstatic
start_bot:
	docker compose exec -d django uv run python manage.py bot
set_certificate:
	docker compose exec nginx /usr/local/bin/setup-certbot.sh
stop:
	docker compose stop
migrate:
	docker compose exec django uv run python manage.py migrate
add_admin:
	docker compose exec django uv run python manage.py createsuperuser