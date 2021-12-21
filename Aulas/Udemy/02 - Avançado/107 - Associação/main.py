from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

# Associação é tipo relação entre classes
# Nesse caso as classes podem existir sozinhas independe da outra

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever("abc")

escritor.ferramenta = maquina
escritor.ferramenta.escrever("banana")          # Foi associado a clase inteira, e chamou o método

del escritor                                    # A classe Canete e MaquinaDeEscrever é independente
print(caneta.marca)                             # da clase escritor
maquina.escrever("Algo sei lá")
