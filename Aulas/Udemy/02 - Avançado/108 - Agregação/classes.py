class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.valor
        return soma

    def __del__(self):
        print("Clase principal deletada")


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __del__(self):
        print(self.nome + " foi deletado")
