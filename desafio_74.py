# Crie um programa que vai gerar cinco números aleatórios e colocar em uma
# tupla. Depois disso, mostre a listagem de números gerados e também indique o
# menor e o maior valor que estão na tupla.

from random import randint

x = randint(0, 10)

y = randint(0, 10)

z = randint(0, 10)

c = randint(0, 10)

s = randint(0, 10)

t = (x, y, z, c, s)

print(f'Os valores sorteados foram: {t}')
print(f'O maior valor sorteado foi {max(t)}')
print(f'O menor valor sorteado foi {min(t)}')
