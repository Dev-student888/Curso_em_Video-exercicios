# Crie um programa onde o usuário possa digitar 7 valores numéricos
# e cadastre-os em uma lista única que mantenha os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

l = [[], []]
valor = 0

for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor % 2 == 0:
        l[0].append(valor)
    else:
        l[1].append(valor)

l[0].sort()
l[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {l[0]}')
print(f'Os valores ímpares digitados foram: {l[1]}')
