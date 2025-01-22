from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from core.models import db_helper
from api import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    print("Waiting for engine to dispose.")  # TODO: add logger
    await db_helper.dispose()
    print("Engine disposed.")  # TODO: add logger


main_app = FastAPI(
    title="WareWarden API",
    description="API for WareWarden web application",
    license_info={"name": "MIT License", "url": "https://opensource.org/license/mit"},
    docs_url=f"{settings.api.prefix}/docs",
    redoc_url=None,
    openapi_url=f"{settings.api.prefix}/openapi.json",
    swagger_ui_oauth2_redirect_url=f"{settings.api.prefix}/docs/oauth2-redirect",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)
main_app.include_router(router=api_router, prefix=settings.api.prefix)

origins = [
    "http://localhost",
    "http://localhost:5000",
    "https://localhost",
    "https://localhost:5000",
    "http://127.0.0.1",
    "http://127.0.0.1:5000",
    "https://127.0.0.1",
    "https://127.0.0.1:5000",
    f"http://{settings.react_app.host}:5000",
    f"https://{settings.react_app.host}:5000",
]

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
