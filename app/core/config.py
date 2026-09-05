from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "upskill-api"
    environment: str = "local"
    database_url: str = "postgresql+psycopg://upskill:upskill@localhost:5432/upskill"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
