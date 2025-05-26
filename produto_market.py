from datetime import datetime

produtos = {}
sessoes = {}
tp_sessao = {"1":"AÇOUGUE", "2":"FRIOS E LATICÍNIOS", "3":"PADARIA", "4":"BEBIDAS", "5":"HIGIENE PESSOAL", "6":"LIMPEZA", "7":"HORTIFRUTI", "8":"MERCEARIA"}

class produto: # função para armazenar dados do produto
    def __init__(self, codigo, nome, sessao, quantidade, preco, validade):
        self.codigo = codigo
        self.nome = nome
        self.sessao = sessao
        self.quantidade = quantidade
        self.preco = preco
        self.validade = datetime.strptime(validade, "%d/%m/%Y")

    def exibir_info(self):
        return f"Código: {self.codigo}\nProduto: {self.nome}\nSessão: {self.sessao}\nQuantidade: {self.quantidade}\nPreço: {self.preco}\nValidade: {self.validade.strftime('%d/%m/%Y')}"

def cadastro_produto():
    print("SISTEMA DE CADASTRO DE PRODUTOS.")
    while True:
        codigo = input("Digite o código para Cadastro do Produto: ").strip()
        if not codigo:
            print("Dados Inválidos. 🚨🚨")
        elif not codigo.isdigit():
            print("Por Favor, só pode conter números no Código. 🚨🚨")
        elif codigo in produtos:
            print("Código já usado, por favor, digite um Código novo..🚨🚨")
        else:
            break

    nome = input("Digite o nome do Produto: ").upper()
    print("Informe a Sessão de Cadastro:")

    for chave, valor in tp_sessao.items():
        print(f"{chave} - {valor}")
    while True:
        selec_sessao = input("Digite a Sessão do produto: ").strip()
        if selec_sessao in tp_sessao:
            sessao = tp_sessao[selec_sessao]
            break
        else:
            print("Opção Escolhida Inválida - Repita o processo novamente.")
    while True:
        try:
            quantidade = float(input("Digite a quantidade do Produto: "))
            if quantidade >= 0:
                break
            else:
                print("Quantidade definida inferior ao permitido. 🚨🚨")   
        except ValueError:
            print("Dados Inválidos.🚨🚨")
    while True:                        
        try:
            preco = float(input("Digite o valor de venda da Unidade: "))
            if preco > 0:
                break
            else:
                print("A precificação está incorreta. 🚨🚨")
        except ValueError:
            print("Dados Inválidos.🚨🚨")
    while True:
        validade = input("Digite a validade do Produto (DD/MM/AAAA): ")
        try:
            data_valida = datetime.strptime(validade, "%d/%m/%Y")  # Tenta converter para um formato correto
            break #return data_valida.strftime("%d/%m/%Y")  # Retorna a data formatada corretamente.
        except ValueError:
            print("Data inválida! Insira no formato correto (DD/MM/AAAA).")

    item = produto(codigo, nome, sessao, quantidade, preco, validade)
    print("\nProduto Cadastrado com Sucesso!")
    print(item.exibir_info())

    produtos[codigo] = {"nome": nome, "sessao": sessao, "quantidade": quantidade, "preco": preco, "validade": item.validade.strftime('%d/%m/%Y')} # "item.validade" - Armazena como datetime, não como string

    if sessao not in sessoes:
        sessoes[sessao] = [] # Inicializa a sessão como uma lista vazia
    sessoes[sessao].append({"codigo": codigo, "nome": nome, "quantidade": quantidade, "preco": preco, "validade": item.validade.strftime('%d/%m/%Y')}) # "item.validade" - Armazena como datetime, não como string

    for codigo, dados in produtos.items():
        print(f"\nCódigo: {codigo} \nItem: {dados['nome']} \nSessão: {dados['sessao']} \nQuantidade: {dados['quantidade']}\nUnid. Preço: R${dados['preco']}\nValidade: {dados['validade']}")

# cadastro_produto()


def listarProduto():
    print("SISTEMA DE LISTAGEM DO ESTOQUE.")
    if not produtos:
        print ("Não há produto cadastrado.")
        return
    for codigo, dados in produtos.items():
        print(f"| Código: {codigo:<5} | Item: {dados['nome']:<20} | Sessão: {dados['sessao']:<18} | Quantidade: {dados['quantidade']:<5} | Preço Unid.: {dados['preco']} | Validade do Produto: {dados['validade']} |")
        if isinstance(dados['validade'], str):
            validade = datetime.strptime(dados['validade'], "%d/%m/%Y")
        else:
            validade = dados['validade']
        if validade < datetime.now():
            print ("| Produto Vencido")

#listarProduto()


def pesquisaritem():
    print("SISTEMA DE PESQUISA DE ITEM NO ESTOQUE.")
    codigo = input("Digite Código para Pesquisa: ")
    if codigo in produtos:
        dados = produtos[codigo]
        print(f"| Item: {dados['nome']:<20} | Sessão: {dados['sessao']:<18} | Quantidade: {dados['quantidade']:<5} | Preço Unid.: {dados['preco']:<6} | Validade do Produto: {dados['validade']} |")
    else:
        print("Produto não encontrado.")
        return
    if isinstance(dados['validade'], str):
        validade = datetime.strptime(dados['validade'], "%d/%m/%Y")
    else:
        validade = dados['validade']
        return
    if validade < datetime.now():
            print ("| Produto Vencido🚨🚨🚨")
#pesquisaritem()

def pesquisarsessao():
    print("SISTEMA DE PESQUISA POR SESSÃO.")
    print("informe a Sessão que deseja filtrar:")

    for chave, valor in tp_sessao.items():
        print(f"{chave} - {valor}")

    sessao_pesq = input("Digite o código correspondente. ")

    if sessao_pesq in tp_sessao:
        sessao_filtrada = tp_sessao[sessao_pesq]
        
        if sessao_filtrada in sessoes:
            print(f"\nProdutos encontrados na Sessão {sessao_filtrada}: ")

            for dados in sessoes[sessao_filtrada]:
                print(f"Sessão: {sessao_filtrada:<18} | Código: {dados['codigo']:<5} | Item: {dados['nome']:<20} | Quantidade: {dados['quantidade']:<5} | Preço Unid.: {dados['preco']:<6} | Validade: {dados['validade']} |")
                    
                if isinstance(dados['validade'], str):
                    validade = datetime.strptime(dados['validade'], "%d/%m/%Y")
                else:
                    validade = dados['validade']
                
                if validade < datetime.now():
                    print("Produto Vencido 🚨")
        else:
            print("Sem itens cadastrados nessa Sessão.")
    else:
        print("Código de sessão inválido.")


        