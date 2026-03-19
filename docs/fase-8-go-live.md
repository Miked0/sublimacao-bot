# 🚀 Fase 8 – Configurações Finais & Go Live

> **Status:** Próximos passos | Data prevista: Março 2026

## Objetivo

Levar o bot de desenvolvimento para **produção real** com número WhatsApp da loja, planilha de produção e monitoramento ativo.

---

## Checklist de Configurações Finais

### 1. Variáveis de Ambiente no Railway

Configure as seguintes variáveis em **Railway > seu projeto > Variables**:

```env
# WhatsApp / Evolution API
EVOLUTION_API_URL=https://sua-instancia.evolution-api.com
EVOLUTION_API_KEY=sua_api_key_aqui
EVOLUTION_INSTANCE=nome_da_instancia

# Google Sheets
SPREADSHEET_ID=id_da_planilha_de_producao
GOOGLE_CREDENTIALS_JSON={...json_da_service_account...}

# App
WEBHOOK_SECRET=token_secreto_para_validar_webhook
ENVIRONMENT=production
```

### 2. Parear Número WhatsApp Real

1. Acesse o painel da Evolution API em produção
2. Crie uma nova instância com o nome da loja
3. Escaneie o QR Code com o WhatsApp da loja
4. Configure o webhook apontando para: `https://seu-app.railway.app/webhook`
5. Valide com uma mensagem de teste

### 3. Planilha de Produção

1. Crie uma cópia da planilha de desenvolvimento
2. Compartilhe com o e-mail da Service Account (permissão de Editor)
3. Copie o ID da planilha da URL e configure no Railway
4. Execute `python scripts/setup_sheets.py` para configurar cabeçalho e formatação

### 4. Teste de Fluxo Completo em Produção

```bash
# Roteiro de teste (5 minutos)
1. Envie "oi" para o número da loja via WhatsApp
2. Percorra todas as 5 etapas do pedido
3. Confirme que o pedido apareceu na planilha
4. Mude o status para "Pronto" na planilha
5. Confirme que o cliente recebeu a notificação
```

### 5. Monitoramento (Railway)

- Ative **Health Check** em: `https://seu-app.railway.app/health`
- Configure alertas de downtime no Railway
- Monitore logs em tempo real: `railway logs --tail`

### 6. Segurança

- [ ] Adicione `WEBHOOK_SECRET` para validar requisições da Evolution API
- [ ] Ative branch protection no GitHub (`main` requer PR)
- [ ] Nunca commite credentials reais no repositório
- [ ] Use `.env.example` como referência (nunca o `.env` real)

### 7. Backup

```bash
# Proteger branch main
git checkout -b develop
git push origin develop

# Tag de versão MVP
git tag -a v1.0.0 -m "MVP: Bot WhatsApp Loja de Sublimação - Go Live"
git push origin v1.0.0
```

### 8. Treinamento do Lojista

Demonstrar ao vivo:
1. Como ver pedidos novos na planilha
2. Como filtrar por status
3. Como mudar status e o cliente ser notificado
4. Como ver o Dashboard com totais do dia
5. O que fazer se o bot parar de responder

### 9. Scripts úteis

```bash
# Ver logs em tempo real
railway logs --tail

# Reiniciar serviço
railway up

# Testar webhook localmente
curl -X POST http://localhost:8000/webhook \
  -H "Content-Type: application/json" \
  -d '{"data": {"key": {"remoteJid": "5511999999999@s.whatsapp.net"}, "message": {"conversation": "oi"}}}'

# Testar health
curl https://seu-app.railway.app/health
```

---

## Cronograma Go Live

| Etapa | Estimativa | Responsável |
|-------|-----------|-------------|
| Configurar variáveis Railway | 30 min | Dev |
| Parear número WhatsApp | 15 min | Dev + Lojista |
| Setup planilha produção | 20 min | Dev |
| Teste fluxo completo | 30 min | Dev + Lojista |
| Treinamento lojista | 1h | Dev |
| **Total** | **~2h30** | |

---

## Contato de Emergência

Se o bot parar de funcionar:
1. Verificar Railway: logs e status do serviço
2. Verificar Evolution API: QR Code ainda válido?
3. Verificar Google Sheets: credenciais ainda ativas?
4. Reiniciar serviço no Railway

---

*Fase 8 concluída = Bot em produção real. 🎉*
