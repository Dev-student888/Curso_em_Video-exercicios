# Crie um programa que vai ler vários números e coloca-los em uma
# lista. Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

l = list()
par = list()
impar = list()

r = 'S'
while r == 'S':
    l.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
if r not in 'SN':
    print('Erro! Por favor tente novamente!')
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

print('=-'*30)

for i in l:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'Lista: {l}')
print(f'Números PARES: {par}')
print(f'Númros ÍMPARES: {impar}')
