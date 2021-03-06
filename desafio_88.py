# Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites. O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo
# em uma lista composta.

from random import randint
l = list()

j = int(input('Quantos jogos você quer gerar? '))
for u in range(0, j):
    l.append([])

for i in range(1, j + 1):
    print(f'Resultado do {i}º jogo: ')

print(l)
