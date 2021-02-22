# Faça um programa que leia 5 valores numéricos guarde-os em uma lista.
# No final mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.

l = list()

for i in range(5):
    l.append(int(input(f'Digite um valor para a Posição {i}: ')))
print('=-' * 30)
print(f'Você digitou os valores {l}')
pos_max = list()
if l.count(max(l)) >= 1:
    for p in range(l.count(max(l)) + 1):
        pos_max.append(l.index(max(l)))
print(f'O maior valor digitado foi {max(l)} nas posições ', end='')
for v in pos_max:
    print(f'{v}... ', end='')
pos_min = list()
if l.count(min(l)) >= 1:
    for p in range(l.count(min(l)) + 1):
        pos_min.append(l.index(min(l)))
print(f'\nO menor valor digitado foi {min(l)} nas posições ', end='')
for v in pos_min:
    print(f'{v}... ', end='')
