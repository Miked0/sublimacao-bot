from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Evolution API
    EVOLUTION_API_URL: str
    EVOLUTION_API_KEY: str
    EVOLUTION_INSTANCE: str

    # Google Sheets
    GOOGLE_CREDENTIALS_JSON: str
    SPREADSHEET_ID: str

    # Geral
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()
