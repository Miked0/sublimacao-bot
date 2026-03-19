import httpx
from app.config import settings


class EvolutionAPI:
    """Cliente para a Evolution API - envia mensagens WhatsApp."""

    def __init__(self):
        self.base_url = settings.EVOLUTION_API_URL.rstrip("/")
        self.headers = {
            "apikey": settings.EVOLUTION_API_KEY,
            "Content-Type": "application/json",
        }

    async def send_text(self, phone: str, text: str) -> dict:
        """Envia mensagem de texto para um numero WhatsApp."""
        url = f"{self.base_url}/message/sendText/{settings.EVOLUTION_INSTANCE}"
        payload = {
            "number": phone,
            "text": text,
        }
        async with httpx.AsyncClient(timeout=15) as client:
            resp = await client.post(url, json=payload, headers=self.headers)
            resp.raise_for_status()
            return resp.json()

    async def send_list(self, phone: str, title: str, description: str, options: list[str]) -> dict:
        """Envia mensagem de lista (menu interativo)."""
        rows = [{"title": opt, "rowId": str(i + 1)} for i, opt in enumerate(options)]
        url = f"{self.base_url}/message/sendList/{settings.EVOLUTION_INSTANCE}"
        payload = {
            "number": phone,
            "title": title,
            "description": description,
            "buttonText": "Ver opcoes",
            "sections": [{"title": "Opcoes", "rows": rows}],
        }
        async with httpx.AsyncClient(timeout=15) as client:
            resp = await client.post(url, json=payload, headers=self.headers)
            resp.raise_for_status()
            return resp.json()


evolution = EvolutionAPI()
