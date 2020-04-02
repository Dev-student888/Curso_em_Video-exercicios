# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número inteiro: '))
totvd = 0
for i in range(1, n + 1):  # laço i no intervalo(1, n + 1)
    if n % i == 0:  # Mostra os valores pelos quais o n é divisível
        print('\033[32m', end=' ')  # Mostra os valores coloridos na tela
        totvd += 1  # Mostra quantas vezes o n pode ser dividido (contador) dentro do laço
    else:  # Mostra os valores pelos quais o n não é divisível
        print('\033[31m', end=' ')
    print(i, end=' ')  # Mostra os valores em que o n pode e não pode ser divisível
print('\n\033[mO número {} é divisível {} vezes!'.format(n, totvd))
if totvd == 2:
    print('Este número É PRIMO!')
else:
    print('Este número NÃO É PRIMO!')
