# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.

n = int(input('Digite um número de 0 a 9999: '))

u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Analisando o número {}'.format(n))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

# n = str(input('Digite um número de 0 a 9999: ')).zfill(4)
# print('Unidade: {}'.format(n[3]))
# print('Dezena: {}'.format(n[2]))
# print('Centena: {}'.format(n[1]))
# print('Milhar: {}'.format(n[0]))

# n = str(input('Digite um número de 0 a 9999: '))
# if len(n) == 4:
    # print('Unidade: {}'.format(n[3]))
    # print('Dezena: {}'.format(n[2]))
    # print('Centena: {}'.format(n[1]))
    # print('Milhar: {}'.format(n[0]))

# elif len(n) == 3:
    # print('Unidade: {}'.format(n[2]))
    # print('Dezena: {}'.format(n[1]))
    # print('Centena: {}'.format(n[0]))

# elif len(n) == 2:
    # print('Unidade: {}'.format(n[1]))
    # print('Dezena: {}'.format(n[0]))

# else:
    # print('Unidade: {}'.format(n[0]))
