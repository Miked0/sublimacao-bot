# 🤖 sublimacao-bot

> Bot de pedidos via WhatsApp com FastAPI + Google Sheets para loja de sublimação

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Configura%C3%A7%C3%B5es%20Finais-orange.svg)](#)

---

## 📖 A História por trás desse projeto

> *"Não fiz isso porque era fácil. Fiz porque a loja precisava, e eu sabia que dá pra resolver com código."*

### O problema real

Uma loja de sublimação em plena operação. Pedidos chegando pelo WhatsApp o dia todo.
A lojista respondendo mensagem por mensagem, anotando num caderno, esquecendo cor, esquecendo tamanho, perdendo pedido no meio de 200 mensagens.

O caos era o processo.

Cada pedido dependia 100% de atenção humana para não se perder. Não havia padrão. Não havia registro. Não havia controle.

### A decisão

Em vez de reclamar do problema, decidi resolver.

Não com uma plataforma cara. Não com um SaaS de R$500/mês. Com código.

Com uma stack enxuta, open source e que roda com menos de R$20/mês em infraestrutura:
- **Evolution API** para conectar o WhatsApp sem precisar de aprovação do Meta
- **FastAPI** para um backend leve e rápido em Python
- **Google Sheets** como banco de dados visual que a lojista já sabe usar
- **Railway** para deploy em minutos, sem servidor para gerenciar

### A jornada — fase por fase

Esse projeto foi construído de forma **completamente pública**, fase por fase, documentando cada etapa:

```
Fase 0 → Direcionamento e escopo do MVP
Fase 1 → WhatsApp conectado ao backend. Primeira mensagem recebida.
Fase 2 → Bot guiando o cliente: nome, produto, cor, tamanho, confirmação.
Fase 3 → Pedido registrado automaticamente no Google Sheets.
Fase 4 → Painel visual para a lojista: cores por status, dashboard, filtros.
Fase 5 → Cliente notificado automaticamente quando o pedido fica pronto.
Fase 6 → Arquitetura preparada para 100+ pedidos/dia com Redis.
Fase 7 → Documentação completa. História contada.
Fase 8 → Go Live. Bot em produção real. 🚀
```

Cada fase virou um Story no Instagram. Cada commit virou prova pública de que estava sendo feito de verdade.

### O resultado

Um sistema que:
- Recebe pedidos 24h por dia, mesmo quando a loja está fechada
- Elimina erros de anotação manual
- Registra tudo automaticamente na planilha
- Notifica o cliente quando o pedido está pronto
- Permite à lojista gerenciar o dia inteiro em menos de 1 minuto

Tudo isso com menos de 500 linhas de código Python.

### Por que esse projeto importa

Porque não é só um bot.

É a prova de que pequenas lojas podem ter automações de nível profissional sem pagar fortune.
É a prova de que um desenvolvedor pode resolver problemas reais de negócio, não só criar projetos acadêmicos.
É a prova de que construir em público, fase por fase, é a forma mais honesta de mostrar o que você é capaz.

---

## 🚀 Sobre o Projeto

Automação completa de pedidos para loja de sublimação via WhatsApp. O cliente conversa com um bot guiado, confirma o pedido e tudo é registrado automaticamente no Google Sheets com painel visual para o lojista.

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
│   └── setup_sheets.py      # Setup automático da planilha de produção
├── docs/
│   ├── fase-1-setup.md
│   ├── fase-2-fluxo-bot.md
│   ├── fase-3-google-sheets.md
│   ├── fase-4-painel-lojista.md
│   ├── fase-5-notificacao-status.md
│   ├── fase-6-escala-100-pedidos.md
│   ├── fase-7-storytelling.md
│   └── fase-8-go-live.md    # ⭐ PRÓXIMA ETAPA
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
npm install -g @railway/cli
railway login
railway up
```

Configure as variáveis de ambiente no painel do Railway conforme `.env.example`.

## 📄 Variáveis de Ambiente

```env
EVOLUTION_API_URL=       # URL da Evolution API
EVOLUTION_API_KEY=       # Chave da API
EVOLUTION_INSTANCE=      # Nome da instância
SPREADSHEET_ID=          # ID da planilha Google Sheets
GOOGLE_CREDENTIALS_FILE= # Caminho para credentials.json
```

## 📝 Documentação

Guias detalhados de cada fase em `docs/`. Para ir direto ao ponto:
- [`docs/fase-8-go-live.md`](docs/fase-8-go-live.md) — Checklist de configurações finais para produção

## 📈 Capacidade

- **MVP (<50 pedidos/dia):** Sessões em memória + Google Sheets direto
- **Escala (100+ pedidos/dia):** Redis + append_rows em lote

## 📅 Atualizado em

Março de 2026 — Fases 0–7 concluídas. Fase 8 (Go Live) em andamento.

## 📄 Licença

MIT License — veja [LICENSE](LICENSE) para detalhes.

---

> *Construído em público. Commit por commit. Fase por fase.*
> *Porque a melhor forma de provar que você sabe fazer é mostrando enquanto faz.*
