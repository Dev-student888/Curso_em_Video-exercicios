# Crie um programa que faça o computador jogar
# Jokenpô (Pedra, Papel e Tesoura) com você!

from random import randint
from time import sleep

print('*'*30, end='\n\t')
print('Pedra, papel e tesoura')
print('*'*30, end='\n\n')

l = ('Pedra', 'Papel', 'Tesoura')
print('Bora jogar!\n')
j = int(input('''OPÇÕES:
[ 1 ] - Pedra
[ 2 ] - Papel
[ 3 ] - Tesoura
: '''))
opj = l[j - 1]
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
c = randint(0, 2)
opc = l[c - 1]

if opj == opc:
    print('EMPATE!')

elif opj == l[0] and opc == l[2] or opj == l[1] and opc == l[0] or opj == l[2] and opc == l[1]:
    print('PARABÉNS! VOCÊ VENCEU!')

else:
    print('SINTO MUITO! VOCÊ PERDEU!')

print('Você: {}'.format(opj))
print('Computador: {}'.format(opc))
