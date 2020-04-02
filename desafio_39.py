# Faça um programa que leia o ano de nascimento
# de um jovem e informe, de acordo com sua idade:
#
# - Se ele ainda vai se alistar no serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
#
# Seu programa também deverá mostrar o tempo que falta
# ou que passou do prazo.

from datetime import date
y = date.today().year
n = int(input('Em que ano você nasceu? '))
idade = y - n
sexo = str(input('Qual é o seu sexo? ')).lower().strip()
if 'masculino' in sexo:
    if idade < 18:
        print('Você nasceu em {} e está com {} anos!'.format(n, idade))
        print('Faltam {} anos para você se alistar!'.format(18 - idade))
    elif idade == 17:
        print('Você nasceu em {} e está com {} anos!'.format(n, idade))
        print('Falta 1 ano para você se alistar!')
    elif idade == 18:
        print('Você nasceu em {} e está com {} anos!'.format(n, idade))
        print('Já está na hora de você se alistar!')
    elif idade == 19:
        print('Você nasceu em {} e está com {} anos!'.format(n, idade))
        print('Já passou do tempo de você ir se alistar!')
        print('Você deveria ter se alistado a {} ano atrás,'.format(idade - 18))
        print('ou seja, no ano de {}!'.format(y - 1))
    else:
        print('Você nasceu em {} e está com {} anos!'.format(n, idade))
        print('Já passou do tempo de você ir se alistar!')
        print('Você deveria ter se alistado a {} anos atrás,'.format(idade - 18))
        print('ou seja, no ano de {}!'.format(y - (idade - 18)))
else:
    print('Você não precisa fazer o alistamento militar!')
