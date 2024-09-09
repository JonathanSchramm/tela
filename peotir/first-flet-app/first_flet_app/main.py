import flet as ft
import os
import socket

# Obter o nome do computador (hostname)
hostname = socket.gethostname()
user = os.getlogin()

def main(page: ft.Page):
    page.title = "Painel automações Auditoria"
    page.window.maximizable = False
    page.window.resizable = False
    page.window.width = 800
    page.window.height = 500
    page.window.center()
    page.window.icon = "F:\\workspace\\projetos_dataBricks\\peotir\\first-flet-app\\first_flet_app\\Ailos.ico"

    def top_header():
        # Texto com o nome do usuário
        t = ft.Text(value=f"Usuário: {user}/{hostname}", color="green")

        # Definindo o tema inicial
        page.theme_mode = ft.ThemeMode.DARK

        # Função para alternar entre o tema claro e escuro
        def switch_theme(e):
            if page.theme_mode == ft.ThemeMode.LIGHT:
                page.theme_mode = ft.ThemeMode.DARK
                theme_toggle.text = "Modo claro"
            else:
                page.theme_mode = ft.ThemeMode.LIGHT
                theme_toggle.text = "Modo escuro"
            page.update()  # Atualiza a página para aplicar o tema novo

        # Botão para alternar o tema
        theme_toggle = ft.ElevatedButton(
            text="Modo claro",
            on_click=switch_theme,
        )

        # Cria um Row para alinhar o nome do usuário à esquerda e o botão de tema à direita
        top_bar = ft.Row(
            controls=[t, ft.Container(content=theme_toggle, alignment=ft.alignment.top_right, expand=True)],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        # Adiciona o layout na página
        page.add(top_bar)

    def card_automacoes():
        # Adiciona uma imagem (altere o caminho para a sua imagem ou use um URL)
        img = ft.Image(
            src="F:\\workspace\\projetos_dataBricks\\peotir\\first-flet-app\\first_flet_app\\ailos_logo.png",  # Substitua pelo caminho da sua imagem
            width=60,
            height=60,
            fit=ft.ImageFit.CONTAIN
        )

        # Função para o clique do botão
        def on_button_click(e):
            page.add(ft.Text("Botão clicado!", color="blue"))

        # Criando o botão
        button = ft.ElevatedButton(
            text="TAC's semanais",
            on_click=on_button_click,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    size=11  # Altere o tamanho do texto conforme desejado
                )
            )
        )

        # Card semanal
        card_semanal = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=img,
                            alignment=ft.alignment.center,
                            expand=True  # Faz com que a imagem ocupe o espaço disponível
                        ),
                        button,
                    ],
                    # alignment=ft.MainAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=10,
                border_radius=10,
                bgcolor="white",
                shadow=ft.BoxShadow(
                    blur_radius=8,
                    spread_radius=2,
                    color="rgba(0, 0, 0, 0.1)"
                ),
            ),
            elevation=4,
            width=150,
            height=170,
        )

        # Card mensal
        card_mensal = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=img,
                            alignment=ft.alignment.center,
                            expand=True  # Faz com que a imagem ocupe o espaço disponível
                        ),
                        button,
                    ],
                    # alignment=ft.MainAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=10,
                border_radius=10,
                bgcolor="white",
                shadow=ft.BoxShadow(
                    blur_radius=8,
                    spread_radius=2,
                    color="rgba(0, 0, 0, 0.1)"
                ),
            ),
            elevation=4,
            width=150,
            height=170,
        )

        # Adiciona os cards lado a lado
        page.add(ft.Row(
            controls=[card_semanal, card_mensal],
            alignment=ft.MainAxisAlignment.START,
            spacing=10  # Espaçamento entre os cards
        ))

    top_header()
    card_automacoes()

# Executa o app Flet
ft.app(target=main)
