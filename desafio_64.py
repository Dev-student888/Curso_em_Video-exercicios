# Crie um programa que leia vários números inteiros pelo teclado. O programa
# só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag, ou seja, o valor 999).

while True:
    n = int(input('Digite um número inteiro [999 para parar]: '))
    s = 0
    tot = 0
    while n != 999:
        s += n
        tot += 1
        n = int(input('Digite outro número inteiro [999 para parar]: '))
    print('\nAo total você digitou {} números inteiros e a soma de todos eles é {}.'.format(tot, s))
    break
