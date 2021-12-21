from classes import Pessoa, Cliente, ClienteVIP

"""
A sobreposição segue a hierarquia da herança
Como os filhos herdam tudo, eles tem o que o pai tem
Agora, se os filhos sobreporem algo, esse vai ser sopreposto o do pai

A função super retorna a classe pai

A classe pai dá uma interface para as classes filhas
As quais podem sobrepor membros, e dar outra interface para as suas classes filhas
"""

cliente_vip = ClienteVIP("Maria", 27, "Dias")

cliente_vip.falar()
