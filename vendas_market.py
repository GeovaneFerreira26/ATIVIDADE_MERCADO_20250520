import produto_market
total_item = 0

def vendasCaixa():
    print("\n\nSISTEMA DE CAIXA - VENDAS")
    itens_venda = []

    while True:
        iniVendas = input("Digite: \n1 - Continuar \n2 - Voltar ao Menu Anterior\n")
        match iniVendas:
            case "1":
                codigo = input("\nInforme o código do Item: ")
                if codigo in produto_market.produtos:
                    try:
                        quant_item = float(input("Informe a quantidade para venda: "))
                        if produto_market.produtos[codigo]['quantidade'] >= quant_item:
                            produto_market.produtos[codigo]['quantidade'] -= quant_item
                            valor_unit = produto_market.produtos[codigo]['preco']
                            subtotal = valor_unit * quant_item
                            itens_venda.append({"codigo": codigo, "quantidade": quant_item, "valor_unit": valor_unit, "subtotal": subtotal})
                        else:
                            print("Sem estoque para venda.\n")
                            #return None, 0.0, 0.0
                    except ValueError:
                        print("Por Gentileza, digite um número válido. 🚨🚨")    
                        #return None, 0.0, 0.0
                else:
                    print("Item não encontrado. 🚨🚨")    
                    #return None, 0.0, 0.0
            case "2":
                print("Cancelando Operação.")
                break
    return itens_venda
