# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.

d = float(input('Digite a distância da sua viagem: '))

# if d <= 200:
#     print('Sua passagem custará R${:.2f}'.format(0.50 * d))
# else:
#     print('Sua passagem custará R${:.2f}'.format(0.45 * d))

price = d * 0.50 if d <= 200 else d * 0.45
print('Sua passagem custará R${:.2f}'.format(price))
