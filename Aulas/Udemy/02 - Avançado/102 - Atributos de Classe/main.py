print("Clase A")


class A:
    variavel_de_classe = 123


a1 = A()
a1.variavel_de_classe = 321     # Criou o atributo "variavel_de_classe" para a1, não mudou da classe A

a2 = A()

print("\"variavel_de_classe\" dentro dos objetos")
print(f'a1 - {a1.variavel_de_classe}')
print(f'a2 - {a2.variavel_de_classe}')

print()

print("Dicionários dos objetos")
print(f'a1 - {a1.__dict__}')
print(f'a1 - {a2.__dict__}')

print("\nClasse B")


class B:
    variavel_de_classe = 123

    def __init__(self):
        self.variavel_de_classe = 321


b1 = B()
b1.variavel_de_classe = 123     # Mudou o atributo "variavel_de_classe" em a1

b2 = B()

print("\"variavel_de_classe\" dentro dos objetos")
print(f'b1 - {b1.variavel_de_classe}')
print(f'b2 - {b2.variavel_de_classe}')

print()

print("Dicionários dos objetos")
print(f'b1 - {b1.__dict__}')
print(f'b1 - {b2.__dict__}')
