# Crie um programa que gerencie o aproveitamento de um
# jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade
# de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols
# feitos durante o campeonato.

jogador = dict()
gols = list()
t = 0
jogador['nome'] = str(input('Nome do Jogador: ')).strip()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(partidas):
    gp = int(input(f'Quantos gols na {i + 1}ª partida? '))
    t += gp
    gols.append(gp)
jogador['gols'] = gols[:]
jogador['total'] = t
# jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i in range(partidas):
    for j in gols:
        print(f'\t=> Na {i + 1}ª partida, fez {j} gols.')
        i += 1
    break
# for i, v in enumerate(jogador['gols']):
#     print(f'\t=>Na {i + 1}ª partida, fez {v} gols.')
print(f'Foi um total de {t} gols.')
