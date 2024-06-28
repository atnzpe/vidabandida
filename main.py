import flet as ft
import threading

from oficina_app import OficinaApp, processar_fila_db
from utils import criar_pastas

def main(page: ft.Page):
    """Função principal da aplicação Flet."""

    # Configuração da página
    page.title = "Oficina Guarulhos"  # Título da página
    page.theme_mode = ft.ThemeMode.DARK  # Tema escuro
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Alinhamento centralizado

    # Cria a estrutura de diretórios
    criar_pastas(".")

    # Inicializa a aplicação
    oficina_app = OficinaApp(page)

    # Gerenciamento da thread do banco de dados
    page.pubsub.subscribe(oficina_app._on_message)  # Inscreve-se para receber mensagens da thread
    thread_db = threading.Thread(
        target=processar_fila_db, args=(page,), daemon=True
    )  # Cria a thread
    thread_db.start()  # Inicia a thread

    # Inicialização da interface
    page.update()
    page.add(oficina_app.build())

ft.app(target=main)