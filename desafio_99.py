# Faça um programa que tenha uma função chamada maior(), que
# recebe vários parâmetros com valores inteiros. Seu programa
# tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(* x):
    print('-=' * 30)
    print('Analisando os valores passados ...')
    for i in x:
        print(i, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(x)} valores ao todo.')
    if len(x) > 0:
        print(f'O maior valor informado foi {max(x)}.')
    else:
        print('O maior valor informado foi 0.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
