# 🤖 sublimacao-bot

> Bot de pedidos via WhatsApp com FastAPI + Google Sheets para loja de sublimação

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

---

## 📌 Sobre o Projeto

Automação completa de pedidos para loja de sublimação via WhatsApp.
O cliente conversa com um bot guiado, confirma o pedido e tudo é registrado automaticamente no Google Sheets.

## 🛠️ Stack

| Componente | Tecnologia |
|---|---|
| Gateway WhatsApp | Evolution API |
| Backend | Python + FastAPI |
| Planilha | Google Sheets (gspread) |
| Hospedagem | Railway / Render |
| Sessões | Dict em memória (MVP) / Redis (escala) |

## 📂 Estrutura do Projeto

```
sublimacao-bot/
├── app/
│   ├── main.py              # FastAPI + webhook endpoint
│   ├── config.py            # Variaveis de ambiente
│   ├── bot/
│   │   ├── session.py       # Gerenciamento de estado
│   │   ├── flow.py          # Logica do fluxo de pedido
│   │   └── messages.py      # Templates de mensagem
│   └── integrations/
│       ├── evolution.py     # Cliente Evolution API
│       └── sheets.py        # Cliente Google Sheets
├── docs/
│   ├── arquitetura.png
│   ├── fase-0-direcao-projeto.md
│   ├── fase-1-conexao-whatsapp-backend.md
│   ├── fase-2-fluxo-conversa.md
│   ├── fase-3-integracao-google-sheets.md
│   ├── fase-4-painel-lojista.md
│   ├── fase-5-notificacao-status-cliente.md
│   ├── fase-6-escala-100-pedidos-dia.md
│   └── fase-7-storytelling-documentacao.md
├── requirements.txt
├── Dockerfile
├── .env.example
└── railway.toml
```

## 🚀 Fluxo do Sistema

```
Cliente (WhatsApp)
       ↓ mensagem
[Evolution API] --webhook--> [FastAPI + Python]
                                     ↓
                        [Session Manager]
                                     ↓
                         [Google Sheets API]
                                     ↓
                        [Notificacao ao cliente]
```

## ⚙️ Configuracao

1. Clone o repositorio:
```bash
git clone https://github.com/Miked0/sublimacao-bot.git
cd sublimacao-bot
```

2. Instale as dependencias:
```bash
pip install -r requirements.txt
```

3. Configure as variaveis de ambiente:
```bash
cp .env.example .env
# Edite o .env com suas credenciais
```

4. Rode localmente:
```bash
uvicorn app.main:app --reload
```

## 🗒️ Fases do Projeto

| Fase | Descricao | Status |
|---|---|---|
| 0 | Direcao do Projeto | ✅ Concluida |
| 1 | Conectar WhatsApp ao Backend | 🟡 Em andamento |
| 2 | Fluxo de Conversa do Bot | ⏳ Pendente |
| 3 | Integracao Google Sheets | ⏳ Pendente |
| 4 | Painel do Lojista | ⏳ Pendente |
| 5 | Notificacao de Status | ⏳ Pendente |
| 6 | Escala 100+ Pedidos/Dia | ⏳ Pendente |
| 7 | Storytelling e Documentacao | ⏳ Continuo |

## 📝 Licenca

MIT License - veja [LICENSE](LICENSE) para detalhes.

---

> Projeto documentado publicamente como parte de uma jornada de desenvolvimento. Acompanhe a evolucao no Instagram via Close Friends.
