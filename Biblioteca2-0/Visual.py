from rich import print
from rich.table import Table
from rich.panel import Panel  

def menu_principal():
    texto = ("[bold white][1][/] Cadastrar [bold #F9DC5C]ITEM[/]\n"
    "[bold white][2][/] Cadastrar [#3185FC bold]USUÁRIO[/]\n"
    "[bold white][3][/] Exibir [#04395E bold]INFORMAÇÕES USUÁRIO[/]\n"
    "[bold white][4][/] Exibir [#E6E1C5]ACERVO[/]\n"
    "[bold white][5][/] [#283618]RETIRAR[/]\n"
    "[bold white][6][/] [#283618]DEVOLVER[/]"
    )
    menu = Panel(texto, title="[bold green]MENU[/]")
    print(menu)

def itens_disponiveis():
    print(f"[#F9DC5C bold]ITENS[/] disponíveis: ")
    print(f"[white bold][1] LIVRO[/]")
    print(f"[white bold][2] REVISTA[/]")

def exibir_acervo_estilizado(biblioteca_recebida):
    tabela = Table(title="[white]ACERVO[/]")
    tabela.add_column("ITEM")
    tabela.add_column("AUTOR")
    tabela.add_column("DISPONIBILIDADE")
    for item in biblioteca_recebida.itens:
        if item.disponibilidade == True:
            status = "[green bold]DISPONÍVEL[/]"
        else:
            status = "[red bold]INDISPONÍVEL[/]"
        tabela.add_row(item.titulo, item.autor, status)
    print(tabela)
#F9DC5C ITEM
#
#510D0A ERRO
def senha_invalida():
    print(f"[#FF0000]Senha [bold]INVÁLIDA[/]")

def insira_senha():
    print(f"[#F3A712]Insira a [bold]SENHA:[/]")

def usuario_nao_encontrado():
    print(f"[#2EC4B6 bold]USUÁRIO[/] [#2EC4B6]não encontrado[/]")

def usuario_cadastrado():
    print(f"[#2EC4B6 bold]USUÁRIO[/] [#2EC4B6]já cadastrado[/]")

def exibir_informacoes(usuario):
    print(f"EXIBINDO INFORMAÇÕES DE(A):")
    print(f"[#2EC4B6 bold]NOME: {usuario.nome}[/]")
    print(f"[#2EC4B6 bold]EMPRÉSTIMOS ATUAIS: {usuario._emprestimos_realizados}[/]")
    tabela = Table(title="[white]ITENS RETIRADOS[/]")
    tabela.add_column("ITEM")
    tabela.add_column("AUTOR")
    tabela.add_column("DISPONIBILIDADE")
    for item in usuario._itens_emprestados:
        if item.item.disponibilidade == True:
            status = "[green bold]DISPONÍVEL[/]"
        else:
            status = "[red bold]INDISPONÍVEL[/]"
        tabela.add_row(item.titulo, item.autor, status)
    print(tabela)

def emprestimo_nao_encontrado():
    print(f"[#2EC4B6 bold]EMPRÉSTIMO[/] [#2EC4B6]não encontrado[/]")

def emprestimo_excedente():
    print(f"[#FF0000 bold]Limite de EMPRÉSTIMOS[/] [#FF0000]atingido[/]")

def item_indisponivel():
    print(f"[#F9DC5C bold]ITEM[/] [#FF0000]indisponível[/]")

def emprestimo_nao_encontrado():
    print(f"[#FF0000 bold]EMPRÉSTIMO[/] [#FF0000]não encontrado[/]")

def item_cadastrado():
    print(f"[#F9DC5C bold]ITEM[/] já cadastrado")

def opcao_invalida():
    print("[#FF0000 bold]OPÇÃO INVÁLIDA[/]")