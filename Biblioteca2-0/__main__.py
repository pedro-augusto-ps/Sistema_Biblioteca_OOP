from Classes_Biblioteca_02 import *
from Funcoes_Biblioteca_02 import *
from rich import print, inspect

biblioteca_recebida = Biblioteca()

while True:
    menu_principal()
    escolha = int(input("Insira sua ação: "))
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
        