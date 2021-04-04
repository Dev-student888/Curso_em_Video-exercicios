# Faça um programa que tenha uma função chamada
# ficha(), que dois parâmetros opcionais: o nome de um jogador
# e quantos gols ele marcou. O programa deverá ser capaz de
# mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.

def ficha(nome, gols=0):
    if not nome:
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 30)
n = str(input('Nome do Jogador: ')).strip()
g = int(input('Número de Gols: '))
ficha(n, g)
