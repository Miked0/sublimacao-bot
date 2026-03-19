from app.bot.session import get_session, salvar_session, limpar_session
from app.bot.messages import MSGS

PRODUTOS = ["Camiseta", "Caneca", "Almofada", "Quadro", "Squeeze"]
TAMANHOS = {
    "Camiseta": ["P", "M", "G", "GG"],
    "Caneca": ["325ml"],
    "Almofada": ["40x40"],
    "Quadro": ["20x30", "30x40"],
    "Squeeze": ["500ml"],
}
PALAVRAS_RESET = ["oi", "ola", "menu", "reiniciar", "inicio", "0"]


async def processar_mensagem(telefone: str, texto: str) -> str:
    """Processa mensagem recebida e retorna resposta do bot."""
    texto = texto.strip()
    session = get_session(telefone)
    etapa = session["etapa"]
    dados = session["dados"]

    # Permitir reset a qualquer momento
    if texto.lower() in PALAVRAS_RESET:
        limpar_session(telefone)
        return MSGS["boas_vindas"]

    try:
        if etapa == 0:  # Coletar nome
            dados["nome"] = texto
            session["etapa"] = 1
            salvar_session(telefone, session)
            produtos_str = "\n".join(
                [f"{i+1}. {p}" for i, p in enumerate(PRODUTOS)]
            )
            return MSGS["pedir_produto"].format(produtos=produtos_str)

        elif etapa == 1:  # Coletar produto
            idx = int(texto) - 1
            if idx < 0 or idx >= len(PRODUTOS):
                raise IndexError
            dados["produto"] = PRODUTOS[idx]
            session["etapa"] = 2
            salvar_session(telefone, session)
            return MSGS["pedir_cor"]

        elif etapa == 2:  # Coletar cor
            dados["cor"] = texto
            session["etapa"] = 3
            salvar_session(telefone, session)
            tamanhos = TAMANHOS.get(dados["produto"], ["Unico"])
            tamanhos_str = "\n".join(
                [f"{i+1}. {t}" for i, t in enumerate(tamanhos)]
            )
            return MSGS["pedir_tamanho"].format(tamanhos=tamanhos_str)

        elif etapa == 3:  # Coletar tamanho
            tamanhos = TAMANHOS.get(dados["produto"], ["Unico"])
            idx = int(texto) - 1
            if idx < 0 or idx >= len(tamanhos):
                raise IndexError
            dados["tamanho"] = tamanhos[idx]
            session["etapa"] = 4
            salvar_session(telefone, session)
            return MSGS["pedir_obs"]

        elif etapa == 4:  # Coletar observacoes
            dados["obs"] = "" if texto.lower() == "nao" else texto
            session["etapa"] = 5
            salvar_session(telefone, session)
            return MSGS["confirmar"].format(**dados)

        elif etapa == 5:  # Confirmacao final
            if texto == "1":
                # Importar aqui para evitar circular import
                from app.integrations.sheets import registrar_pedido
                pedido_id = registrar_pedido(dados)
                limpar_session(telefone)
                return MSGS["pedido_confirmado"].format(
                    nome=dados["nome"], pedido_id=pedido_id
                )
            elif texto == "2":
                limpar_session(telefone)
                return MSGS["pedido_cancelado"]
            else:
                return "Digite *1* para confirmar ou *2* para cancelar."

    except (ValueError, IndexError):
        return MSGS["opcao_invalida"]
    except Exception:
        return MSGS["erro_generico"]

    return MSGS["boas_vindas"]
