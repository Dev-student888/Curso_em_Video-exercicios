# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

from datetime import date
nasc = 0
t = date.today().year
idade = 0
nm = 0
cont_m = 0
i = 0
for i in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    idade = t - nasc
    nm = i - cont_m
    if nasc > t:
        print('Houve algum ERRO! Por favor reinicie seu programa!')
    elif idade >= 18:
        cont_m += 1

print('De {} concorrentes, os que já atingiram a maioridade foram {}'.format(i, cont_m))
print('E os que não atingiram a maioridade foram {}'.format(nm))
