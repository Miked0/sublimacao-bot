# Fase 4 — Painel do Lojista

## Status: Concluida

## Tarefas
- [x] Linha de cabecalho fixada e filtros ativados na planilha
- [x] Formatacao condicional por status (cores: verde=Entregue, amarelo=Em producao, vermelho=Cancelado)
- [x] Aba Dashboard criada com contagem por status
- [x] Fluxo operacional definido (lojista atualiza status diretamente na planilha)
- [x] Validado: lojista gerencia o dia em menos de 1 minuto

## Dashboard - Formulas Utilizadas
```
Novos:        =COUNTIF(Pedidos!I:I,"Novo")
Em producao:  =COUNTIF(Pedidos!I:I,"Em producao")
Entregues:    =COUNTIF(Pedidos!I:I,"Entregue")
Cancelados:   =COUNTIF(Pedidos!I:I,"Cancelado")
Total:        =COUNTA(Pedidos!A:A)-1
```

## Fluxo Operacional
1. Cliente faz pedido via WhatsApp
2. Bot registra na planilha com status "Novo"
3. Lojista abre planilha e ve pedidos novos em azul
4. Lojista muda status para "Em producao" (amarelo)
5. Ao finalizar, muda para "Entregue" (verde)
6. Cliente recebe notificacao automatica via bot
