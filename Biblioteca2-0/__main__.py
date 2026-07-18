from Classes_Biblioteca_02 import *
from Funcoes_Biblioteca_02 import *
from rich import print, inspect
import time
import os

pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_item = os.path.join(pasta_atual, "itens.json")
caminho_user = os.path.join(pasta_atual, "usuarios.json")
biblioteca_recebida = Biblioteca()
biblioteca_recebida.carregar_itens(caminho_item)
biblioteca_recebida.carregar_usuarios(caminho_user)

menu_principal()
while True:
    try:
        print("[white bold]Insira sua ação: [7] = MOSTRAR MENU[/]")
        escolha = int(input(""))
        if escolha == 1:
            escolha1_cadastrar_item(biblioteca_recebida)
        elif escolha == 2:
            escolha2_cadastrar_usuario(biblioteca_recebida)
        elif escolha == 3:
            escolha3_exibir_informações(biblioteca_recebida)
        elif escolha == 4:
            exibir_acervo_estilizado(biblioteca_recebida)
        elif escolha == 5:
            escolha5_retirar(biblioteca_recebida)
        elif escolha == 6:
            escolha6_devolver(biblioteca_recebida)
        elif escolha == 7:
            menu_principal()
        else:
            invalido()
    except:
        invalido()

        