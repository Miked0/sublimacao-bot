from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Evolution API
    EVOLUTION_API_URL: str
    EVOLUTION_API_KEY: str
    EVOLUTION_INSTANCE: str

    # Google Sheets
    # Aceita JSON inline (para Railway) OU caminho do arquivo (para local)
    GOOGLE_CREDENTIALS_JSON: Optional[str] = None   # JSON string completo
    GOOGLE_CREDENTIALS_FILE: str = "credentials.json"  # caminho do arquivo
    SPREADSHEET_ID: str

    # Webhook
    WEBHOOK_SECRET: Optional[str] = None  # opcional - valida origem das requisicoes

    # Geral
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"
    PORT: int = 8000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
