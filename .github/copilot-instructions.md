# Copilot / AI Agent Instructions — Bela

Purpose: quickly orient an AI coding agent to be productive in this Django-based repo.

- **Big picture:** This is a small Django project (project package `config`) providing REST endpoints with DRF. Key runtime pieces:
  - Django settings and URL routing live under [config](config).
  - Database is PostgreSQL and is expected to run as a Docker service named `db` (see [config/settings.py](config/settings.py) and `docker-compose.yml`).
  - Packaging uses `pyproject.toml` + Poetry; Python requirement is >=3.14.

- **Where to look first:**
  - Project entry: [manage.py](manage.py)
  - Settings: [config/settings.py](config/settings.py)
  - URL routing: [config/urls.py](config/urls.py)
  - Container build: [Dockerfile](Dockerfile) and [docker-compose.yml](docker-compose.yml)
  - Dependencies: [pyproject.toml](pyproject.toml)

- **Run / dev workflow (concrete commands):**
  - Local with Poetry (recommended when iterating locally):
    - `poetry install`
    - `poetry run python manage.py migrate`
    - `poetry run python manage.py runserver 0.0.0.0:8000`
  - With Docker Compose (mirrors production-like DB):
    - `docker compose up --build` (service `web` maps 8000, `db` is postgres)
    - Inside container: `docker compose exec web poetry run python manage.py migrate`

- **DB & env specifics:**
  - `config/settings.py` reads `POSTGRES_NAME`, `POSTGRES_USER`, `POSTGRES_PASSWORD`; the DB host is `db` (Docker service). Keep those env var names when adding scripts or CI.

- **Project conventions & patterns:**
  - Add Django apps in `INSTALLED_APPS` in [config/settings.py](config/settings.py).
  - Register app routes by including `path(..., include(...))` in [config/urls.py](config/urls.py).
  - Use DRF for APIs (package `djangorestframework` is installed).
  - The Dockerfile uses Poetry and `poetry install --no-root` — prefer restoring dependencies via Poetry in CI as well.

- **Testing & CI:**
  - No tests directory was found. If adding tests, follow Pytest + Django patterns and ensure `poetry add --dev pytest pytest-django` and a simple `pytest` run in CI.

- **Editing guidance for PRs:**
  - Keep changes small and focused: add a Django app, update `INSTALLED_APPS`, add migrations, and register routes in `config/urls.py`.
  - If changing DB schema, include generated migrations and show the `manage.py makemigrations`/`migrate` commands in PR description.

- **Integration points to be careful of:**
  - DB connectivity assumptions: code expects a `db` host (docker-compose). Locally without Docker you must set env vars to point to a running Postgres instance.
  - Container entrypoint runs `poetry run python manage.py runserver`; long-running background processes should be added explicitly.

- **When you need clarification:**
  - Ask where new REST endpoints should be mounted (URL prefix) and whether to add a new Django app or extend an existing one.

If anything here is unclear or you'd like specific examples (example API view, serializer, or a small app scaffold), tell me which area to expand and I will update this file.
