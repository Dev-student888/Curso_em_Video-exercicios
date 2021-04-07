# Este arquivo faz parte do Exercício 109!

def aumentar(x, perc, m=False):
    y = x + x * perc / 100
    if m is False:
        return y
    else:
        return moeda(y)


def diminuir(x, perc, m=False):
    y = x - x * perc / 100
    if m is False:
        return y
    else:
        return moeda(y)


def dobro(x, m=False):
    if m is False:
        return x * 2
    else:
        return moeda(x * 2)


def metade(x, m=False):
    if m is False:
        return x / 2
    else:
        return moeda(x / 2)


def moeda(x):
    return f'R${x:.2f}'
