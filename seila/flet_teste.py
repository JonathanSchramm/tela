import flet as ft

def main(page: ft.Page):
    page.title = "Painel automações"
    page.window.maximizable = False
    page.window.resizable = False
    page.window.width = 800
    page.window.height = 500
    page.window.center()

    

ft.app(main)
