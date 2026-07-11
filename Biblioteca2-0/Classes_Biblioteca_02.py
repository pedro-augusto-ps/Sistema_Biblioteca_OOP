from abc import ABC, abstractmethod
import hashlib
from rich import print,inspect

class Item(ABC):
    """Clase ITEM, abstrata e serve para criação das SUBCLASSES livro e Revista
    Possuí um método abstrato para ser implatado em ambas.
    """
    def __init__(self, titulo, autor, disponibilidade): #Todo item deve ter: Titulo, Autor, e uma disponibilidade(Bool)
        self.titulo = titulo
        self.autor = autor
        self.disponibilidade = disponibilidade

    @abstractmethod         #Método abstrato para forçar a criaçao nas subclasses
    def calcular_multa(self, dias_de_atraso):
        pass

class Livro(Item): 
    """Livro SUBCLASSE de item, com essa classe criamos um item para nossa biblioteca"""
    def __init__(self, titulo, autor, disponibilidade):
        super().__init__(titulo, autor, disponibilidade)

    def calcular_multa(self, dias_de_atraso):
        return dias_de_atraso * 1

class Revista(Item):
    """Revista SUBCLASSE de item, com essa classe criamos um item para nossa biblioteca"""
    def __init__(self, titulo, autor, disponibilidade):
        super().__init__(titulo, autor, disponibilidade)

    def calcular_multa(self, dias_de_atraso):
        return dias_de_atraso * 0.50

class Emprestimo:
    """Nesta CLASSE, os atributos: (usuario_fornecido) e (item_fornecido) seram CLASSES!
    (usuario_fornecido)será utilizado para verificar a quantia de emprestimos que esse usuario já tem
    (item_fornecido)é usado para ver se o item está True, ou False"""
    def __init__(self, usuario_fornecido, item_fornecido, data_do_emprestimo, dias_de_atraso):
        self.usuario_do_emprestimo = usuario_fornecido  #O usuario fornecido será o usuario PASSADO no MÉTODO RETIRAR da CLASSE BIBLIOTECA
        self.item_do_emprestimo = item_fornecido        #O Item fornecido será um OBJETO, um livro ou uma revista
        self.data_do_emprestimo = data_do_emprestimo
        self.dias_de_atraso = dias_de_atraso

    def finalizar(self):
        self.item_do_emprestimo.disponibilidade = True      #O item fornecido passado como PARAMETRO no MÉTODO RETIRAR, da CLASSE BIBLIOTECA está disponivel
        self.usuario_do_emprestimo._emprestimos_realizados -= 1  #O Usuario passado, e seus emprestimos -1

class Usuario:
    def __init__(self, nome, senha_usuario):
        self._nome = nome
        self.__senha_usuario = hashlib.sha256(senha_usuario.encode('utf-8')).hexdigest()  #Senha trasnformada em HASH de cara
        self._emprestimos_realizados = 0

    @property
    def checagem_nome(self):
        return self._nome

    @checagem_nome.setter
    def checagem_nome(self, novo_nome):
        if novo_nome == self._nome:
           raise ValueError("O novo nome não pode ser igual o antigo")
        else:
            self._nome = novo_nome

    @property
    def checagem_senha(self):
        return self.__senha_usuario

    @checagem_senha.setter
    def checagem_senha(self, nova_senha):
        teste_veracidade = str(input("Insira a sua senha para confirmar autenticidade: "))
        if hashlib.sha256(teste_veracidade.encode('utf-8')).hexdigest() != self.__senha_usuario:
            return "Senha não compátivel para troca"
        else:
            nova_senha = str(input("Insira a nova senha: "))
            self.__senha_usuario = hashlib.sha256(nova_senha.encode('utf-8')).hexdigest()
         
class Biblioteca:
    def __init__(self):
        self.usario = []
        self.item = []
        self.emprestimos_lista = []

    def retirar(self, usuario_fornecido, item_fornecido): #(usuario_fornecido = objeto usuario)(item_forncido = objeto item)
        senha = str(input("Insira a senha: "))
        if hashlib.sha256(senha.encode('utf-8')).hexdigest() != usuario_fornecido.checagem_senha:
            print("Senha errada")
        else:
            if item_fornecido.disponibilidade == True:              #Se a disponibilidade daquele objeto é True
                if usuario_fornecido._emprestimos_realizados < 3:   #Se aquele "objeto"usuario tem menos de 3 emprestimos
                    item_fornecido.disponibilidade = False          #A disponibilidade daquele objeto sera False
                    usuario_fornecido._emprestimos_realizados += 1  #Soma um emprestimo naquele "objeto" usuário
                    novo_emprestimo = Emprestimo(usuario_fornecido, item_fornecido, "11 de Julho", 0)  #Cria um Emprestimo, para o "objeto"usuario 
                    self.emprestimos_lista.append(novo_emprestimo)  #Adiciona esse empréstimo na lista da biblioteca
                    return novo_emprestimo
            
    def devolver(self, emprestimo):
        if emprestimo in self.emprestimos_lista: #se o meu ITEM emprestado está na lista com os items já emprestados, removo o item da lista
            self.emprestimos_lista.remove(emprestimo)
        emprestimo.finalizar()                  #Finalizo meu emprestimo, chamando a funcao do emprestimo.finalizar()


l1 = Livro("Clarissa", "Machado de Assis", True)
inspect(l1, private=True, methods=True)

user0000000001 = Usuario("Maurice", "lemure")
inspect(user0000000001, private=True, methods=True)

bibliotecalocal = Biblioteca()
inspect(bibliotecalocal, private=True, methods=True)

bibliotecalocal.retirar(user0000000001, l1)
emprestimo1 = Emprestimo(user0000000001, l1, "11 De Julho", 0)
bibliotecalocal.devolver(emprestimo1)
bibliotecalocal.retirar(user0000000001, l1)

inspect(user0000000001, private=True, methods=True)
inspect(bibliotecalocal, private=True, methods=True)
inspect(l1, private=True, methods=True)


