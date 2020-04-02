# O mesmo professor do desafio 019 quer sortear a
# ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro
# alunos e mostre a ordem sorteada.

from random import shuffle  # shuffle significa embaralhar

a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
o = [a, b, c, d]
shuffle(o)
print('A ordem de apresentação dos trabalhos é \n{}'.format(o))
