# Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites. O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo
# em uma lista composta.

from random import randint
from time import sleep
l = list()
e = 0
print('-' * 30)
print(f'{"JOGO NA MEGA SENA":^30}')
print('-' * 30)

j = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(0, j):
    l.append([randint(1, 60), randint(1, 60), randint(1, 60),
              randint(1, 60), randint(1, 60), randint(1, 60)])

print('-=' * 6, f' SORTEANDO {j} JOGOS ', '-=' * 6)
for i in range(1, j + 1):
    print(f'Resultado do {i}º jogo: {l[i - 1]}')
    sleep(1)
