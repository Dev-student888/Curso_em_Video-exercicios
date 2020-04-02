# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
#
# Seu programa deverá realizar
# a operação realizada em cada caso.

from time import sleep
v = int(input('Digite um valor: '))
n = int(input('Digite outro valor: '))
o = 0
while o != 5:
    print('''OPÇÕES:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR 
    [4] NOVOS NÚMEROS 
    [5] SAIR DO PROGRAMA
    ''')
    o = int(input(': '))
    if o == 1:
        s = v + n
        print('A soma entre {} e {} é {}\n'.format(v, n, s))
    elif o == 2:
        m = v * n
        print('A multiplicação entre {} e {} é {}\n'.format(v, n, m))
    elif o == 3:
        maior = max(v, n)
        print('O maior número entre {} e {} é {}\n'.format(v, n, maior))
    elif o == 4:
        v = int(input('\nDigite um valor: '))
        n = int(input('Digite outro valor: '))
    elif o == 5:
        print('Finalizando ...')
        sleep(2)
    else:
        print('Opção Inválida! Por favor tente novamente!\n')
print('Fim do programa! Volte Sempre!\n')
