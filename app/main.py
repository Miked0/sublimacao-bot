from fastapi import FastAPI, Request, BackgroundTasks
from app.bot.flow import processar_mensagem
from app.integrations.evolution import enviar_mensagem

app = FastAPI(title="Sublimacao Bot", version="1.0.0")


@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0.0"}


@app.post("/webhook")
async def webhook(request: Request, background_tasks: BackgroundTasks):
    body = await request.json()

    try:
        evento = body.get("event")
        if evento != "messages.upsert":
feat: adiciona app/main.py com FastAPI e endpoint webhook
        msg_data = body.get("data", {})

        # Ignorar mensagens enviadas pelo proprio bot
        if msg_data.get("key", {}).get("fromMe"):
            return {"status": "ignored"}

        # Extrair telefone e texto
        telefone = msg_data["key"]["remoteJid"].replace("@s.whatsapp.net", "")
        mensagem = msg_data.get("message", {})
        texto = (
            mensagem.get("conversation")
            or mensagem.get("extendedTextMessage", {}).get("text", "")
        )

        if not texto:
            return {"status": "no_text"}

        # Processar em background para nao bloquear o webhook
        background_tasks.add_task(processar_e_responder, telefone, texto)
        return {"status": "queued"}

    except (KeyError, TypeError) as e:
        return {"status": "parse_error", "detail": str(e)}


async def processar_e_responder(telefone: str, texto: str):
    resposta = await processar_mensagem(telefone, texto)
    await enviar_mensagem(telefone, resposta)
