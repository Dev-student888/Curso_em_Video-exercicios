# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais
# alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

t = int(input('Digite o 1° termo de uma PA: '))
r = int(input('Digite sua razão: '))
u = 10
c = 0
tot = 0
print('PA: ', end='')
while u != 0:
    while c < u:
        print('{} '.format(t), end='')
        print('=> ' if c < u else '', end='')
        t += r
        c += 1
        tot += 1
    print('PAUSA\n')
    c = 0
    u = int(input('Gostaria de ver quantos termos a mais? '))
print('FIM!\n')
print('Ao total você visualizou {} termos!\n'.format(tot))
