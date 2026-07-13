from Classes_Biblioteca_02 import *
from rich import inspect
from datetime import datetime
import time

def menu_principal():
    print(f"[1] Cadastrar ITEM")
    print(f"[2] Cadastrar USUÁRIO")
    print(f"[3] Exibir INFORMAÇÕES USUÁRIO")
    print(f"[4] RETIRAR")
    print(f"[5] DEVOLVER")

def escolha1_cadastrar_item(biblioteca_recebida):
    print(f"Itens possíveis de cadastrar: ")
    print(f"[1] LIVRO")
    print(f"[2] REVISTA")
    escolha = int(input("Insira o item a ser cadastrado: "))
    if escolha == 1:
        titulo = str(input("Insira o TÍTULO: "))
        autor = str(input("Insira o AUTOR: "))
        disponibilidade = True
        biblioteca_recebida.cadastrar_livro(titulo, autor, disponibilidade)
    elif escolha == 2:
        titulo = str(input("Insira o NOME da REVISTA: "))
        autor = str(input("Insira o AUTOR: "))
        disponibilidade = True
        biblioteca_recebida.cadastrar_revista(titulo, autor, disponibilidade)
    else:
        print("Opção INVÁLIDA")

def escolha2_cadastrar_usuario(biblioteca_recebida):
    nome_usuario = str(input("Insira o NOME do USUÁRIO: "))
    if nome_usuario in biblioteca_recebida.usuarios:
        print("USUÁRIO já CADASTRADO")
        return 
    senha_usuario = str(input("Crie sua SENHA: "))
    novo_usuario = Usuario(nome_usuario, senha_usuario)
    biblioteca_recebida.cadastrar_usuario(novo_usuario)

def escolha3_exibir_informações(biblioteca_recebida):
    usario_procurado = str(input("Insira o NOME do USUÁRIO PROCURADO: "))
    for i in range(3):
        print(".", end='')
        time.sleep(1)
    print('')
    procurado = biblioteca_recebida.usuarios.get(usario_procurado)
    if usario_procurado == procurado.nome:
        senha_acessar = str(input("Insira a SENHA para exibir as INFORMAÇÕES: "))
        if procurado.verificar_senha(senha_acessar) == True:
            print(f"EXIBINDO INFORMAÇÕES DE(A):")
            print(f"NOME: {procurado.nome}")
            print(f"EMPRÉSTIMOS ATUAIS: {procurado._emprestimos_realizados}")
        else:
            print("ACESSO NEGADO")
    else:
        print("USUÁRIO NÃO ENCONTRADO")

def escolha4_retirar(biblioteca_recebida):
    exibir_acervo(biblioteca_recebida)
    usuario_fornecido = str(input("Qual USUÁRIO deseja RETIRAR: "))
    if usuario_fornecido in biblioteca_recebida.usuarios.keys():
        item_fornecido = str(input("Qual ITEM deseja RETIRAR: "))
        biblioteca_recebida.retirar(usuario_fornecido, item_fornecido)
    else:
        print("USUÁRIO não consta no SISTEMA")

def exibir_acervo(biblioteca_recebida):
    for item in biblioteca_recebida.item:
        print(item)