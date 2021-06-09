import sys

lista = range(10)
lista = iter(lista)

print("Tamanho da lista:", sys.getsizeof(lista), "Bytes")

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

print("<" + "-=" * 10 + "->")

def gera():
    for n in range(10):
        yield n

g = gera()

for i in g:
    print(i)

print("<" + "-=" * 10 + "->")

def gera2():
    yield "Valor 1"
    yield "Valor 2"
    yield "Valor 3"

g = gera2()

for i in g:
    print(i)

print("<" + "-=" * 10 + "->")

l1 = [i for i in range(pow(10, 5))]     # lista
l2 = (i for i in range(pow(10, 5)))     # gerador

tamanho_lista   = sys.getsizeof(l1)
tamanho_gerador = sys.getsizeof(l2)

print(f"tamanho lista  : {tamanho_lista} Bytes")
print(f"tamanho gerador: {tamanho_gerador} Bytes")
print(f"                 {tamanho_lista / tamanho_gerador:.2f} vezes maior")
