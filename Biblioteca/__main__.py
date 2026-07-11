from Classes_biblioteca import *
from rich import print, inspect

def main():
    l1 = Livro("A volta dos que não foram", "Códigosinistro", True)
    user00000000000001 = Usuario("Maurice", "binana")
    bibliotecadapraça = Biblioteca()
    inspect(user00000000000001, private=True, methods=True)
    inspect(l1, private=True, methods=True)
    inspect(bibliotecadapraça, private=True, methods=True)
    bibliotecadapraça.retirar(user00000000000001, l1)
    inspect(bibliotecadapraça, private=True, methods=True)
    inspect(user00000000000001, private=True, methods=True)
    inspect(l1, private=True, methods=True)
    
if __name__ == "__main__":
    main()