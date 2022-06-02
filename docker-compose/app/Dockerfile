FROM python:3.10.0-slim-buster

ENV PYTHONUNBUFFERED=1 \
    APP_HOME=/app/ \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_NO_INTERACTION=1 \
    POETRY_HOME="/opt/poetry" \
    PATH="/opt/poetry/bin:$PATH"

RUN apt-get update && \
    apt-get install -y curl git openssl build-essential python-dev libpq-dev postgresql-client && \
    mkdir $APP_HOME && useradd -m -s $(which bash) python && \
    chown -R python $APP_HOME

ADD ../.. $APP_HOME
WORKDIR $APP_HOME

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

EXPOSE 5000
USER python

CMD ["uvicorn", "geoname_api.api.app:app", "--host", "0.0.0.0", "--port", "5000", "--workers", "1"]