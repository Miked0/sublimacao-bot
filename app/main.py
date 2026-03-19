import logging
from fastapi import FastAPI, Request, BackgroundTasks, HTTPException, Header
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from app.bot.flow import processar_mensagem
from app.integrations.evolution import evolution
from app.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Bot WhatsApp - Sublimacao iniciando...")
    yield
    logger.info("Bot WhatsApp - Sublimacao encerrando...")


app = FastAPI(
    title="Sublimacao Bot",
    version="1.0.0",
    description="Bot WhatsApp para loja de sublimacao - gerencia pedidos automaticamente",
    lifespan=lifespan,
)


@app.get("/health")
def health():
    """Endpoint de health check - verifica se o servico esta no ar."""
    return {
        "status": "ok",
        "version": "1.0.0",
        "service": "sublimacao-bot",
    }


@app.get("/")
def root():
    """Rota raiz - redireciona para /health."""
    return {"message": "Sublimacao Bot ativo", "docs": "/docs", "health": "/health"}


@app.post("/webhook")
async def webhook(
    request: Request,
    background_tasks: BackgroundTasks,
):
    """
    Endpoint principal que recebe eventos da Evolution API.
    Aceita apenas eventos do tipo 'messages.upsert'.
    Processa a mensagem em background para resposta imediata ao webhook.
    """
    body = await request.json()
    logger.info(f"Webhook recebido: evento={body.get('event')}")

    try:
        # Filtrar apenas eventos de nova mensagem
        evento = body.get("event")
        if evento != "messages.upsert":
            return {"status": "ignored", "reason": f"evento '{evento}' nao processado"}

        msg_data = body.get("data", {})

        # Ignorar mensagens enviadas pelo proprio bot
        if msg_data.get("key", {}).get("fromMe"):
            return {"status": "ignored", "reason": "fromMe=true"}

        # Ignorar mensagens de grupos
        remote_jid = msg_data.get("key", {}).get("remoteJid", "")
        if "@g.us" in remote_jid:
            return {"status": "ignored", "reason": "grupo ignorado"}

        # Extrair telefone (limpar sufixo WhatsApp)
        telefone = remote_jid.replace("@s.whatsapp.net", "")

        # Extrair texto da mensagem (suporta texto simples e estendido)
        mensagem = msg_data.get("message", {})
        texto = (
            mensagem.get("conversation")
            or mensagem.get("extendedTextMessage", {}).get("text", "")
            or ""
        ).strip()

        if not texto:
            return {"status": "ignored", "reason": "sem texto na mensagem"}

        logger.info(f"Mensagem recebida de {telefone}: {texto[:50]}")

        # Processar em background para nao bloquear o webhook
        background_tasks.add_task(processar_e_responder, telefone, texto)
        return {"status": "queued", "telefone": telefone}

    except (KeyError, TypeError) as e:
        logger.error(f"Erro ao parsear webhook: {e}")
        return JSONResponse(
            status_code=422,
            content={"status": "parse_error", "detail": str(e)},
        )
    except Exception as e:
        logger.error(f"Erro inesperado no webhook: {e}")
        return JSONResponse(
            status_code=500,
            content={"status": "error", "detail": str(e)},
        )


async def processar_e_responder(telefone: str, texto: str):
    """Processa mensagem e envia resposta via Evolution API."""
    try:
        resposta = await processar_mensagem(telefone, texto)
        if resposta:
            await evolution.send_text(telefone, resposta)
            logger.info(f"Resposta enviada para {telefone}")
    except Exception as e:
        logger.error(f"Erro ao processar/responder para {telefone}: {e}")
