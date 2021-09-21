
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def mudar_nome(self, nome):
        self.nome = nome

    def ver_nome(self):
        return self.nome

    @property
    def nome(self):                                 # Getter nome
        return self._nome

    @nome.setter
    def nome(self, value):                          # Setter nome
        self._nome = f'{value} {value.upper()}'

    @property
    def _nome(self):                                # Getter _nome
        return self._nome2

    @_nome.setter
    def _nome(self, value):                         # Setter _nome
        self._nome2 = f'{value} {value.split()[0].lower()}'


p1 = Pessoa("Alguém")
print(p1.nome)
