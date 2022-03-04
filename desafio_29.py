# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite

v = float(input('Digite a velocidade atual do carro(Km/h): '))
if v > 80:
    print('Você foi multado(a)!\nSua velocidade está acima do limite, que é de 80 Km/h!')
    m = (v - 80) * 7.00
    print('Sua multa vai custar R${:.2f}'.format(m))
else:
    print('Tenha um bom dia. Dirija com segurança! \n')
