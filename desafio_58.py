# Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número de 0 a 10.
# Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

from random import randint
from playsound import playsound as play

c = randint(0, 10)
print('Olá! Sou seu computador!')
print('Vamos jogar um jogo?\nAcabei de pensar em um número entre 0 e 10.\n')
acertou = False
palpites = 0
while not acertou:
    u = int(input('Em qual número pensei? '))
    if u == c:
        acertou = True
        play('./acertou_miseravi.mp3')
    else:
        play('./faustao-errou.mp3')
        if u < c:
            print('Mais... Tente novamente!\n')
        else:
            print('Menos... Tente novamente!\n')
        palpites += 1
print('Você precisou de {} tentativa(s) até acertar!\n'.format(palpites))
