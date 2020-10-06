# Escreva um programa que leia um número n inteiro qualquer e mostre na tela
# os n primeiros elementos de uma sequência de fibonacci.
# Ex:
#
# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

print('-'*30)
print('Sequência de Fibonacci ')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {} '.format(t1, t2), end='')
c = 3
while c <= n:
    s = t1 + t2
    print('-> {} '.format(s), end='')
    t1 = t2
    t2 = s
    c += 1
print('-> FIM!')
print('~'*30)
