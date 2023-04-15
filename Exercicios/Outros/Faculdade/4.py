# 4- Escreva um algoritmo que leia um grupo de valores reais e determine quantos valores
# são positivos e quantos são negativos. Determine, também, qual é o menor desses
# valores. Utilize o comando de repetição que desejar.

menor = float("inf")
positivo = 0
negativo = 0

print("Digite 5 valores")

for i in range(1, 6):
    valor = float(input(f"Digite o {i}º valor: "))

    if valor >= 0:
        positivo += 1
    else:
        negativo += 1
    
    if valor < menor:
        menor = valor


print(f"Foram {positivo} números positivos, {negativo} negativos e o menor foi o {menor}")
