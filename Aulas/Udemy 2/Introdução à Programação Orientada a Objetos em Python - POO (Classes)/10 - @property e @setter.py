# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor):
        # private protected
        self.cor = cor
        self._cor_tampa = None

    @property                           # decorador para o getter
    def cor(self):
        # print('ESTOU NO GETTER')
        return self._cor

    @cor.setter                         # decorador para o setter usando o do getter
    def cor(self, valor):
        # print('ESTOU NO SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):                        # getter - mesmo que não tenha " cor", vai vir com isso
        return self._cor_tampa + " cor"         # getter retorna algum valor

    @cor_tampa.setter
    def cor_tampa(self, valor):                 # setter - escreve um valor na instância
        if valor == "Azul":                     # Restrição para que se for "Azul" torna "Laranja"
            self._cor_tampa = "Laranja"
        else:
            self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)
