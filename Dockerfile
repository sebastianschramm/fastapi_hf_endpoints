FROM python:3.11-slim as builder

WORKDIR /app

ENV POETRY_VERSION=1.7.1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_HOME=/opt/poetry \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    PATH="/opt/poetry/bin:$PATH"

WORKDIR /app

COPY inference inference
COPY pyproject.toml pyproject.toml 
COPY poetry.lock poetry.lock

RUN apt update && \
    apt install -y curl && \
    curl -sSL https://install.python-poetry.org | python - && \
    poetry install --only main --no-root


FROM python:3.11-slim as runtime

WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv \
    POETRY_HOME=/opt/poetry \
    PATH="/opt/poetry/bin:/app/.venv/bin:$PATH"

COPY --from=builder ${POETRY_HOME} ${POETRY_HOME}
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY --from=builder /app .

CMD ["uvicorn", "inference.server:app", "--host", "0.0.0.0", "--port", "80"]