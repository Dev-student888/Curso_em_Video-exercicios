# Crie um programa que gerencie o aproveitamento de um
# jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade
# de gols feitos em cada partida. No final, tudo isso será guardado
# em um dicionário, incluindo o total de gols feitos durante
# o campeonato.

jogador = dict()
t = 0
jogador['nome'] = str(input('Nome: ')).strip()
jogador['partidas'] = int(input(f'Quantidade de partidas que {jogador["nome"]} jogou: '))
for i in range(jogador['partidas']):
    gp = int(input(f'Gols da {i + 1}ª partida: '))
    t += gp
jogador['total de gols'] = t
print('-=' * 30)
print(' == RANKING DO JOGADOR ==')
for k, v in jogador.items():
    print(f'  - {k} tem o valor {v}')
