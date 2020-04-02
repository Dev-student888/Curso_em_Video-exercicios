print('=' * 36, 'DESAFIO 13', '=' * 36)
p = float(input('Digite o preço de um produto: '))
pv = p - p * 10/100
pp = p + p * 8/100
print('Este produto à vista tem 10% de desconto, passando a custar R${:.2f}'.format(pv))
print('Este produto à prazo tem um acréscimo de 8%, passando a custar R${:.2f}'.format(pp))
print('=' * 84)
