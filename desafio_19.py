from random import choice  # choice significa escolha
a = input('Digite o nome do 1º aluno: ')
b = input('Digite o nome do 2º aluno: ')
c = input('Digite o nome do 3º aluno: ')
d = input('Digite o nome do 4º aluno: ')
q = [a, b, c, d]
print('Lista de alunos: {}'.format(q))
print('Sorteando quem vai apagar o quadro ...')
print('O sorteado que apagará o quadro é {}.'.format(choice(q)))
