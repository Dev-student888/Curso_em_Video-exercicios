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
    return f'R${x:.2f}'.replace('.', ',')  # Preste atenção no método REPLACE


def resumo(x, aum, red):
    print('-' * 32)
    print('        RESUMO DO VALOR')
    print('-' * 32)
    print(f'Preço analisado:    {moeda(x)}')
    print(f'Dobro do preço:     {dobro(x, True)}')
    print(f'Metade do preço:    {metade(x, True)}')
    print(f'{aum}% de aumento:     {aumentar(x, aum, True)}')
    print(f'{red}% de redução:     {diminuir(x, red, True)}')
    print('-' * 32)
