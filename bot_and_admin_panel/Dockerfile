FROM python:3.9-slim

WORKDIR /app

RUN pip install uv

COPY ./pyproject.toml .

RUN uv sync --no-dev

COPY . .

CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "bot_and_admin_panel.wsgi:application"]