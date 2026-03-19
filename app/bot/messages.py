# Templates de mensagem do bot
# Centralizar aqui facilita manutencao e traducao futura

MSGS = {
    "boas_vindas": (
        "Ola! Bem-vindo a *Loja de Sublimacao*! "
        "Para fazer seu pedido, me diga seu *nome completo*:"
    ),
    "pedir_produto": (
        "Qual produto voce deseja?\n\n{produtos}\n\n"
        "Digite o *numero* do produto:"
    ),
    "pedir_cor": (
        "Qual a *cor principal* ou descricao da arte?\n"
        "(ex: azul royal, foto personalizada, logo da empresa)"
    ),
    "pedir_tamanho": (
        "Qual o tamanho?\n\n{tamanhos}\n\nDigite o *numero*:"
feat: adiciona app/bot/messages.py com templates de mensagem    "pedir_obs": (
        "Alguma *observacao* especial?\n"
        "(ex: prazo urgente, detalhe da arte)\n"
        "Ou digite *nao* para continuar sem observacoes:"
    ),
    "confirmar": (
        "*Resumo do Pedido:*\n\n"
        "Nome: {nome}\n"
        "Produto: {produto}\n"
        "Cor/Arte: {cor}\n"
        "Tamanho: {tamanho}\n"
        "Obs: {obs}\n\n"
        "1 - Confirmar pedido\n"
        "2 - Cancelar\n\n"
        "Digite *1* ou *2*:"
    ),
    "pedido_confirmado": (
        "*Pedido confirmado, {nome}!*\n\n"
        "Numero do pedido: *{pedido_id}*\n"
        "Status: *EM ANALISE*\n\n"
        "Entraremos em contato para combinar arte e pagamento."
    ),
    "pedido_cancelado": (
        "Pedido cancelado. "
        "Digite *oi* quando quiser comecar um novo pedido."
    ),
    "opcao_invalida": "Opcao invalida. Digite o *numero* correspondente.",
    "erro_generico": "Ocorreu um erro. Digite *oi* para recomecar.",
}
