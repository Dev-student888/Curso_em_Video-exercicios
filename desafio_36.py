# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. O programa vai perguntar o
# valor da casa, o salário do comprador e em quantos anos
# ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ele não
# pode exceder 30% do salário ou então o empréstimo será negado.

vc = float(input('Qual o valor da casa que você quer comprar?\nR$'))
sc = float(input('Qual é o seu salário?\nR$'))
a = int(input('Em quantas prestações você pretende pagar a casa?\nPrestações: '))
p = vc / (a * 12)
minimo = sc * 30 / 100
if p <= minimo:
    print('A prestação será de R${:.2f}'.format(p))
else:
    print('Sinto Muito!\nInfelizmente não há como você financiar este imóvel!')
    print('Empréstimo Negado!')
