import flet as ft
import pandas as pd

# App terá 1 página de login + 4 páginas para usuários padrão + N páginas para admins
# Ordem de trabalho em flet: 
# 1º - Criar os parâmetros da janela/página;
# 2º - Criar os elementos; 
# 3º - configurar os conteiners onde serão alocados os elementos;
# 4º - Adicionar os conteiners à página.

# 1º - Login
# Definições da janela
def pg_login(page: ft.Page):
    page.title = "SisGB - Login"
    page.window.width = 600
    page.window.height = 430
    page.window.resizable = False
    page.update()
    
# 2º - Elementos; 
    texto_esquerda1 = ft.Text(
        "Sistema de",
        size=24,
        weight=ft.FontWeight.W_500,    
    )

    texto_esquerda2 = ft.Text(
        "Gestão de",
        size=24,
        weight=ft.FontWeight.W_500,    
    )
    
    texto_esquerda3 = ft.Text(
        "Brindes",
        size=24,
        weight=ft.FontWeight.W_500,    
    )

    campo_usuario = ft.TextField(
        label="Nome de usuário",
        color="#1E1E1E",
        value="",
        width=250,
        height=40,        
    )

    campo_senha = ft.TextField(
        value="",
        width=250,
        height=40,
        label="Senha", 
        color="#1E1E1E",
        password=True, 
        can_reveal_password=True, 
    )

    botao_login = ft.CupertinoButton(
        content=ft.Text("Entrar", color="#1E1E1E"),
        width=170,
        bgcolor="#D9D9D9",
    )

    layout_esquerda = ft.Container(
        width=210,
        height=430,
        bgcolor='#131F6B',
        margin=ft.margin.all(0),
        padding=ft.padding.only(left=45, top=70),
        content=ft.Column(
            controls=[
                texto_esquerda1,
                texto_esquerda2,
                texto_esquerda3,
                ft.Image(
                    src='https://yt3.googleusercontent.com/pFQHuA7nnTk5298xVLdnOQWWQ2FvzQr0RkwrB9PKA0Z5YOXcn8wq5Qxpw-PRmIEJoxSJuRxt3Q=s900-c-k-c0x00ffffff-no-rj',
                    height=120,
                    width=120,
                    fit=ft.ImageFit.CONTAIN,
                )
            ],
            spacing=10
        )
    )

    layout_direita = ft.Container(
        width=400,
        height=430,
        bgcolor='#FFFFFF',
        margin=ft.margin.all(0),
        padding=ft.padding.only(left=45, top=150),
        content=ft.Column(
            controls=[
                campo_usuario,
                campo_senha,
                botao_login
            ],
            spacing=10
        )
    )

    # 3º - Conteiners (esquerda e direita)
    layout = ft.Container(
        content=ft.Row(
            controls=[
                layout_esquerda,
                layout_direita
            ],
            spacing=0
        )
    )

    # 4º - Adicionar o layout completo à página
    page.add(layout)

# Executa o app
ft.app(target=pg_login)