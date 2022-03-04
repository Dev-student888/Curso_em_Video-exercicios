# Faça um programa que leia 5 valores numéricos guarde-os em uma lista.
# No final mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.

l = list()

for i in range(5):
    l.append(int(input(f'Digite um valor para self Posição {i}: ')))
print('=-' * 30)
print(f'Você digitou os valores {l}')
print(f'O maior valor digitado foi {max(l)} nas posições ', end='')
for pos, v in enumerate(l):
    if v == max(l):
        print(f'{pos}... ', end='')
print(f'\nO menor valor digitado foi {min(l)} nas posições ', end='')
for pos, v in enumerate(l):
    if v == min(l):
        print(f'{pos}... ', end='')
