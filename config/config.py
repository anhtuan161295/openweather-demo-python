from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    database_url: str
    database_port: str
    database_username: str
    database_password: str
    database_name: str
    openweather_api_key: str

    class Config:
        env_file = 'dev.env'
        env_file_encoding = 'utf-8'


settings = Settings()


@lru_cache
def get_settings():
    return settings
