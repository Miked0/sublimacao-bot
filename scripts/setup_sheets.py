#!/usr/bin/env python3
"""
Setup automatico do Google Sheets para o Bot WhatsApp - Loja de Sublimacao.
Execute este script UMA VEZ para configurar a planilha de producao.

Uso:
    python scripts/setup_sheets.py
"""

import os
import sys
from pathlib import Path

# Adiciona o diretorio raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

load_dotenv()

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# Colunas do cabecalho
HEADERS = [
    "ID",
    "Telefone",
    "Nome",
    "Produto",
    "Cor",
    "Tamanho",
    "Observacoes",
    "Status",
    "DataHora",
]

# Configuracoes de formatacao condicional por status
STATUS_COLORS = {
    "Novo": {"backgroundColor": {"red": 0.81, "green": 0.89, "blue": 1.0}},           # Azul claro
    "Em producao": {"backgroundColor": {"red": 1.0, "green": 0.95, "blue": 0.8}},      # Amarelo
    "Pronto": {"backgroundColor": {"red": 0.82, "green": 0.98, "blue": 0.9}},          # Verde claro
    "Entregue": {"backgroundColor": {"red": 0.9, "green": 0.9, "blue": 0.9}},          # Cinza claro
    "Cancelado": {"backgroundColor": {"red": 1.0, "green": 0.89, "blue": 0.89}},       # Vermelho claro
}


def get_client():
    """Autentica com Google Sheets via Service Account."""
    credentials_file = os.getenv("GOOGLE_CREDENTIALS_FILE", "credentials.json")
    
    if not os.path.exists(credentials_file):
        print(f"ERRO: Arquivo de credenciais nao encontrado: {credentials_file}")
        print("Baixe o arquivo credentials.json do Google Cloud Console.")
        sys.exit(1)
    
    creds = Credentials.from_service_account_file(credentials_file, scopes=SCOPES)
    return gspread.authorize(creds)


def setup_header(sheet):
    """Configura o cabecalho da planilha com formatacao."""
    print("Configurando cabecalho...")
    
    # Escreve o cabecalho na linha 1
    sheet.update("A1", [HEADERS])
    
    # Formata o cabecalho (negrito, fundo escuro, texto branco)
    spreadsheet = sheet.spreadsheet
    sheet_id = sheet.id
    
    requests = [
        # Negrito no cabecalho
        {
            "repeatCell": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": 0,
                    "endRowIndex": 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": len(HEADERS),
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": {"red": 0.2, "green": 0.2, "blue": 0.2},
                        "textFormat": {
                            "bold": True,
                            "foregroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0},
                        },
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,textFormat)",
            }
        },
        # Congelar linha de cabecalho
        {
            "updateSheetProperties": {
                "properties": {
                    "sheetId": sheet_id,
                    "gridProperties": {"frozenRowCount": 1},
                },
                "fields": "gridProperties.frozenRowCount",
            }
        },
        # Auto-resize colunas
        {
            "autoResizeDimensions": {
                "dimensions": {
                    "sheetId": sheet_id,
                    "dimension": "COLUMNS",
                    "startIndex": 0,
                    "endIndex": len(HEADERS),
                }
            }
        },
    ]
    
    spreadsheet.batch_update({"requests": requests})
    print("  Cabecalho configurado com sucesso!")


def setup_filters(sheet):
    """Ativa filtros automaticos na planilha."""
    print("Ativando filtros...")
    
    spreadsheet = sheet.spreadsheet
    sheet_id = sheet.id
    
    requests = [
        {
            "setBasicFilter": {
                "filter": {
                    "range": {
                        "sheetId": sheet_id,
                        "startRowIndex": 0,
                        "startColumnIndex": 0,
                        "endColumnIndex": len(HEADERS),
                    }
                }
            }
        }
    ]
    
    spreadsheet.batch_update({"requests": requests})
    print("  Filtros ativados com sucesso!")


def setup_conditional_formatting(sheet):
    """Aplica formatacao condicional por status."""
    print("Configurando formatacao condicional por status...")
    
    spreadsheet = sheet.spreadsheet
    sheet_id = sheet.id
    
    # Indice da coluna Status (H = indice 7)
    status_col_index = HEADERS.index("Status")
    
    requests = []
    for status, format_config in STATUS_COLORS.items():
        requests.append({
            "addConditionalFormatRule": {
                "rule": {
                    "ranges": [
                        {
                            "sheetId": sheet_id,
                            "startRowIndex": 1,
                            "startColumnIndex": 0,
                            "endColumnIndex": len(HEADERS),
                        }
                    ],
                    "booleanRule": {
                        "condition": {
                            "type": "TEXT_EQ",
                            "values": [{"userEnteredValue": status}],
                        },
                        "format": {"backgroundColor": format_config["backgroundColor"]},
                    },
                },
                "index": 0,
            }
        })
    
    spreadsheet.batch_update({"requests": requests})
    print(f"  Formatacao condicional aplicada para {len(STATUS_COLORS)} status!")


def setup_dashboard(spreadsheet):
    """Cria ou atualiza a aba Dashboard com contagens por status."""
    print("Configurando aba Dashboard...")
    
    # Verifica se a aba Dashboard ja existe
    dashboard = None
    for ws in spreadsheet.worksheets():
        if ws.title == "Dashboard":
            dashboard = ws
            break
    
    if not dashboard:
        dashboard = spreadsheet.add_worksheet(title="Dashboard", rows=20, cols=5)
        print("  Aba Dashboard criada!")
    
    # Cabecalho do dashboard
    dashboard.update("A1", [["Status", "Quantidade"]])
    
    # Linhas com formulas COUNTIF
    status_list = list(STATUS_COLORS.keys())
    rows = []
    for i, status in enumerate(status_list, start=2):
        rows.append([status, f'=COUNTIF(Pedidos!H:H,"{status}")')
    
    # Total
    rows.append(["TOTAL", f"=SUM(B2:B{len(status_list)+1})"])
    
    dashboard.update(f"A2", rows)
    
    print("  Dashboard configurado com formulas COUNTIF!")
    print("  Dica: Adicione um grafico de pizza selecionando A1:B6 e inserindo grafico.")


def main():
    spreadsheet_id = os.getenv("SPREADSHEET_ID")
    if not spreadsheet_id:
        print("ERRO: Variavel SPREADSHEET_ID nao configurada no .env")
        sys.exit(1)
    
    print("="*50)
    print("Setup Google Sheets - Bot WhatsApp Sublimacao")
    print("="*50)
    
    print("\nConectando ao Google Sheets...")
    gc = get_client()
    spreadsheet = gc.open_by_key(spreadsheet_id)
    
    # Pega ou cria a aba de pedidos
    try:
        sheet = spreadsheet.worksheet("Pedidos")
        print("  Aba 'Pedidos' encontrada!")
    except gspread.exceptions.WorksheetNotFound:
        sheet = spreadsheet.sheet1
        sheet.update_title("Pedidos")
        print("  Aba principal renomeada para 'Pedidos'!")
    
    print()
    setup_header(sheet)
    setup_filters(sheet)
    setup_conditional_formatting(sheet)
    setup_dashboard(spreadsheet)
    
    print()
    print("="*50)
    print("Setup concluido com sucesso!")
    print(f"Planilha: https://docs.google.com/spreadsheets/d/{spreadsheet_id}")
    print("="*50)


if __name__ == "__main__":
    main()
