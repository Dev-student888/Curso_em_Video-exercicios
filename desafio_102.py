# Crie um programa que tenha uma função fatorial() que
# receba dois parâmetros: o primeiro que indique o número a
# calcular e o outro chamado show(), que será um valor lógico
# [opcional] indicando se será mostrado ou não na tela
# o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    print('-' * 30)
    if show is False:
        f = 1
        for i in range(n, 0, -1):
            f *= i
        return f
    else:
        f = 1
        for i in range(n, 0, -1):
            f *= i
            print(str(i) + ' x ' if i >= 2 else str(i) + ' = ', end='')
        return f


print(fatorial(5))
print(fatorial(5, True))
print()
help(fatorial)
