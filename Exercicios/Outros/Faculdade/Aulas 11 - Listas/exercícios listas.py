###################################################################################################
# Exercício 1

valores = []
pares = []
impares = []

while True:

    num = int(input("Digite um valor: "))
    continuar = input("Quer continuar [ S / N ]: ").lower()

    valores.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    if continuar == 'n':
        break

print("\nValores: ", end='')
print(*valores, sep=", ")

print("Impares: ", end='')
print(*impares, sep=", ")

print("Pares: ", end='')
print(*pares, sep=", ")


###################################################################################################
# Exercício 2

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


###################################################################################################
# Exercício 3

from random import random, randint

letras = ("A", "B", "C", "D", "E")

placas = [f"{letras[randint(0,4)]}{letras[randint(0,4)]}{letras[randint(0,4)]}-{randint(1000, 10000)}" for _ in range(15)]
multas = [round(random() * 1000, 2) for _ in range(15)]

print("Carros")
print(f"|{'Placa'.center(10)}| Multa")
for i in range(15):
    print(f"|{placas[i].center(10)}| R$ {multas[i]}")
print()

media = sum(multas) / 15
maiorQue300 = sum(1 for i in multas if i >= 300)

print(f"Média das multas: {media:.2f}")
print(f"Quantos acima de R$ 300: {maiorQue300}")


###################################################################################################
# Exercício 4

from random import randint

dias_semana = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")

dias = [dias_semana[randint(0, 6)] for _ in range(10)]
volume = [randint(0, 100) for _ in range(10)]
media_quarta = []

print("Valores:")
for i, a, b in zip(range(1, 11), dias, volume):
    print(f"{str(i).center(2)} - dia: {a.center(7)} - volume: {b}")
print()

for i in range(10):
    if dias[i] == "Quarta":
        media_quarta.append(volume[i])

media = sum(media_quarta)/len(media_quarta)
volume_total = sum(volume)

print(f"Média de volume de quartas: {media}")
print(f"Volume total: {volume_total}")


###################################################################################################
# Exercício 5

numero_alunos = 5
media_notas = 6
cursos = ("ccp", "tabs")

nomes = []
notas = []
curso = []

for i in range(numero_alunos):
    nomes.append(input(f"Digite o nome do {i + 1}º aluno: "))
    notas.append(int(input(f"Digite a nota do {i + 1}º aluno: ")))
    curso.append(input(f"Digite o curso do {i + 1}º aluno [ ccp / tabs ]: "))

tabs = curso.count("tabs")
media = sum(notas) / numero_alunos
acima_media = sum([1 for i in notas if i >= media_notas])

print(f"Quantidade tabs: {tabs}")
print(f"Média: {media}")
print(f"Quantidade acima da média: {acima_media}")


###################################################################################################
# Exercício 6

lista = []

while True:
    num = int(input("Digite um número: "))
    continuar = input("Quer continuar? [ S / N ]").lower()

    lista.append(num)

    if continuar == 'n':
        break

media = sum(lista)/len(lista)
print(f"A média é: {media}")
print(f"{sum([1 for i in lista if i >= media])} valores estão acima da média.")


###################################################################################################
# Exercício 7

from random import randint

salarios = [randint(500, 5000) for i in range(10)]

print("Salários: ", end='')
print(*salarios, sep=', ')
print()

media = sum(salarios)/10
maior = max(salarios)
menor850 = sum([1 for i in salarios if i < 850])

print(f"A média dos sálarios é: {media}")
print(f"O maior salário é: {maior}")
print(f"Tem {menor850} salário{'s' if menor850 != 1 else ''} menor{'es' if menor850 != 1 else ''} que R$ 850,00")
