from Classes_Biblioteca_02 import *
from rich import inspect
from datetime import datetime
import time
from Visual import *
from getpass import getpass

def escolha1_cadastrar_item(biblioteca_recebida):
    itens_disponiveis()     #Exibe os ITENS disponíveis
    escolha = int(input("Insira o [#F9DC5C bold]ITEM[/] a ser cadastrado: "))
    if escolha == 1:
        titulo = str(input("Insira o TÍTULO: "))
        autor = str(input("Insira o AUTOR: "))
        disponibilidade = True
        biblioteca_recebida.cadastrar_livro(titulo, autor, disponibilidade) #Cria um livro
    elif escolha == 2:
        titulo = str(input("Insira o NOME da REVISTA: "))
        autor = str(input("Insira o AUTOR: "))
        disponibilidade = True
        biblioteca_recebida.cadastrar_revista(titulo, autor, disponibilidade) #Cria uma revista
    else:
        opcao_invalida()

def escolha2_cadastrar_usuario(biblioteca_recebida):
    nome = str(input("Insira o NOME do USUÁRIO: "))
    if nome in biblioteca_recebida.usuarios:  #Se o nome já está na lista da biblioteca
        usuario_cadastrado()
    insira_senha() 
    senha = getpass("")
    usuario = Usuario(nome, senha)  #Cria um usuário
    biblioteca_recebida.cadastrar_usuario(usuario)  #Cadastra ele na biblioteca

def escolha3_exibir_informações(biblioteca_recebida):
    procurado = str(input("Insira o NOME do USUÁRIO PROCURADO: "))
    usuario = biblioteca_recebida.usuarios.get(procurado)   #Acha o usuário na lista da biblioteca
    if procurado == usuario.nome:
        insira_senha()        
        senha = getpass("")
        if usuario.verificar_senha(senha) == True:  #Verifica a senha do usuário
            exibir_informacoes(usuario)     #Exibe as informaçoes do usuário
        else:
            senha_invalida()
    else:
        usuario_nao_encontrado() 

def escolha4_exibir_acervo(bibilioteca_recebida):
    exibir_acervo_estilizado(bibilioteca_recebida)

def escolha5_retirar(biblioteca_recebida):
    exibir_acervo_estilizado(biblioteca_recebida)
    usuario = str(input("Qual USUÁRIO deseja RETIRAR: "))
    if usuario in biblioteca_recebida.usuarios.keys():  #Confirma se o usuário(STR) está na lista da biblioteca
        item = str(input("Qual ITEM deseja RETIRAR: "))
        biblioteca_recebida.retirar(usuario, item)
    else:
        usuario_nao_encontrado()

def escolha6_devolver(biblioteca_recebida):
    usuario_fornecido = str(input("Qual USUÁRIO deseja DEVOLVER: "))
    if usuario_fornecido in biblioteca_recebida.usuarios.keys():
        usuario_objeto = biblioteca_recebida.usuarios.get(usuario_fornecido)
        print(f"ITENS RETIRADOS: ")
        for item in usuario_objeto._itens_emprestados:
            print(item)
        item_fornecido = str(input("Qual ITEM deseja DEVOLVER: "))
        biblioteca_recebida.devolver(usuario_fornecido, item_fornecido)
        

