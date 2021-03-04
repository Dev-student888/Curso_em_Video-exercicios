# Faça um programa que leia nome e peso de várias pessoas, guardando
# tudo em uma lista. No final, mostre:
#
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
dados = list()
mai = men = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = ''
    while not r:
        r = str(input('Quer continuar? [S/N] ')).strip()[0]
    if r in 'Ss':
        continue
    while r not in 'SsNn':
        print('Erro! Por favor tente novamente!')
        print('Para a pergunta a seguir digite apenas \'S\' ou \'N\'!')
        r = str(input('Quer continuar? [S/N] ')).strip()[0]
    if r in 'Nn':
        break
print('-='*30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {mai} Kg. Peso de ', end='')
for i in pessoas:
    if i[1] == mai:
        print(f'[{i[0]}] ', end='')
print()
print(f'O menor peso foi de {men} Kg. Peso de ', end='')
for i in pessoas:
    if i[1] == men:
        print(f'[{i[0]}] ', end='')
