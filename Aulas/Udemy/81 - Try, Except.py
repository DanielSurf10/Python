try:
    a = 1/0
    print(a)
except NameError as erro:
    print('erro de nome')
except (KeyError, IndexError) as erro:
    print('erro de indice')
except ZeroDivisionError as erro:
    print("erro de divisão de zero")
else:
    print("sem erro")
finally:
    print('acabou')

