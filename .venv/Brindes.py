import flet as ft
import pandas as pd

# App terá 1 página de login + 4 páginas para usuários padrão + N páginas para admins
# Ordem de trabalho em flet: 
# 1º - Criar os parâmetros da janela/página;
# 2º - Criar os elementos; 
# 3º - configurar os conteiners onde serão alocados os elementos;
# 4º - Adicionar os conteiners à página;
# 5º - Adicionar o backend

# 1º - Login
# Definições da janela
def pg_login(page: ft.Page):
    page.title = "SisGB - Login"
    page.window.width = 600
    page.window.height = 430
    page.padding = 0
    page.window.resizable = False
    page.update()
    
# 2º - Elementos;

    usuarios_sistema = {
        'ID': [1, 2, 3, 4, 5],
        'Nome': ['Jorge', 'Renata', 'Kleber', 'Luiz', 'Julia'],
        'Sobrenome': ['Rasta', 'Kaiser', 'Santana', 'Julio', 'Luiza'],
        'Email': ['jorge.rasta@empresa.org', 'renata.kaiser@empresa.org', 'kleber.santana@empresa.org', 'luiz.julio@empresa.org', 'julia.luiza@empresa.org'],
        'Senha': ['a1a1a1', 'b2b2b2', 'c3c3c3', 'd4d4d4', 'e5e5e5']
    }

    df_usuarios = pd.DataFrame(usuarios_sistema)

    adm_sistema = {
        'ID': [1, 2, 3],
        'Nome': ['Raul', 'Jão', 'Jackson'],
        'Sobrenome': ['Gil', 'Jones', 'Five'],
        'Email': ['raul.gil@empresa.org', 'jao.jones@empresa.org', 'jackson.five@empresa.org'],
        'Senha': ['tiro_o_chapeu', 'joao_jonathan', 'Heehee']
    }

    df_adms = pd.DataFrame(adm_sistema)

# Ao entregar, conversar com TI para fazer conexão com banco de dados
    def autenticar_usuario(email, senha):
        if usuarios_sistema in df_usuarios and usuarios_sistema[email] == senha:
            return True
        else:
            return False
        
    def autenticar_adm(email, senha):
        if adm_sistema in df_adms and adm_sistema[email] == senha:
            return True
        else:
            return False

    texto_esquerda = ft.Text(
        "Sistema de Gestão de Brindes",
        size=24,
        weight=ft.FontWeight.W_500,
        no_wrap=False,
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
        content=ft.Text("Entrar", color="#FFFFFF", size=16),
        padding=0,
        width=100,
        bgcolor="#131F6B",
        on_click=autenticar_usuario
        if autenticar_usuario(Email, Senha):
            page.go("/Home")
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Usuário ou senha incorretos"), bgcolor=ft.colors.RED)
            page.snack_bar.open = True
            page.update()
    )

    layout_esquerda = ft.Container(
        width=210,
        height=430,
        bgcolor='#131F6B',
        margin=ft.margin.all(0),
        padding=ft.padding.only(left=45, top=90, bottom=150),
        content=ft.Column(
            controls=[
                texto_esquerda,
                ft.Image(
                    src='https://yt3.googleusercontent.com/pFQHuA7nnTk5298xVLdnOQWWQ2FvzQr0RkwrB9PKA0Z5YOXcn8wq5Qxpw-PRmIEJoxSJuRxt3Q=s900-c-k-c0x00ffffff-no-rj',
                    height=110,
                    width=110,
                    fit=ft.ImageFit.CONTAIN,
                    border_radius=ft.border_radius.all(100),
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