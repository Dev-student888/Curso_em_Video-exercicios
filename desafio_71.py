# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
#
# OBS.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

def title(x):
    print('='*x)
    print(' '*int(x/3), end='')
    print('BANCO CEV')
    print('='*x)


def eq(y):
    print('='*y)


title(30)
v = int(input('Qual valor você quer sacar? '))
total = v
c = 50
tc = 0
while True:
    if total >= c:
        total -= c
        tc += 1
    else:
        if tc > 0:
            print(f'Total de {tc} cédulas de R${c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        tc = 0
        if total == 0:
            break
eq(30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
