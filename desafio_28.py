# Escreva um programa que faça o computador
# "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário
# venceu ou perdeu

from random import randint
from playsound import playsound as play
from time import sleep

num = randint(0, 5)
print('Pensei em um número entre 0 e 5.')
nu = int(input('Tente descobrir em qual número eu pensei!\nDigite um número inteiro: '))
print('PROCESSANDO ...')
sleep(5)
if nu == num:
    print('PARABÉNS! VOCÊ DESCOBRIU!')
    play('./acertou_miseravi.mp3')
    print('VOCÊ: {}'.format(nu))
    print('COMPUTADOR: {}'.format(num))
else:
    print('Sinto muito! Tente outra vez!')
    print('VOCÊ: {}'.format(nu))
    print('COMPUTADOR: {}'.format(num))
    play('./faustao-errou.mp3')
