# WareWarden

[![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)](./LICENSE)

## Описание

WareWarden — это open-source система для ведения и поддержания актуальной информации о компьютерном оборудовании и программном обеспечении в локальной сети.

WareWarden с точки зрения пользователя представляет из себя веб-приложение. В его основе лежит серверная часть (бэкенд) на Python/FastAPI, который предоставляет REST API для взаимодействия с клиентской частью (фронтендом) и другими сервисами в локальной сети.

WareWarden является личным пет-проектом и не связан с какой-либо организацией.

## Стек технологий

- Бэкенд
    - Веб-сервер
        - [Nginx](https://nginx.org) (обратный прокси сервер)
    - База данных
        - [PostgreSQL](https://www.postgresql.org/) (реляционная СУБД)
    - API
        - [Python](https://www.python.org/) (язык программирования)
        - [Poetry](https://python-poetry.org/) (инструмент для управления зависимостями в Python)
        - [FastAPI](https://fastapi.tiangolo.com/) (Python-фреймворк для API)
        - [Pydantic](https://docs.pydantic.dev/latest/) (валидация данных)
        - [SQLAlchemy](https://www.sqlalchemy.org/) (ORM для базы данных)
            - [asyncpg](https://github.com/MagicStack/asyncpg) (асинхронный драйвер для PostgreSQL)
            - [Alembic](https://github.com/sqlalchemy/alembic) (инструмент для миграций базы данных)
        - [Gunicorn](https://gunicorn.org/) (WSGI HTTP-сервер для Python)
- Фронтенд:
    - [TypeScript](https://www.typescriptlang.org/) (типизированный JavaScript)
    - [Vite](https://vite.dev/) (инструмент сборки фронтенда)
    - [Tailwind CSS](https://tailwindcss.com/) (CSS-фреймворк)
    - [React](https://react.dev/) (библиотека для создания пользовательских интерфейсов)
        - [Ant Design](https://ant.design/) (библиотека компонентов для React)
    - [Axios](https://axios-http.com/ru/docs/intro) (HTTP-клиент на основе Promise)
- DevOps
    - [Docker](https://www.docker.com/) / [Docker Compose](https://docs.docker.com/compose/) (контейнеризация)

## Установка для разработки (Linux / WSL2)

Для запуска WareWarden необходимы `Docker` и `Docker Compose`. Для активации виртуального окружения Python для разработки бэкенда следует установить `Python` и `Poetry`. Также следует установить `Node.js` для разработки фронтенда.

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

3. Установить зависимости для Node.js:

```bash
cd warewarden_frontend
npm install
cd ..
```

4. Настроить конфигурацию в файле `.dev.env`

```bash
cp .env.example .dev.env
nano .dev.env
```

5. Собрать и запустить контейнеры с помощью Docker Compose:

```bash
docker compose --env-file .dev.env up --build -d
```

6. Применить миграцию базы данных с помощью Alembic:

```bash
docker exec warewarden-api-service-1 sh -c "cd ./warewarden_api/ && alembic upgrade head"
```

7. Проверить доступность приложения: http://localhost

8. Проверить доступность API и его документации: http://localhost/api/docs

## Лицензия

WareWarden распространяется под лицензией [MIT](https://opensource.org/license/MIT)