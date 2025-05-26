def cadastro_produto():
    print("SISTEMA DE CADASTRO DE PRODUTOS.")
    codigo = input("Digite o código para Cadastro do Produto: ")
    nome = input("Digite o nome do Produto: ").upper()
    print("Informe a Sessão de Cadastro:")
    
    for chave, valor in tp_sessao.items():
        print(f"{chave} - {valor}")
    
    selec_sessao = input("Digite a Sessão do produto: ")
    
    if selec_sessao in tp_sessao:
        sessao = tp_sessao[selec_sessao]
    
    quantidade = int(input("Digite a quantidade do Produto: "))
    preco = float(input("Digite o valor de venda da Unidade: "))
    validade = input("Digite a validade do Produto (DD/MM/AAAA): ")

    item = produto(codigo, nome, sessao, quantidade, preco, validade)
    print("\nProduto Cadastrado com Sucesso!")
    print(item.exibir_info())

    produtos[codigo] = {
        "nome": nome, "sessao": sessao, "quantidade": quantidade,
        "preco": preco, "validade": item.validade.strftime('%d/%m/%Y')
    }

    # 🔹 Posicionamento correto da verificação da sessão:
    if sessao not in sessoes:
        sessoes[sessao] = []  # Inicializa a sessão como uma lista vazia

    # Agora adiciona o produto à sessão corretamente:
    sessoes[sessao].append({
        "codigo": codigo, "nome": nome, "quantidade": quantidade,
        "preco": preco, "validade": item.validade.strftime('%d/%m/%Y')
    })


    def pesquisarsessao():
    print("SISTEMA DE PESQUISA POR SESSÃO.")
    print("Informe a Sessão que deseja filtrar:")
    
    for chave, valor in tp_sessao.items():
        print(f"{chave} - {valor}")
    
    sessao_pesq = input("Digite o código correspondente: ")
    
    if sessao_pesq in tp_sessao:
        sessao_filtrada = tp_sessao[sessao_pesq]

        # 🔹 Alteração: verificar apenas a sessão informada!
        if sessao_filtrada in sessoes:
            print(f"\nProdutos encontrados na sessão {sessao_filtrada}:")
            for dados in sessoes[sessao_filtrada]:  # Percorrer somente a sessão escolhida
                print(f"Sessão: {sessao_filtrada:<18} | Código: {dados['codigo']:<5} | Item: {dados['nome']:<20} | Quantidade: {dados['quantidade']:<5} | Preço Unid.: {dados['preco']:<6} | Validade: {dados['validade']} |")

                if isinstance(dados['validade'], str):
                    validade = datetime.strptime(dados['validade'], "%d/%m/%Y")
                else:
                    validade = dados['validade']

                if validade < datetime.now():
                    print("Produto Vencido 🚨")
        else:
            print("Nenhum produto encontrado nessa sessão.")
    else:
        print("Código de sessão inválido.")



        from datetime import datetime

def validar_data():
    while True:
        data_input = input("Digite a validade do Produto (DD/MM/AAAA): ")
        try:
            data_valida = datetime.strptime(data_input, "%d/%m/%Y")  # Tenta converter
            return data_valida.strftime("%d/%m/%Y")  # Retorna a data formatada
        except ValueError:
            print("Data inválida! Insira no formato correto (DD/MM/AAAA).")

# Testando
data_correta = validar_data()
print(f"Data cadastrada corretamente: {data_correta}")