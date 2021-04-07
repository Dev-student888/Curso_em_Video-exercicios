# Crie um módulo chamado moeda.py que tenha as funções
# incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas
# funções.

from moeda import aumentar, diminuir, dobro, metade

p = float(input('Digite o preço: R$'))
print(f'A metade de {int(p)} é R${metade(p):.2f}')
print(f'O dobro de {int(p)} é R${dobro(p):.2f}')
print(f'Aumentando 10%, temos R${aumentar(p, 10):.2f}')
print(f'Reduzindo 13%, temos R${diminuir(p, 13):.2f}')
