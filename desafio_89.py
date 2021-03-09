# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.

l = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('1ª Nota: '))
    n2 = float(input('2ª Nota: '))
    média = (n1 + n2) / 2
    l.append([nome, [n1, n2], média])
    r = str(input('Quer continuar? [S/N] ')).strip()[0]
    if r in 'Ss':
        continue
    while r not in 'SsNn':
        print('Erro! Por favor tente novamente!')
        print('Por favor digite apenas \'S\' ou \'N\'!')
        r = str(input('Quer continuar? [S/N] ')).strip()[0]
    else:
        break
print('-=' * 30)
print(f'{"Nº":<4}|{"NOME":<10}|{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(l):
    print(f'{i:<4}|{a[0]:<10}|{a[2]:>8.1f}')
print('-' * 26)
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(l) - 1:
        print(f'Notas de {l[opc][0]} são {l[opc][1]}')
print('<<<< VOLTE SEMPRE >>>>')
