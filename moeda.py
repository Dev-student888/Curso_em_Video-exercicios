# Faz parte dos Exercícios 107 e 108!

def aumentar(x, perc):
    y = x + x * perc/100
    return y


def diminuir(x, perc):
    y = x - x * perc/100
    return y


def dobro(x):
    return x * 2


def metade(x):
    return x / 2


def moeda(x):
    return f'R${x:.2f}'
