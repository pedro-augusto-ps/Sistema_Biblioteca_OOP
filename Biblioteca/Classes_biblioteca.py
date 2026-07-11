from abc import ABC, abstractmethod
import hashlib
from datetime import datetime

class Item(ABC):
    """Classe mãe, e é abstrata, nesse código item será
    herdado para livro e revista"""
    def __init__(self, autor, titulo, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    @abstractmethod
    def calcular_multa(self, dias_atrasado):
        pass

class Livro(Item):
    """Classe livro, herdando atributos de item e 
    obrigando a criação do método calcular multa"""
    def __init__(self, autor, titulo, disponivel):
        super().__init__(autor, titulo, disponivel)

    def calcular_multa(self, dias_atrasado):
        """Calcula a multa do livro, RS$1,00 por dia atrasado"""
        multa = dias_atrasado * 1.00
        return multa

class Revista(Item):
    """Classe Revista, herdando atributos de item e 
    obrigando a criação do método calcular multa"""
    def __init__(self, autor, titulo, disponivel):
        super().__init__(autor, titulo, disponivel)

    def calcular_multa(self, dias_atrasado):
        """Calcula a multa da revista, R$0.50 por dia atrasado"""
        multa = dias_atrasado * 0.50
        return multa

class Usuario:
    """Crio um usuário, nome(+), senha(-), emprestimos começa com 0"""
    def __init__(self, nome, senha):
        self.nome = nome
        self.__senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()  #Transformo a senha em hash de cara
        self._emprestimos = 0

    @property
    def senha_segura(self):
        return self.__senha
    
    @senha_segura.setter
    def senha_segura(self, nova_senha):
        self.__senha = hashlib.sha256(nova_senha.encode('utf-8')).hexdigest()

class Emprestimo:
    def __init__(self, usuario, item, data_emprestimo, dias_atrasado):   #USUARIO: Instacia da classe usuario, ITEM: Instancia da classe item
        self.usuario = usuario
        self.item = item
        self.data_emprestimo = data_emprestimo
        self.dias_atrasado = dias_atrasado 

    def finalizar(self):
        self.item.disponivel = True 
        self.usuario._emprestimos -= 1
        print(f"EMPRÉSTIMOS: {self.usuario._emprestimos}")

class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.itens = []
        self.emprestimos = []

    def retirar(self, usuario, item):
        senha_para_retirar = str(input("Insira a sua senha: "))
        if hashlib.sha256(senha_para_retirar.encode('utf-8')).hexdigest() != usuario.senha_segura:
            print(f"Senha Inválida!")
        else:
            if usuario._emprestimos < 3:
                if item.disponivel == True:
                    item.disponivel = False
                    novo_emprestimo = Emprestimo(usuario, item, datetime.now(), 0)
                    self.emprestimos.append(novo_emprestimo)
                    usuario._emprestimos += 1
                    
    def devolver(self, usuario, item):
        for livro_emprestado in self.emprestimos:
            if livro_emprestado.usuario == usuario and livro_emprestado.item == item:
                livro_emprestado.finalizar()
                self.emprestimos.remove(livro_emprestado)
                break
            