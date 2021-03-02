# Faça um programa que leia nome e peso de várias pessoas, guardando
# tudo em uma lista. No final, mostre:
#
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
dado = list()
MP = mP = 0
nM = list()
nm = list()

r = 'S'
while r in 'Ss':
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    r = str(input('Quer continuar? [S/N] ')).strip()[0]
    while r not in 'SsNn':
        print('\nErro! Por favor tente novamente!')
        print('Obs.: Por favor digite apenas \'S\' ou \'N\'!')
        r = str(input('Quer continuar? [S/N] ')).strip()[0]

print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
for p in pessoas:
    if p[1] > MP:
        MP = p[1]
        nM.append(p[0])
    else:
        mP = p[1]
        nm.append(p[0])
print(f'O maior peso foi de {MP}Kg. Peso de {nM[-1]}')
print(f'O menor peso foi de {mP}Kg. Peso de {nm[-1]}')
