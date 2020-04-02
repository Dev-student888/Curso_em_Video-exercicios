# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome.

n = str(input('Digite seu nome completo: ')).strip().title()
print('O seu nome tem a palavra \'SILVA\'? {}'.format('Silva' in n))
