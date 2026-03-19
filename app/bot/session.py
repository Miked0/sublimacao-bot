from typing import Dict

# Gerenciamento de sessao em memoria (suficiente para < 50 pedidos/dia)
# Para escala: migrar para Redis (Fase 6)
sessions: Dict[str, dict] = {}

ETAPAS = ["nome", "produto", "cor", "tamanho", "obs", "confirmar"]


def get_session(telefone: str) -> dict:
    """Retorna sessao existente ou cria uma nova."""
    if telefone not in sessions:
        sessions[telefone] = {
            "etapa": 0,
            "dados": {"telefone": telefone}
        }
    return sessions[telefone]


def salvar_session(telefone: str, session: dict):
    """Salva sessao atualizada."""
    sessions[telefone] = session


def limpar_session(telefone: str):
    """Remove sessao ao fim do pedido ou em reset."""
    sessions.pop(telefone, None)
