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
