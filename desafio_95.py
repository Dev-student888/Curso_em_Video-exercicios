# Aprimore o DESAFIO 093 para que ele funcione com vários
# jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.

times = list()
jogador = dict()

while True:
    jogador['nome'] = str(input('Nome de jogador: ')).strip()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols em cada partida'] = list()
    for i in range(jogador['partidas']):
        jogador['gols em cada partida'].append(int(input(f'\tQuantos gols na {i + 1}ª partida? ')))
    jogador['total de gols'] = sum(jogador['gols em cada partida'])
    r = str(input('Quer continuar? [S/N] ')).strip()[0]
    while r not in 'SsNn':
        print('ERRO! Por favor digite apenas \'S\' ou \'N\'!')
        r = str(input('Quer continuar? [S/N] ')).strip()[0]
    if r in 'Nn':
        times.append(jogador.copy())
        break
    times.append(jogador.copy())
print('-=' * 30)
print('cod nome\t\t\t\tgols\t\t\t\ttotal')
print('-' * 51)
for i in range(len(times)):
    print(f'  {i} {times[i]["nome"]} {str(times[i]["gols em cada partida"])} {str(times[i]["total de gols"])}')
print('-' * 51)
