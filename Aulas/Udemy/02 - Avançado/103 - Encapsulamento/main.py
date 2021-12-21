"""
public, protected, private - Outras linguagens

Python (Convenção):
_   weak private   / privado fraco / protected
__  strong private / privado forte / private
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}           # Dado de estrema importância, não pode mudar fora da classe

    def __inserir_clientes(self, identificador, nome):          # Da pra fazer com métodos também
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {identificador: nome}

        else:
            self.__dados['clientes'].update({identificador: nome})

    def remover_cliente(self, identificador):
        del self.__dados['clientes'][identificador]

    def listar_clientes(self):
        for k, v in self.__dados['clientes'].items():
            print(k, v)

    def inserir_clientes(self, identificador, nome):
        self.__inserir_clientes(identificador, nome)

    @property
    def dados(self):
        return self.__dados


loja = BaseDeDados()
loja.inserir_clientes(0, "André")
loja.inserir_clientes(1, "Júlio")
loja.inserir_clientes(2, "Pedro")

print(loja._BaseDeDados__dados)             # Não poderia mexer em "__dados", mas dá

print(loja.dados)                           # O jeito certo de pegar esse valor, com getter
