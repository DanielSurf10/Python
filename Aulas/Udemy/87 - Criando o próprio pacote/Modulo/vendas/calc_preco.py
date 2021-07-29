from vendas.formata.preco import real


def aumento(valor, porcentagem, formata=False):
    r = valor + (porcentagem / 100 * valor)

    if formata:
        return real(r)
    else:
        return r


def desconto(valor, porcentagem, formata=False):
    r = valor - (valor / 100 * porcentagem)

    if formata:
        return real(r)
    else:
        return r
