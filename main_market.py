# os "import" serve para trazer dados/funções de cada módulo/arquivo criado.
import produto

# função "opmenu" serve para chamar o menu completo na tela de prompt.


def opmenu():
    print("\n|-----------    ⛽ MERCADO GGK - MENU DE ATIVIDADES       -----------------|")
    print("| 1. CADASTRO DE PRODUTO.     | 4. PESQUISAR POR SESSÃO.                   |")
    print("| 2. LISTAR PRODUTOS.         | 5.                                         |")
    print("| 3. PESQUISAR POR CÓDIGO.    | 0. ENCERRAR PROGRAMA .                     |\n")

while True:
    opmenu()
    oper = input("Selecione uma Opção. ")
    match oper:
        case "1":
            produto.cadastro_produto()
        case "2":
            produto.listarProduto()
        case "3":
            produto.pesquisaritem()  
        case "4":
            produto.pesquisarsessao()
        case "_":
            print("Opção Inválida.")
        case "0":
            print("Encerrando o Programa.")
            break