from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

KEY = os.getenv('SECRET_KEY')

class Settings(BaseSettings):
    SECRET_KEY: str = KEY
    ALGORITHMS:  str = "HSH256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    class Config:
        env_file = ".env"



settings = Settings()
