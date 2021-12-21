
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * percentual / 100)

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            self._preco = float(valor.replace("R$", ''))
            return

        self._preco = valor


p1 = Produto("Copo", 2)
p2 = Produto("Camisa", "R$5")   # "R$5" não era o esperado, e sim um inteiro ou float
p2.desconto(10)

print(f'| {"Nome":^10} | {"preço":^7} |')
print(f'| {p1.nome:^10} | {p1.preco:^7.2f} |')
print(f'| {p2.nome:^10} | {p2.preco:^7.2f} |')
