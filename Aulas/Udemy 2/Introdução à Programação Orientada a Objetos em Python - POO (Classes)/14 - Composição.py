# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []                                 # Lista com outro objeto, é apagado junto com o "pai"

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))        # Aqui o objeto é criado dentro da classe - composição

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)                     # Aqui o objeto é criado fora da classe - agregação/associação

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):                                      # "Destrutor" usado para ver quando o objeto é destruído
        print('APAGANDO,', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)
endereco_externo = Endereco('Av Saudade', 123213)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1                                                # Destruindo o pai, os filhos são destruídos junto

print(endereco_externo.rua, endereco_externo.numero)
print(' AQUI TERMINA MEU CÓDIGO '.center(50, "#"))
