# os "import" serve para trazer dados/funções de cada módulo/arquivo criado.
import produto_market
import vendas_market
import cupom_market

# função "opmenu" serve para chamar o menu completo na tela de prompt.


def opmenu():
    print("\n|-----------    🛒 MERCADO GGK - MENU DE ATIVIDADES       -----------------|")
    print("| 1. CADASTRO DE PRODUTO.     | 4. PESQUISAR POR SESSÃO.                   |")
    print("| 2. LISTAR PRODUTOS.         | 5. CAIXA VENDAS.                           |")
    print("| 3. PESQUISAR POR CÓDIGO.    | 0. ENCERRAR PROGRAMA .                     |\n")

while True:
    opmenu()
    oper = input("Selecione uma Opção. ")
    match oper:
        case "1":
            produto_market.cadastro_produto()
        case "2":
            produto_market.listarProduto()
        case "3":
            produto_market.pesquisaritem()  
        case "4":
            produto_market.pesquisarsessao()
        case "5":
            #vendas_market.vendasCaixa()
            codigo, valor_total, quant_item = vendas_market.vendasCaixa()
            
           # cupom_market.cupom(codigo, valor_total, quant_item,)
            cupom_market.cupom(codigo, valor_total, quant_item)

        case "_":
            print("Opção Inválida.")
        case "0":
            print("Encerrando o Programa.")
            break