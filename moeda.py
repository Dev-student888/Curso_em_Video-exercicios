# Este arquivo faz parte dos Exercícios 107, 108, 109 e 110!

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
    y = x * 2
    if m is False:
        return y
    else:
        return moeda(y)


def metade(x, m=False):
    y = x / 2
    if m is False:
        return y
    else:
        return moeda(y)


def moeda(x):
    return f'R${x:.2f}'.replace('.', ',')  # Preste atenção no método REPLACE


def resumo(x, aum=10, red=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(x)}')
    print(f'Dobro do preço: \t{dobro(x, True)}')
    print(f'Metade do preço: \t{metade(x, True)}')
    print(f'{aum}% de aumento: \t{aumentar(x, aum, True)}')
    print(f'{red}% de redução: \t{diminuir(x, red, True)}')
    print('-' * 30)
