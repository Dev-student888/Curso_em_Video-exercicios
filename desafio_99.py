# Faça um programa que tenha uma função chamada maior(), que
# recebe vários parâmetros com valores inteiros. Seu programa
# tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* x):
    print(f'Dos números {x} o maior é {max(x)}')


maior(2, 3, 5, 6, 7, 9, 10, 23, 45)
