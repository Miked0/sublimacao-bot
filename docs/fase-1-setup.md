# Fase 1 — Setup do Ambiente e Estrutura Base

## Objetivo
Configurar o ambiente de desenvolvimento, criar a estrutura do projeto no GitHub e garantir que a base do codigo esteja pronta para as proximas fases.

## Status: Em Andamento

---

## Tarefas

### Tarefa 1.1 — Estrutura do Repositorio GitHub
- [x] Criar repositorio `sublimacao-bot` no GitHub (publico)
- [x] Adicionar `.gitignore` para Python
- [x] Criar `README.md` com descricao do projeto
- [x] Criar `requirements.txt` com dependencias
- [x] Criar `.env.example` com variaveis de ambiente
- [x] Criar `Dockerfile` para containerizacao
- [x] Criar `railway.toml` para deploy automatico
- [x] Criar `app/main.py` — entrada FastAPI + webhook
- [x] Criar `app/config.py` — configuracoes via pydantic-settings
- [x] Criar `app/bot/session.py` — gerenciamento de estado
- [x] Criar `app/bot/messages.py` — templates de mensagem
- [x] Criar `app/bot/flow.py` — logica do fluxo de pedido
- [x] Criar `app/integrations/__init__.py`
- [x] Criar `app/integrations/evolution.py` — cliente Evolution API
- [x] Criar `app/integrations/sheets.py` — cliente Google Sheets

### Tarefa 1.2 — Ambiente Local
- [ ] Clonar o repositorio na maquina local
- [ ] Criar ambiente virtual Python: `python -m venv venv`
- [ ] Ativar venv: `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows)
- [ ] Instalar dependencias: `pip install -r requirements.txt`
- [ ] Copiar `.env.example` para `.env` e preencher variaveis

### Tarefa 1.3 — Variaveis de Ambiente
Editar o arquivo `.env` com as seguintes informacoes:

```env
EVOLUTION_API_URL=https://sua-evolution-api.com
EVOLUTION_API_KEY=sua_chave_aqui
EVOLUTION_INSTANCE=nome_da_instancia
SPREADSHEET_ID=id_da_planilha_google
GOOGLE_CREDENTIALS_FILE=credentials.json
WEBHOOK_SECRET=segredo_webhook
```

### Tarefa 1.4 — Google Sheets
- [ ] Criar planilha no Google Sheets chamada `Bot Pedidos`
- [ ] Anotar o ID da planilha (da URL)
- [ ] Criar projeto no Google Cloud Console
- [ ] Ativar Google Sheets API e Google Drive API
- [ ] Criar Service Account e baixar `credentials.json`
- [ ] Compartilhar a planilha com o email da Service Account

### Tarefa 1.5 — Teste Local
- [ ] Executar: `uvicorn app.main:app --reload --port 8000`
- [ ] Acessar `http://localhost:8000/health` — deve retornar `{"status": "ok"}`
- [ ] Testar webhook via ngrok ou similar

---

## Estrutura de Arquivos Esperada

```
sublimacao-bot/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── bot/
│   │   ├── __init__.py
│   │   ├── flow.py
│   │   ├── messages.py
│   │   └── session.py
│   └── integrations/
│       ├── __init__.py
│       ├── evolution.py
│       └── sheets.py
├── docs/
│   └── fase-1-setup.md
├── .env.example
├── .gitignore
├── Dockerfile
├── railway.toml
├── README.md
└── requirements.txt
```

---

## Dependencias (requirements.txt)

```
fastapi
uvicorn[standard]
httpx
gspread
google-auth
pydantic-settings
python-dotenv
```

---

## Links Uteis
- [Evolution API Docs](https://doc.evolution-api.com)
- [gspread Docs](https://docs.gspread.org)
- [Railway Deploy](https://railway.app)
- [Google Cloud Console](https://console.cloud.google.com)

---

*Proxima fase: Fase 2 — Logica do Bot e Fluxo de Pedido*
