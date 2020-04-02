# A Confederação Nacional de Natação precisa
# de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo
# com a idade:
#
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import date
print('-' * 55)
print('\t\tConfederação Nacional de Natação: \n')
nasc = int(input('Digite o ano de nascimento de um atleta: '))
y = date.today().year
idade = y - nasc
print('Este atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Este atleta faz parte da categoria MIRIM')
elif idade <= 14:
    print('Este atleta faz parte da categoria INFANTIL')
elif idade <= 19:
    print('Este atleta faz parte da categoria JUNIOR')
elif idade <= 25:
    print('Este atleta faz parte da categoria SÊNIOR')
else:
    print('Este atleta faz parte da categoria MASTER')
print('-' * 55)
