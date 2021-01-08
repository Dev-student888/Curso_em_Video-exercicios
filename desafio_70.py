# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
#
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

print('-'*35)
print('\t\tLOJA SUPER BARATÃO')
print('-'*35)
tot = 0
pm1000 = 0
pp = []
a = 0
np = []
li = 0
n_pos = 0
pb = 0
while True:
    n = str(input('Nome do Produto: '))
    p = float(input('Preço: R$'))
    tot += p
    if p > 1000:
        pm1000 += 1
    a = pp.append(p)
    li = np.append(n)
    pb = min(pp)
    r = str(input('Quer continuar? [S/N] ')).upper()
    n_pos = pp.index(pb)
    while r not in 'SN':
        print('Dados inválidos. Por favor digite a sua resposta novamente!')
        r = str(input('Quer continuar? [S/N] ')).upper()
    if r == 'S':
        continue
    else:
        break
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {pm1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {np[n_pos]} que custa R${pb:.2f}')
