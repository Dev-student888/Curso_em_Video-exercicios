# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

pesos = []
for i in range(1, 6):
    p = float(input('Digite o peso(kg) da {}ª pessoa: '.format(i)))
    pesos.append(p)
print('Maior peso: {:.2f} kg'.format(max(pesos)))
print('Menor peso: {:.2f} kg'.format(min(pesos)))
