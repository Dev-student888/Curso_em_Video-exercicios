# Crie um programa que leia o nome completo de uma pessoa e mostre:
#  - O nome com todas as letras maiúsculas e minúsculas.
#  - Quantas letras ao todo (sem considerar espaços).
#  - Quantas letras tem o primeiro nome.

n = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas é {}'.format(n.upper()))
print('Seu nome em letras minúsculas é {}'.format(n.lower()))
# print('Seu nome ao todo possui {} letras'.format(len(n) - n.count(' ')))
# print('Seu primeiro nome possui {} letras'.format(n.find(' ')))
p = n.split()
print('Seu nome ao todo possui {} letras'.format(len(''.join(p))))
print('Seu primeiro nome é {} e ele possui {} letras'.format(p[0], len(p[0])))
