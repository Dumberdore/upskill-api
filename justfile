set dotenv-load := true

default:
    just --list

dev:
    docker compose up -d db
    uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

sync:
    uv sync --locked

test:
    docker compose up -d db
    RUN_INTEGRATION_TESTS=1 TEST_DATABASE_URL=postgresql+psycopg://upskill:upskill@localhost:5432/upskill_test uv run pytest

lint:
    uv run ruff check .

format:
    uv run ruff format .

format-check:
    uv run ruff format --check .

typecheck:
    uv run mypy app

audit:
    uv run pip-audit

check:
    just lint
    just format-check
    just typecheck
    just test

migrate:
    docker compose up -d db
    uv run alembic upgrade head

container-build:
    docker build -t upskill-api:local .

container-run:
    docker run --rm -p 8000:8000 -e DATABASE_URL=postgresql+psycopg://upskill:upskill@host.docker.internal:5432/upskill upskill-api:local
