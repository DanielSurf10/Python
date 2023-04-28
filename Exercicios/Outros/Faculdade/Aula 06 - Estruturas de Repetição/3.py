# 3- Faça um programa em Python que leia um valor n, inteiro e positivo, calcule e mostre a seguinte soma:
# S = 1 + 1/2 + 1/3 + 1/4 +...+ 1/n

soma = 0
num = int(input("Digite um valor: "))

for i in range(1, num + 1):
    soma += 1 / i

print(soma)