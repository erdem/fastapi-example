import logging
import os
import pathlib
from functools import lru_cache

from dotenv import dotenv_values, load_dotenv
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent
    ASSETS_DIR: str = "assets"
    DEBUG: bool
    ENV: str = os.environ.get("FASTAPI_ENV", "development")
    APP_NAME: str
    PDF_SERVICE_API_KEY: str
    LOGGING_LEVEL: int = logging.INFO

    @property
    def is_production(self):
        return self.ENV == "production"


class DevelopmentConfig(BaseConfig):
    DEBUG: bool = True
    LOGGING_LEVEL: int = logging.DEBUG


class ProductionConfig(BaseConfig):
    DEBUG: bool = False


class TestingConfig(BaseConfig):
    DEBUG: bool = False


@lru_cache()
def get_settings():
    config_cls_dict = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "testing": TestingConfig,
    }

    env_dict = dotenv_values(dotenv_path=".env")
    config_name = env_dict.pop("FASTAPI_ENV", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls(**env_dict)


settings = get_settings()
load_dotenv()
