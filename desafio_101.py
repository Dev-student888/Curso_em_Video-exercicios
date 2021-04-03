# Crie um programa que tenha uma função voto() que vai
# receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa
# tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

from time import localtime


def voto():
    a = localtime().tm_year
    print('-' * 30)
    n = int(input('Em que ano você nasceu? '))
    idade = a - n
    if 65 > idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    elif 18 > idade >= 16 or idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    elif 0 > idade < 16:
        print(f'Com {idade} anos: NÃO VOTA.')


voto()
