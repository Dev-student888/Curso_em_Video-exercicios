# Crie um programa onde 4 jogadores joguem um dado e tenham
# resultados aleatórios. Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor
# tirou o maior número no dado.

from random import randint
from time import sleep

jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)
             }
print('Valores sortados:')
for k, v in jogadores.items():
    print(f'\tO {k} tirou {v}')
    sleep(1)
print('Ranking dos jogadores:')
for i in range(1, 5):
    print(f'\t{i}º jogador:  com ')
