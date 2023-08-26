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
