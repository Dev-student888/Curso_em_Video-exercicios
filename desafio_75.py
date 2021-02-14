# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o valor 3.
# C) Quais foram os números pares.

a = int(input('Digite um valor: '))

b = int(input('Digite outro valor: '))

c = int(input('Digite mais um valor: '))

d = int(input('Digite o último valor: '))

t = (a, b, c, d)
print(f'Você digitou os valores {t}')

print(f'O valor 9 apareceu {t.count(9)} vezes')

if 3 in t:
    print(f'O valor 3 apareceu na {t.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

vp = []
ap = 0

for valor in t:
    if valor % 2 == 0:
        ap = vp.append(valor)

print('Os valores pares digitados foram ', end='')

for num in vp:
    print(f'{num}', end=' ')
