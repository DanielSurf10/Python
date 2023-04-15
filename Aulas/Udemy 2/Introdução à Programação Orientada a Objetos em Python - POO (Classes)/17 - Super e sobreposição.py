# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# 
# super() se referencia a classe pai sendo classe
# super(classe, objeto) se referencia a classe pai como objeto
# o MRO pega da pilha de classes, procura no pai, se não tiver no "avó" e assim vai

class Circulo:
    def __init__(self, raio):
        self.raio = raio                        # Círculo tem um raio
    
    def get_area(self):                         # Círculo tem uma área
        return (self.raio ** 2) * 3.14
    
    def get_perimetro(self):                    # Círculo tem um perímetro
        return self.raio * 2 * 3.14
    

class Cilindro(Circulo):                        # Herda tudo de círculo
    def __init__(self, raio, altura):
        super().__init__(raio)                  # Usa o __init__() da classe pai usando o super
        self.altura = altura                    # E incrementa a alura

    def get_area(self):
        return super(Cilindro, self).get_area() * self.altura
    
    def get_perimetro(self):
        return super().get_perimetro() * self.altura + super().get_perimetro() * 2
    

circulo = Circulo(5)
cilindro = Cilindro(7, 10)


print(f"Círculo:")
print(f"\tÁrea:\t\t{circulo.get_area():.2f}")
print(f"\tPerímetro:\t{circulo.get_perimetro():.2f}")

print()

print(f"Cilindro:")
print(f"\tÁrea:\t\t{cilindro.get_area():.2f}")
print(f"\tPerímetro:\t{cilindro.get_perimetro():.2f}")
