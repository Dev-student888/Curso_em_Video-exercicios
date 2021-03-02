# Crie um programa onde o usuário possa digitar 7 valores numéricos
# e cadastre-os em uma lista única que mantenha os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

l = list()
for i in range(1, 8):
    l.append(int(input(f'Digite o {i}º valor: ')))

print('-='*30)
l.sort()
print('Os valores pares digitados foram: [ ', end='')
for p in l:
    if p % 2 == 0:
        print(f'{p}', end=' ')
print(']\nOs valores ímpares digitados foram: [ ', end='')
for p in l:
    if p % 2 == 1:
        print(f'{p}', end=' ')
print(']')
