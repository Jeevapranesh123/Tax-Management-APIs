from databases import DatabaseURL
from starlette.config import Config
from starlette.datastructures import Secret
from pydantic import BaseSettings
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


class Settings:

    PROJECT_NAME = os.getenv("PROJECT_NAME")
    PROJECT_DESCRIPTION = os.getenv("PROJECT_DESCRIPTION")
    API_ROOT_PATH: str = os.getenv("API_ROOT_PATH")
    VERSION = "0.0.1"
    SECRET_KEY = os.getenv("SECRET_KEY")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT"))
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    DATABASE_URL = os.getenv("DATABASE_URL")

    class Config:
        case_sensitive = True


class AuthJWTSettings(BaseSettings):
    authjwt_secret_key: str = os.getenv("SECRET_KEY")


settings = Settings()
auth_jwt_settings = AuthJWTSettings()
