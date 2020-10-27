# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
#
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

pmais18 = 0
h = 0
Mmenos20 = 0
while True:
    print('-' * 25)
    print('\tCADASTRE UMA PESSOA ')
    print('-' * 25)
    i = int(input('Idade: '))
    s = str(input('Sexo: [M/F] ')).upper()
    while s not in 'MF':
        s = str(input('Sexo: [M/F] ')).upper()
    print('-'*25)
    if i > 18:
        pmais18 += 1
    if s == 'M':
        h += 1
    if i < 20 and s == 'F':
        Mmenos20 += 1
    r = str(input('Quer continuar? [S/N] ')).upper()
    while r not in 'SN':
        print('Dado incorreto! Por favor digite novamente sua resposta!\n')
        r = str(input('Quer continuar? [S/N] ')).upper()
    if r == 'S':
        continue
    else:
        break
print('='*6, end='')
print(' FIM DO PROGRAMA ', end='')
print('='*6)
print(f'Total de pessoas com mais de 18 anos: {pmais18}')
print(f'Ao todo temos {h} homens cadastrados.')
print(f'E temos {Mmenos20} mulheres com menos de 20 anos.')
