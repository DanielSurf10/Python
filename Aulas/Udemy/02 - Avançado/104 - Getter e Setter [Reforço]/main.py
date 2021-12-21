
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def mudar_nome(self, nome):
        self.nome = nome

    def ver_nome(self):
        return self.nome

    def ver_sobrenome(self):
        return self.sobrenome

    # Setters para nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        print(f"setter 1 entra: {value}")
        print(f"setter 1 sai  : {value} {value.upper()}")
        self._nome = f"{value} {value.upper()}"

    @property
    def _nome(self):
        return self._nome2

    @_nome.setter
    def _nome(self, value):
        print(f"setter 2 entra: {value}")
        print(f"setter 2 sai  : {value} {value.lower()}")
        self._nome2 = f'{value} {value.lower()}'

    # Getters para nome
    @property
    def sobrenome(self):
        print(f"getter 1 sai: {self._sobrenome} {self._sobrenome.upper()}")
        return f'{self._sobrenome} {self._sobrenome.upper()}'

    @sobrenome.setter
    def sobrenome(self, value):
        self._sobrenome = value

    @property
    def _sobrenome(self):
        print(f"getter 2 sai: {self._sobrenome2} {self._sobrenome2.lower()}")
        return f'{self._sobrenome2} {self._sobrenome2.lower()}'

    @_sobrenome.setter
    def _sobrenome(self, value):
        self._sobrenome2 = value


# Setters
print("Setters\n")

print("declaração")
p1 = Pessoa("Alguém", "Outro")
print("declarado\n")

print(f'{"p1.nome":<11}: {p1.nome}')
print(f'{"p1._nome":<11}: {p1._nome}')
print(f'{"p1._nome2":<11}: {p1._nome2}')
print(f'{"p1.__dict__":<11}: {p1.__dict__}')

# Mudando o nome
print("\nComeçando a mudar")
p1.mudar_nome('Ninguém')
print("Mudado")
print(p1.__dict__)

print("\n\nGetters\n")
print("Pegando valor")
print(p1.ver_sobrenome())
print("Valor pego")

print(f'\t{"p1.sobrenome":<11}: {p1.sobrenome}')
print(f'\t{"p1._sobrenome":<11}: {p1._sobrenome}')
print(f'\t{"p1._sobrenome2":<11}: {p1._sobrenome2}')
print(f'\t{"p1.__dict__":<11}: {p1.__dict__}')
