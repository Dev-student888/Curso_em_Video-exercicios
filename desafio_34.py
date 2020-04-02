# Escreva um programa que pergunte o salário de um funcionário e calcule o valor
# do seu aumento.
# Para salários superiores a R$1.250,00 , calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sf = float(input('Digite o salário de um funcionário: R$'))

if sf > 1250.00:
    sf = sf + sf * 10 / 100
    print('O novo salário deste funcionário com 10% de aumento será de R${:.2f}'.format(sf))
else:
    sf = sf + sf*15/100
    print('O novo salário deste funcionário com 15% de aumento será de R${:.2f}'.format(sf))
