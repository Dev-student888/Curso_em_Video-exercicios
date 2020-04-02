# Crie um programa que leia duas notas de um aluno
# e calcule a sua média, mostrando uma mensagem no
# final de acordo com a média atingida:
#
# - Média abaixo de 5.0:
# REPROVADO
# - Média entre 5.0 e 6.9:
# RECUPERAÇÃO
# - Média 7.0 ou superior:
# APROVADO

r = str(input('Qual o seu gênero? ')).lower().strip()
s1 = 0
s2 = 0
if r == 'masculino':
    s1 = 'e'
    s2 = 'O'
elif r == 'feminino':
    s1 = 'a'
    s2 = 'A'
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Com as notas {} e {} a média dest{} estudante é de {} pontos.'.format(n1, n2, s1, m))
    print('{} estudante está REPROVAD{}.'.format(s2, s2))
elif 5.0 <= m < 6.9:
    print('Com as notas {} e {} a média dest{} estudante é de {} pontos.'.format(n1, n2, s1, m))
    print('O(A) estudante está de RECUPERAÇÃO.')
elif m >= 7.0:
    print('Com as notas {} e {} a média dest{} estudante é de {} pontos.'.format(n1, n2, s1, m))
    print('{} estudante está APROVAD{}.'.format(s2, s2))
