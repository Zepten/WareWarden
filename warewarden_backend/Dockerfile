###############################################################################
# Stage 1. Base image
###############################################################################

FROM python:3.13.1-alpine3.21 AS python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=2.0.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apk update && apk add --no-cache curl

###############################################################################
# Stage 2. Builder image
###############################################################################

FROM python-base AS builder-base

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./

RUN poetry install --no-root --no-interaction --without dev

###############################################################################
# Stage 3. Development image
###############################################################################

FROM python-base AS development

COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

WORKDIR $PYSETUP_PATH

RUN poetry install --no-root --no-interaction

WORKDIR /src

EXPOSE 8080
ENTRYPOINT /docker-entrypoint.sh $0 $@
CMD ["python", "./warewarden_api/main.py"]

###############################################################################
# TODO: Stage 4. Linting image
###############################################################################

# FROM development AS lint
# RUN black --config ./pyproject.toml --check app tests
# RUN isort --settings-path ./pyproject.toml --recursive --check-only
# CMD ["tail", "-f", "/dev/null"]

###############################################################################
# TODO: Stage 5. Testing image
###############################################################################

# FROM development AS test
# RUN coverage run --rcfile ./pyproject.toml -m pytest ./tests
# RUN coverage report --fail-under 95