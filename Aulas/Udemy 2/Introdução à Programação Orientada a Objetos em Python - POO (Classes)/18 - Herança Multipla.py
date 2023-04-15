# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A         - A ordem importa
# D -> B -> C -> A
#
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 usa C3 superclass linearization
# para gerar o mro.
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#                                                                                                                        
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro() - uma lista
# Ou o atributo __mro__ - uma tupla


class O(): 
    pass

class AA(O): 
    pass

class BB(O): 
    pass

class CC(O): 
    pass

class DD(O): 
    pass

class EE(O): 
    pass

class K1(CC, AA, BB): 
    pass

class K3(AA, DD): 
    pass

class K2(BB, DD, EE): 
    pass

class Z(K1, K3, K2): 
    pass


num = 0
for classe in Z.mro():
    print(f"{num + 1:2} - {classe.__name__:6}", end='')
    num += 1
    if (num % 3 == 0):
        print()
print("\n")

#########################################################################################################################


class A:
    def quem_sou(self):
        print('A')


class B(A):
    def quem_sou(self):
        print('B')


class C(A):
    def quem_sou(self):
        print('C')


class D(B, C):                  # Formou o diamante, a ordem importa
    def quem_sou(self):
        print('D')

# [D, B, C, A, object]          # MRO da classe D


print("[", end='')
for classe in D.mro():
    if classe.__name__ == "object":
        print(f"{classe.__name__}]")
        continue
    print(f"{classe.__name__}", end=', ')
