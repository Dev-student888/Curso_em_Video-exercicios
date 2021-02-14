# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação.Depois mostre:
# A) Apenas os 5 primeiros colocados
# B) Os últimos 4 colocados da tabela
# C) Uma lista com os times em ordem alfabética
# D) Em que posição na tabela está o time do Chapecoense

tcb = ('Flamego', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo',
       'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia',
       'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará SC',
       'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

cp = 'Chapecoense'
print('-='*15)
print(f'Lista de times do Brasileirão: {tcb}')
print('-='*15)
print(f'Os 5 primeiros são {tcb[:5]}')
print('-='*15)
print(f'Os 4 últimos são {tcb[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(tcb)}')
print('-='*15)
print(f'O Chapecoense está na {tcb.index(cp) + 1}ª posição')
