# Elabore um programa que conclua o valor a ser pago por um produto,
# considerando o seu preço normal e a condição de pagamento:
#
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - parcelado em até 3x ou mais no cartão: 20% de juros

print('-' * 39)
print('\t\t\tDESAFIO 44')
print('-' * 39)
vp = float(input('Preço das compras: R$'))
r1 = int(input('''FORMAS DE PAGAMENTO:
[ 1 ] - à vista no dinheiro/cheque
[ 2 ] - à vista no cartão
[ 3 ] - 2x no cartão
[ 4 ] - 3x ou mais no cartão
: '''))

if r1 == 1:
    print('Pagando à vista no dinheiro/cheque você tem 10% de desconto!')
    total = vp - vp*10/100
    print('Preço total à pagar: R${:.2f}'.format(total))

elif r1 == 2:
    print('Pagando à vista no cartão você tem 5% de desconto!')
    total = vp - vp*5/100
    print('Preço total à pagar: R${:.2f}'.format(total))

elif r1 == 3:
    r2 = vp / 2
    print('Preço da parcela: R${:.2f}'.format(r2))
    print('Preço total à pagar: R${:.2f}'.format(vp))

elif r1 == 4:
    print('Pagando parcelado em até 3x ou mais você tem um acréscimo de JUROS de 20% !')
    p = int(input('Em quantas parcelas gostaria de pagar? '))
    total = vp + vp*20/100
    r2 = total / p
    print('Preço da parcela: R${:.2f}'.format(r2))
    print('Preço total à pagar: R${:.2f}'.format(total))
else:
    print('Opção inválida! Por favor reinicie o programa e tente novamente!\n')
