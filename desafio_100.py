# Faça um programa que tenha uma lista chamada números e
# duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a
# segunda função vai mostrar a SOMA entre todos os valores pares
# sorteados pela função anterior.
from random import randint
from time import sleep

números = list()


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        números.append(randint(0, 10))

    for i in números:
        print(i, end=' ')
        sleep(0.5)
    print('PRONTO!')


def somapar():
    s = 0
    for i in números:
        if i % 2 == 0:
            s += i
    print(f'Somando os valores pares de {números}, temos {s}')


sorteia()
somapar()
