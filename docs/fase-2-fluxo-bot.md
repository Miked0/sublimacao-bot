# Fase 2 — Fluxo de Conversa do Bot

## Objetivo
Implementar o fluxo completo de conversa do bot: receber mensagem, identificar etapa do pedido, guiar o cliente e registrar o pedido.

## Status: Concluida

---

## Arquivos Implementados

### app/bot/session.py — Session Manager
- Gerencia estado de cada cliente em memoria (dict)
- Funcoes: get_session(), update_session(), clear_session()
- Estado: etapa atual + dados coletados do pedido

### app/bot/messages.py — Templates de Mensagem
- MSG_BOAS_VINDAS: apresentacao do bot
- MSG_SOLICITA_NOME, MSG_SOLICITA_PRODUTO, MSG_SOLICITA_QUANTIDADE
- MSG_SOLICITA_ARTE, MSG_SOLICITA_OBSERVACAO
- MSG_CONFIRMACAO: resumo do pedido para confirmacao
- MSG_PEDIDO_REGISTRADO: confirmacao final com numero do pedido
- MSG_ERRO: mensagem de erro generica

### app/bot/flow.py — Logica do Fluxo (5 etapas)
- Etapa 0: Boas-vindas e solicita nome
- Etapa 1: Recebe nome, solicita produto
- Etapa 2: Recebe produto, solicita quantidade
- Etapa 3: Recebe quantidade, solicita arte
- Etapa 4: Recebe arte/obs, exibe confirmacao
- Etapa 5: Confirma pedido, registra na planilha

## Fluxo de Conversa

```
Cliente digita qualquer coisa
docs: adiciona fase-2-fluxo-bot.md        v
[BOAS-VINDAS] Ola! Bem-vindo a Loja de Sublimacao
        |
        v
[ETAPA 1] Qual o seu nome?
        |
        v
[ETAPA 2] Qual produto deseja? (Caneca, Camisa, Almofada...)
        |
        v
[ETAPA 3] Qual a quantidade?
        |
        v
[ETAPA 4] Voce tem arte pronta? (Sim/Nao)
        |
        v
[CONFIRMACAO] Resumo do pedido - confirma? (Sim/Nao)
        |
        v
[REGISTRO] Pedido #ID registrado na planilha!
```

## Checklist
- [x] Session Manager implementado
- [x] Templates de mensagem criados
- [x] flow.py com 5 etapas implementado
- [x] Fluxo conectado ao webhook
- [x] Testado end-to-end
