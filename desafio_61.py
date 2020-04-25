# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando
# os 10 primeiros termos da progressão usando a estrutura while.

nt = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão desta PA: '))
i = 1
print('Termos da PA:\n')
print('PA: {} ->'.format(nt), end='')
while i < 10:
    nt += r
    print(' {} '.format(nt), end='')
    print('->' if i < 9 else '', end='')
    i += 1
print('\n')
