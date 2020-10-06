# Crie um programa que leia vários números inteiros pelo teclado. No final da
# execução, mostre a média entre todos os valores e qual foi o maior e
# o menor valores lidos. O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar valores.

c = 1
n = int(input('Digite um número inteiro: '))
tot = n
v = []
a = v.append(n)
while True:
    r = str(input('Quer continuar [S/N]? ')).lower()
    while r in 'Ss':
        n = int(input('Digite um número inteiro: '))
        c += 1
        tot += n
        a = v.append(n)
        r = str(input('Quer continuar [S/N]? '))
    break
m = tot/c
print('Você digitou {} números ao total.'.format(c))
print('A média entre todos os valores é {}'.format(m))
print('O maior valor digitado foi {} e o menor foi {}'.format(max(v), min(v)))
