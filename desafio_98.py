# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo e realize
# a contagem. Seu programa tem que realizar três contagens
# através da função criada:
#
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada
from time import sleep


def contador(início, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    if início > fim:
        passo *= -1
        fim -= 1
    if fim > início:
        fim += 1
    print('-=' * 30)
    if início > fim and passo < 0:
        print(f'Contagem de {início} até {fim + 1} de {passo * -1} em {passo * -1}', flush=True)
    elif fim > início:
        print(f'Contagem de {início} até {fim - 1} de {passo} em {passo}', flush=True)
    for i in range(início, fim, passo):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
