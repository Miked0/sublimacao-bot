# 🤖 sublimacao-bot

> Bot de pedidos via WhatsApp com FastAPI + Google Sheets para loja de sublimação

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Configura%C3%A7%C3%B5es%20Finais-orange.svg)](#)

---

## 🚀 Sobre o Projeto

Automação completa de pedidos para loja de sublimação via WhatsApp.
O cliente conversa com um bot guiado, confirma o pedido e tudo é registrado automaticamente no Google Sheets com painel visual para o lojista.

## 🛠 Stack

| Componente | Tecnologia |
|---|---|
| Gateway WhatsApp | Evolution API |
| Backend | Python + FastAPI |
| Planilha | Google Sheets (gspread) |
| Hospedagem | Railway / Render |
| Sessões | Dict em memória (MVP) / Redis (escala) |

## 📁 Estrutura do Projeto

```
sublimacao-bot/
├── app/
│   ├── main.py              # FastAPI + webhook endpoint
│   ├── config.py            # Settings e variáveis de ambiente
│   ├── bot/
│   │   ├── flow.py          # 5 etapas do fluxo de pedido
│   │   ├── messages.py      # Templates de mensagem
│   │   └── session.py       # Session Manager em memória
│   └── integrations/
│       ├── evolution.py     # Cliente Evolution API (WhatsApp)
│       └── sheets.py        # Cliente Google Sheets
├── scripts/
│   └── setup_sheets.py      # Setup automatico da planilha de produção
├── docs/
│   ├── fase-1-setup.md
│   ├── fase-2-fluxo-bot.md
│   ├── fase-3-google-sheets.md
│   ├── fase-4-painel-lojista.md
│   ├── fase-5-notificacao-status.md
│   ├── fase-6-escala-100-pedidos.md
│   ├── fase-7-storytelling.md
│   └── fase-8-go-live.md    # ⭐ PROXIMA ETAPA
├── .env.example
├── Dockerfile
├── railway.toml
└── requirements.txt
```

## 📊 Status das Fases

| Fase | Descrição | Status |
|------|-----------|--------|
| Fase 0 | Direção do Projeto | ✅ Concluída |
| Fase 1 | Conectar WhatsApp ao Backend | ✅ Concluída |
| Fase 2 | Fluxo de Conversa do Bot | ✅ Concluída |
| Fase 3 | Integração com Google Sheets | ✅ Concluída |
| Fase 4 | Painel do Lojista | ✅ Concluída |
| Fase 5 | Notificação de Status para o Cliente | ✅ Concluída |
| Fase 6 | Escala para 100+ Pedidos/Dia | ✅ Concluída |
| Fase 7 | Storytelling e Documentação | ✅ Concluída |
| **Fase 8** | **Configurações Finais & Go Live** | **🔶 Em andamento** |

## ⚡ Quick Start

### 1. Clonar e instalar dependências

```bash
git clone https://github.com/Miked0/sublimacao-bot.git
cd sublimacao-bot
pip install -r requirements.txt
```

### 2. Configurar variáveis de ambiente

```bash
cp .env.example .env
# Edite o .env com suas credenciais
```

### 3. Setup da planilha (executar uma vez)

```bash
python scripts/setup_sheets.py
```

### 4. Rodar localmente

```bash
uvicorn app.main:app --reload
```

### 5. Testar o webhook

```bash
curl -X POST http://localhost:8000/webhook \
  -H "Content-Type: application/json" \
  -d '{"data": {"key": {"remoteJid": "5511999999999@s.whatsapp.net"}, "message": {"conversation": "oi"}}}'
```

## 🌎 Deploy no Railway

```bash
# Instalar Railway CLI
npm install -g @railway/cli

# Login e deploy
railway login
railway up
```

Configure as variáveis de ambiente no painel do Railway conforme `.env.example`.

## 📄 Variáveis de Ambiente

Veja `.env.example` para a lista completa. Principais:

```env
EVOLUTION_API_URL=       # URL da Evolution API
EVOLUTION_API_KEY=       # Chave da API
EVOLUTION_INSTANCE=      # Nome da instância
SPREADSHEET_ID=          # ID da planilha Google Sheets
GOOGLE_CREDENTIALS_FILE= # Caminho para credentials.json
```

## 📝 Documentação

Guias detalhados de cada fase em `docs/`. Comece por:
- [`docs/fase-8-go-live.md`](docs/fase-8-go-live.md) — Checklist de configurações finais para produção

## 📈 Capacidade

- **MVP (<50 pedidos/dia):** Sessões em memória + Google Sheets direto
- **Escala (100+ pedidos/dia):** Redis + append_rows em lote

## 📅 Atualizado em

Março de 2026 — Fases 0-7 concluídas, Fase 8 (Go Live) em andamento.

## 📄 Licença

MIT License — veja [LICENSE](LICENSE) para detalhes.
