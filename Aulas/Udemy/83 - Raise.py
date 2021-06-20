def divide(a, b):
    if b == 0:
        raise
    return a / b


def divide2(a, b):
    if b == 0:
        raise ZeroDivisionError("Nunca dividiras por zero.")


print(divide(5, 2))
print(divide2(2, 0))
