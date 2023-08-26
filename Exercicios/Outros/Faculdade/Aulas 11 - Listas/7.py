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
