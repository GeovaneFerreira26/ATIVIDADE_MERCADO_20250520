import produto_market
import vendas_market
from datetime import datetime
def cupom(codigo, valor_total, quant_item,):
    if codigo in produto_market.produtos:
        dados = produto_market.produtos[codigo]
    else:
        return
    
    largura = 42
    
    validade_item = datetime.strptime(dados['validade'], "%d/%m/%Y")
    status_validade = "Em Dia ✅✅"
    if validade_item < datetime.now():
        status_validade = "Vencido ⛔⛔"


    print("\n\n" +"-" * largura)
    print (f"| {'CUPOM DE VENDAS':^39}|")
    print("-" * largura)
    
    print(f"| ITEM: {dados['nome']:>32} |")
    print(f"| Produto {status_validade:<13} VAL {dados['validade']} |")
    print(f"| SESSÃO: {dados['sessao']:>30} |")
    print(f"| VALOR UNITÁRIO: R$ {dados['preco']:>19.2f} |")
    print(f"| QUANTIDADE - PESO: {quant_item:>19.2f} |")
    print(f"| Valor Total: R$ {valor_total:>22.2f} |")
    print("-" * largura)
    print(f"|{'OBRIGADO PELA PREFERÊNCIA.':^40}|")
    print(f"|{'MERCADOS GGK.':^40}|")
    print("-" * largura)
    print("\n\n")
    
