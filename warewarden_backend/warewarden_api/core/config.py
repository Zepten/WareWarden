from pathlib import Path

from pydantic import BaseModel, PostgresDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_PATH = Path(__file__).parent.parent / ".env"


class RunSettings(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class DbSettings(BaseModel):
    username: str = "user"
    password: SecretStr = SecretStr("password")
    host: str = "localhost"
    port: int = 5432
    path: str = "postgres"
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 5
    max_overflow: int = 10
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

    @property
    def url(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.username,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            path=self.path,
        )


class ApiV1Settings(BaseModel):
    prefix: str = "/v1"
    pcs: str = "/pcs"


class ApiSettings(BaseModel):
    prefix: str = "/api"
    health: str = "/health"
    v1: ApiV1Settings = ApiV1Settings()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=ENV_PATH,
        env_file_encoding="utf8",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    api: ApiSettings = ApiSettings()
    run: RunSettings = RunSettings()
    db: DbSettings = DbSettings()


settings = Settings()
print(settings.db.url)
