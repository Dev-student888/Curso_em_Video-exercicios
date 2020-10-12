# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total
# de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
c = 0
while True:
    n = int(input('Digite um valor: '))
    r = str(input('Par ou Ímpar? [P/I] ')).upper()
    comp = randint(0, 10)
    s = n + comp
    if r in 'PI':
        print('-'*30)
        print(f'Você jogou {n} e o computador {comp}.', end='')
        pi = ''
        if s % 2 == 0 and r == 'P' or s % 2 == 1 and r == 'I':
            if r == 'P':
                pi = 'PAR'
            else:
                pi = 'ÍMPAR'
            print(f'Total de {s} DEU {pi}! ')
            print('-'*30)
            print('Você VENCEU!')
            c += 1
            print('Vamos jogar novamente...')
        if s % 2 == 1 and r == 'P' or s % 2 == 0 and r == 'I':
            if r == 'P':
                pi = 'ÍMPAR'
            else:
                pi = 'PAR'
            print(f' Total de {s} DEU {pi}! ')
            print('-'*30)
            print('Você PERDEU!')
            break

    if r not in 'PI':
        print('Dado incorreto! Por favor digite novamente sua resposta!\n')

print('=-'*15)
print(f'GAME OVER! Você venceu {c} vezes.')
