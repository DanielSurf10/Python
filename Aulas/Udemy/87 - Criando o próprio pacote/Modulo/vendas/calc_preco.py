from formata.preco import real


def aumento(valor, porcentagem, formata=False):
    r = valor * ((porcentagem / 100) + 1)

    if formata:
        return real(valor)
    else:
        return r


def desconto(valor, porcentagem, formata=False):
    r = valor - (valor / 100 * porcentagem)

    if formata:
        return real(valor)
    else:
        return r
