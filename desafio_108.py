# Adapte o desafio 107, criando uma função adicional chamada moeda()
# que consiga mostrar os valores como um valor monetário formatado.

from moeda import metade, dobro, aumentar, moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando 10%, temos {moeda(aumentar(p, 10))}')
