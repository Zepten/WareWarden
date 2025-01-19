# WareWarden

[![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)](./LICENSE)

## Описание

WareWarden — это open-source система для ведения и поддержания актуальной информации о компьютерном оборудовании и программном обеспечении в локальной сети.

WareWarden с точки зрения пользователя представляет из себя веб-приложение. В его основе лежит серверная часть (бэкенд) на Python/FastAPI, который предоставляет REST API для взаимодействия с клиентской частью (фронтендом) и другими сервисами в локальной сети.

WareWarden является личным пет-проектом и не связан с какой-либо организацией.

## Стек технологий

- Бэкенд
    - База данных
        - [PostgreSQL](https://www.postgresql.org/) (реляционная СУБД)
    - API
        - [Python](https://www.python.org/) (язык программирования)
        - [Poetry](https://python-poetry.org/) (инструмент для управления зависимостями в Python)
        - [FastAPI](https://fastapi.tiangolo.com/) (Python-фреймворк для API)
        - [Pydantic](https://docs.pydantic.dev/latest/) (валидация данных)
        - [SQLAlchemy](https://www.sqlalchemy.org/) (ORM для базы данных)
            - [asyncpg](https://github.com/MagicStack/asyncpg) (асинхронный драйвер для PostgreSQL)
        - [Alembic](https://github.com/sqlalchemy/alembic) (управление миграциями базы данных)
- Фронтенд:
    - [TypeScript](https://www.typescriptlang.org/) (типизированный JavaScript)
    - [Vite](https://vite.dev/) (инструмент сборки фронтенда)
    - [Tailwind CSS](https://tailwindcss.com/) (CSS-фреймворк)
    - [React](https://react.dev/) (библиотека для создания пользовательских интерфейсов)
        - [Ant Design](https://ant.design/) (библиотека компонентов для React)
- DevOps
    - [Docker](https://www.docker.com/) / [Docker Compose](https://docs.docker.com/compose/) (контейнеризация)

## Установка для разработки (Linux / WSL2)

Для запуска WareWarden необходимы `Docker` и `Docker Compose`. Для активации виртуального окружения Python в целях удобства разработки следует установить `Python` и `Poetry`.

1. Клонировать репозиторий:

```bash
git clone https://github.com/Zepten/WareWarden
cd WareWarden
```

2. Установить зависимости для Python в виртуальное окружение внутри директории проекта с помощью Poetry:

```bash
cd warewarden_backend
poetry install --no-root
cd ..
```

3. Настроить конфигурацию в файле `.dev.env`

```bash
cp .env.example .dev.env
nano .dev.env
```

4. Собрать и запустить контейнеры с помощью Docker Compose:

```bash
docker compose --env-file .dev.env up --build -d
```

5. Применить миграцию базы данных с помощью Alembic:

```bash
docker exec warewarden-api-service-1 sh -c "cd ./warewarden_api/ && alembic upgrade head"
```

6. Проверить доступность API: http://localhost:8080/docs

## Лицензия

WareWarden распространяется под лицензией [MIT](https://opensource.org/license/MIT)