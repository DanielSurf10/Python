import re
import random

# Variáveis
valores = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


# Função de remover os ".", "-" e "/"
def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


# Imprime uma sequência de "-" ou "=" na tela
def linha():
    print('-' * 30)


# Imprime o cabeçalho na tela
def cabecalho():
    linha()
    print(" Valide ".center(30, '='))
    print(" seu ".center(30, '-'))
    print(" cnpj ".center(30, '='))
    linha()


# Pegar valor do cnpj
def pega_cnpj():
    cnpj = input('Infome seu cnpj: ')
    return cnpj


# Validar cnpj
def valida_cnpj(cnpj):
    cnpj = remover_caracteres(cnpj)

    if cnpj_sequencia(cnpj):
        return False

    # Primeiro digito
    primeiro_digito = calcula_digito(cnpj, 1)

    # Segundo digito
    segundo_digito = calcula_digito(cnpj, 2)

    # Verificação dos digitos
    verificacao = True if cnpj[-2:] == str(primeiro_digito) + str(segundo_digito) else False

    return verificacao


# Verfica se é um sequência
def cnpj_sequencia(cnpj):
    return cnpj == cnpj[0] * len(cnpj)


# Calcula os digitos
def calcula_digito(cnpj, digito):
    validar = zip(cnpj[:-2 + digito - 1], valores[1 if digito == 1 else 0:])
    soma_cnpj = sum([int(a) * int(b) for a, b in validar])
    digito = 11 - (soma_cnpj % 11)
    digito = digito if digito < 10 else 0

    return digito


# Gerar cnpj
def gerar_cnpj(formatar=False):
    bloco1 = str(random.randint(0, 99)).center(2, '0')
    bloco2 = str(random.randint(100, 999))
    bloco3 = str(random.randint(100, 999))
    bloco4 = '0001'
    cnpj_metade = f'{bloco1}{bloco2}{bloco3}{bloco4}'

    digito1 = str(calcula_digito(cnpj_metade + '00', 1))
    digito2 = str(calcula_digito(cnpj_metade + digito1 + '0', 2))

    bloco5 = f"{bloco1}{bloco2}{bloco3}{bloco4}{digito1}{digito2}"

    return bloco5
