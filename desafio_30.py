# Crie um programa que leia um número
# na tela e diga se ele é PAR ou ÍMPAR

n = int(input('Digite um número: '))

if n % 2 == 0:
    print('Este número é PAR')
else:
    print('Este número é ÍMPAR')

'''if n % 2 == 1:
    print('O número {} é ÍMPAR!'.format(n))
else:
    print('O número {} é PAR!'.format(n))'''
