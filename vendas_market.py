import produto_market
total_item = 0

def vendasCaixa():
    print("SISTEMA DE CAIXA - VENDAS")

    while True:
        iniVendas = input("Digite: \n1 - Continuar \n2 - Voltar ao Menu Anterior\n")
        match iniVendas:
            case "1":
        #if iniVendas == "1":
                codigo = input("\nInforme o código do Item: ")
                if codigo in produto_market.produtos:
                    try:
                        quant_item = float(input("Informe a quantidade para venda: "))
                        if produto_market.produtos[codigo]['quantidade'] >= quant_item:
                            produto_market.produtos[codigo]['quantidade'] -= quant_item
                            valor_total = produto_market.produtos[codigo]['preco'] * quant_item
                            print(f"{valor_total:.2f}")
                            return codigo, valor_total, quant_item
                        else:
                            print("Sem estoque para venda.\n")
                            return None, 0.0, 0.0
                    except ValueError:
                        print("Por Gentileza, digite um número válido. 🚨🚨")    
                        return None, 0.0, 0.0
                else:
                    print("Item não encontrado. 🚨🚨")    
                    return None, 0.0, 0.0
            case "2":
                print("Cancelando Operação.")
                return None, 0.0, 0.0
