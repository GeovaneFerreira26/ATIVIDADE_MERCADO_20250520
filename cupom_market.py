import produto_market
import vendas_market
from datetime import datetime


def cupom(itens):
    largura = 150
    valor_total = 0
    print("\n\n" +"-" * largura)
    print (f"| {'CUPOM DE VENDAS':^147}|")
    print("-" * largura)

    for item in itens:
        codigo, quant_item = item["codigo"], item["quantidade"]

        if codigo in produto_market.produtos:
            dados = produto_market.produtos[codigo]
        else:
            continue
        
        validade_item = datetime.strptime(dados['validade'], "%d/%m/%Y")
        status_validade = "Em Dia ✅✅"
        if validade_item < datetime.now():
            status_validade = "Vencido ⛔⛔"

        valor_item = dados['preco'] * quant_item
        valor_total += valor_item


    
        
        print(f"| ITEM: {dados['nome']:<19}| SESSÃO: {dados['sessao']:<19}| VAL {dados['validade']} - {status_validade:<11}| V. UNIT: R$ {dados['preco']:<6.2f}| QUANT/PESO: {quant_item:<5.2f}| SUBTOTAL: R$ {valor_item:<6.2f} |")
    print("-" * largura)
    print(f"| VALOR TOTAL DA COMPRA: R$ {valor_total:>120.2f} |")
    print("-" * largura)
    print(f"|{'OBRIGADO PELA PREFERÊNCIA.':^148}|")
    print(f"|{'MERCADOS GGK.':^148}|")
    print("-" * largura)
    print("\n\n")



    


    #     print("\n\n" +"-" * largura)
    #     print (f"| {'CUPOM DE VENDAS':^39}|")
    #     print("-" * largura)
        
    #     print(f"| ITEM: {dados['nome']:>32} |")
    #     print(f"| PRODUTO: {status_validade:<12} VAL {dados['validade']} |")
    #     print(f"| SESSÃO: {dados['sessao']:>30} |")
    #     print(f"| VALOR UNITÁRIO: R$ {dados['preco']:>19.2f} |")
    #     print(f"| QUANTIDADE - PESO: {quant_item:>19.2f} |")
    #     print(f"| SUBTOTAL: R$ {valor_item:>22.2f} |")
    #     print("-" * largura)
    # print(f"VALOR TOTAL DA COMPRA: R$ {valor_total:>14.2f} |")
    # print("-" * largura)
    # print(f"|{'OBRIGADO PELA PREFERÊNCIA.':^40}|")
    # print(f"|{'MERCADOS GGK.':^40}|")
    # print("-" * largura)
    # print("\n\n")
    
