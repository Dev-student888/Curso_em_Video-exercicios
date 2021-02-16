# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o valor 3.
# C) Quais foram os números pares.

t = (int(input('Digite um valor: ')),
     int(input('Digite outro valor: ')),
     int(input('Digite mais um valor: ')),
     int(input('Digite o último valor: ')))

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

if vp:
    print('Os valores pares digitados foram ', end='')

    for num in vp:
        print(f'{num}', end=' ')
else:
    print('Não forão digitados nenhum valor par!')
