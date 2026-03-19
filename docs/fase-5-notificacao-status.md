# Fase 5 — Notificacao de Status para o Cliente

## Status: Concluida

## Estrategia Adotada
Job no backend (APScheduler) rodando a cada 60 segundos detectando mudancas de status na planilha e enviando mensagem via Evolution API.

## Tarefas
- [x] Estrategia de notificacao definida: job no backend
- [x] Templates de mensagem criados para cada status
- [x] Mecanismo de deteccao de mudanca de status implementado (coluna StatusNotificado)
- [x] Envio de mensagem via Evolution API conectado
- [x] Ciclo completo testado: mudar status na planilha -> cliente recebe mensagem

## Templates de Notificacao

| Status | Mensagem Enviada |
|--------|------------------|
| Em producao | Ola {nome}! Seu pedido #{id} entrou em producao. |
| Pronto para retirada | Ola {nome}! Pedido #{id} pronto! Pode retirar. |
| Entregue | Obrigado {nome}! Pedido #{id} entregue com sucesso! |
| Cancelado | {nome}, seu pedido #{id} foi cancelado. Entre em contato. |

## Arquivo Implementado
- `app/jobs/notificador.py` - Job de monitoramento com APScheduler
- Roda a cada 60 segundos
- Verifica coluna 'StatusNotificado' na planilha
- Envia mensagem se status mudou e ainda nao notificou
- Atualiza 'StatusNotificado' para evitar duplo envio
