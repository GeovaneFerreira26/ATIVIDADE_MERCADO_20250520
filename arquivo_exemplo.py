#    from datetime import datetime

# class Produto:
#     def __init__(self, nome, quantidade, validade):
#         self.nome = nome
#         self.quantidade = quantidade
#         self.validade = datetime.strptime(validade, "%d/%m/%Y")  # Converte para data

#     def esta_vencido(self):
#         """Verifica se o produto está vencido"""
#         return datetime.now() > self.validade

#     def exibir_informacoes(self):
#         """Retorna uma descrição do produto"""
#         status = "Vencido" if self.esta_vencido() else "Dentro do prazo"
#         return f"Produto: {self.nome}\nQuantidade: {self.quantidade}\nValidade: {self.validade.strftime('%d/%m/%Y')} ({status})"

# # Exemplo de uso:
# leite = Produto("Leite", 50, "25/05/2025")
# print(leite.exibir_informacoes())



from datetime import datetime

class Produto:
    def __init__(self, nome, quantidade, validade):
        self.nome = nome
        self.quantidade = quantidade
        self.validade = datetime.strptime(validade, "%d/%m/%Y")

    def esta_vencido(self):
        return datetime.now() > self.validade

    def exibir_informacoes(self):
        status = "Vencido" if self.esta_vencido() else "Dentro do prazo"
        return f"Produto: {self.nome}\nQuantidade: {self.quantidade}\nValidade: {self.validade.strftime('%d/%m/%Y')} ({status})"

class Estoque:
    def __init__(self):
        self.produtos = {}  # Dicionário para armazenar produtos

    def adicionar_produto(self, nome, quantidade, validade):
        self.produtos[nome] = Produto(nome, quantidade, validade)

    def remover_produto(self, nome):
        if nome in self.produtos:
            del self.produtos[nome]
            return f"Produto '{nome}' removido do estoque."
        return f"Produto '{nome}' não encontrado."

    def listar_produtos(self):
        return "\n\n".join(produto.exibir_informacoes() for produto in self.produtos.values())

    def verificar_vencidos(self):
        vencidos = [produto.nome for produto in self.produtos.values() if produto.esta_vencido()]
        return f"Produtos vencidos: {', '.join(vencidos)}" if vencidos else "Nenhum produto vencido."

# Exemplo de uso
estoque = Estoque()
estoque.adicionar_produto("Leite", 50, "25/05/2025")
estoque.adicionar_produto("Ovos", 100, "15/05/2025")  # Vencido se hoje for depois de 15/05/2025
estoque.adicionar_produto("Queijo", 30, "10/06/2025")

print(estoque.listar_produtos())
print("\n" + estoque.verificar_vencidos())

