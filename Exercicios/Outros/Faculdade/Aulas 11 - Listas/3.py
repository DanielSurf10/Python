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
