# Aprimore o DESAFIO 093 para que ele funcione com vários
# jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.

times = list()
jogador = dict()

while True:
    jogador['nome'] = str(input('Nome de jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols em cada partida'] = list()
    for i in range(partidas):
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
for k, v in enumerate(times):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('-' * 51)
while True:
    d = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    while d != 999:
        if 0 <= d <= len(times) - 1:
            print(f' -- LEVANTAMENTO DO JOGADOR {times[d]["nome"]}:')
            for i, v in enumerate(times[d]['gols em cada partida']):
                print(f'\tNo {i + 1}º jogo fez {v} gols.')
            break
        else:
            print(f'ERRO! Não existe jogador com código {d}.')
            break
    if d == 999:
        break
    print('-' * 51)
print('<< VOLTE SEMPRE >>')
