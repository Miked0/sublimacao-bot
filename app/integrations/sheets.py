import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from app.config import settings

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


class SheetsClient:
    """Cliente Google Sheets via gspread para registrar pedidos."""

    def __init__(self):
        self._client = None
        self._sheet = None

    def _get_client(self):
        if self._client is None:
            creds = Credentials.from_service_account_file(
                settings.GOOGLE_CREDENTIALS_FILE, scopes=SCOPES
            )
            self._client = gspread.authorize(creds)
        return self._client

    def _get_sheet(self):
        if self._sheet is None:
            gc = self._get_client()
            spreadsheet = gc.open_by_key(settings.SPREADSHEET_ID)
            try:
                self._sheet = spreadsheet.worksheet("Pedidos")
            except gspread.WorksheetNotFound:
                self._sheet = spreadsheet.add_worksheet(title="Pedidos", rows=1000, cols=10)
                self._sheet.append_row([
                    "ID", "Data", "Telefone", "Nome", "Produto",
                    "Quantidade", "Arte", "Observacao", "Status"
                ])
        return self._sheet

    def registrar_pedido(self, pedido: dict) -> int:
        """Registra um novo pedido e retorna o numero sequencial."""
        sheet = self._get_sheet()
        all_rows = sheet.get_all_values()
        # Ignora header, conta linhas de dados
        order_id = len(all_rows)  # ID = total de linhas (header + dados anteriores)
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        row = [
            order_id,
            now,
            pedido.get("telefone", ""),
            pedido.get("nome", ""),
            pedido.get("produto", ""),
            pedido.get("quantidade", ""),
            pedido.get("arte", "Nao informado"),
            pedido.get("observacao", ""),
            "Novo",
        ]
        sheet.append_row(row)
        return order_id

    def buscar_pedido(self, order_id: int) -> dict | None:
        """Busca pedido por ID."""
        sheet = self._get_sheet()
        records = sheet.get_all_records()
        for r in records:
            if str(r.get("ID")) == str(order_id):
                return r
        return None

    def atualizar_status(self, order_id: int, status: str) -> bool:
        """Atualiza o status de um pedido pelo ID."""
        sheet = self._get_sheet()
        cell = sheet.find(str(order_id))
        if cell:
            sheet.update_cell(cell.row, 9, status)  # coluna 9 = Status
            return True
        return False


sheets = SheetsClient()
