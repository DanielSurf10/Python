
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
