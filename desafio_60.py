# Faça um programa que leia um número qualquer e mostre o seu fatorial.
#
# Ex:
#
# 5! = 5x4x3x2x1 = 120

# EXEMPLO 1:

# from math import factorial
# n = int(input('Digite um número: '))
# f = factorial(n)
# print('O Fatorial de {} é {}'.format(n, f))

# EXEMPLO 2:

n = int(input('Digite um número: '))
c = n
fat = 1
print('{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print('x' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
print('{}'.format(fat))
