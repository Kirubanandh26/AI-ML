from pydantic_settings import BaseSettings, SettingsConfigDict
from app.utils import BASE_DIR

print("BASE_DIR", BASE_DIR)
class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    PROJECT_NAME: str
    API_DOC_PATH: str
    GEMINI_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env")


settings = Settings()
