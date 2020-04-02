# Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número de 0 a 10.
# Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

from random import randint
from playsound import playsound as play
from time import sleep

print('Vamos jogar um jogo!\nAcabei de pensar em um número entre 0 e 10.\n')
c = randint(0, 10)
u = int(input('Em qual número pensei? '))
while u:
    if u != c:
        print('\nAnalisando resposta ...')
        sleep(3)
        print('Errou!\n', end='')
        play('./faustao-errou.mp3')
        print('Você: {}'.format(u))
        print('Computador: {}'.format(c))
        r = str(input('Gostaria de tentar novamente? [S/N] '))
        if r in 'Ss':
            u = int(input('Em qual número pensei? '))
        elif r in 'Nn':
            exit()
        else:
            print('Opção Inválida! Por favor reinicie o programa!\n')
            exit()
    else:
        print('\nAnalisando resposta ...')
        sleep(3)
        print('PARABÉNS! VOCÊ ACERTOU!\n', end='')
        play('./acertou_miseravi.mp3')
        print('Você: {}'.format(u))
        print('Computador: {}'.format(c))
        exit()
