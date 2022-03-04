# Crie um programa que leia nome, idade e sexo de várias
# pessoas, guardando os dado de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
#
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média

pessoa = dict()
ficha = list()
idade = media = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    while pessoa['sexo'] not in 'MmFf':
        print('Erro! Por favor tente novamente!')
        print('Por favor digite apenas \'M\' ou \'F\'!')
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip()[0]
    ficha.append(pessoa.copy())
    pessoa.clear()
    r = str(input('Quer continuar? [S/N] ')).strip()[0]
    while r not in 'SsNn':
        print('Erro! Por favor tente novamente!')
        print('Por favor digite apenas \'S\' ou \'N\'!')
        r = str(input('Quer continuar? [S/N] ')).strip()[0]
    if r in 'Nn':
        break
print('-=' * 30)
print(f'A) Ao total foram cadastradas {len(ficha)} pessoas.')
for e in ficha:
    idade += e['idade']
    media = idade / len(ficha)
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for e in ficha:
    if e['sexo'] in 'Ff':
        print(f'{e["nome"]}', end=' ')
print('\nD) Lista das pessoas que estão acima da média: ')
for e in ficha:
    if e['idade'] > media:
        print('\t', end='')
        for k, v in e.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
