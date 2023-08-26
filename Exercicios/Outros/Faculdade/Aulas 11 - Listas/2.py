from random import randint

lista1 = [randint(0, 10) for i in range(5)]
lista2 = [randint(0, 10) for i in range(5)]
lista3 = []

print(f"Lista 1 = {lista1}")
print(f"Lista 2 = {lista2}")

for valor in lista1:
    if valor in lista2 and valor not in lista3:
        lista3.append(valor)

if len(lista3) == 0:
    print("Não tem valores iguais")
else:
    print("\nValores iguais: ")
    print(*lista3, sep=", ")
