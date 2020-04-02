# Faça um programa que leia um ano qualquer e diga se ele é BISSEXTO.
from datetime import date

a = int(input('Digite o ano que você quer analisar(Digite 0 se quiser analisar o ano atual): '))
if a == 0:
    a = date.today().year
if a % 400 == 0 or a % 4 == 0 and a % 100 != 0:
    print('O ano {} é BISSEXTO!\n'.format(a))
else:
    print('O ano {} NÃO É BISSEXTO!\n'.format(a))
