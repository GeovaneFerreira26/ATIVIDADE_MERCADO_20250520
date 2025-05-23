while True:
    validade = input("Digite a validade do Produto (DD/MM/AAAA): ")
    try:
        data_valida = datetime.strptime(validade, "%d/%m/%Y")  # Converte para formato correto
        break  # Sai do loop corretamente
    except ValueError:
        print("Data inválida! Insira no formato correto (DD/MM/AAAA).")

item = produto(codigo, nome, sessao, quantidade, preco, validade)  # Aqui ocorre a criação correta do objeto
print("\nProduto Cadastrado com Sucesso!")
print(item.exibir_info())

produtos[codigo] = {
    "nome": nome,
    "sessao": sessao,
    "quantidade": quantidade,
    "preco": preco,
    "validade": item.validade.strftime('%d/%m/%Y')
}

if sessao not in sessoes:
    sessoes[sessao] = []  
sessoes[sessao].append({
    "codigo": codigo,
    "nome": nome,
    "quantidade": quantidade,
    "preco": preco,
    "validade": item.validade.strftime('%d/%m/%Y')
})

for codigo, dados in produtos.items():
    print(f"\nCódigo: {codigo} \nItem: {dados['nome']} \nSessão: {dados['sessao']} \nQuantidade: {dados['quantidade']}\nUnid. Preço: R${dados['preco']}\nValidade: {dados['validade']}")
