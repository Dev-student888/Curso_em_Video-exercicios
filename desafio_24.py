# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO".

nc = str(input('Digite o nome de uma cidade somente: ')).strip().title()
d = nc.split()
print('Esta cidade possui a palavra \'SANTO\' no começo de seu nome?')
print('Santo' in d[0])

# nc = str(input('Digite o nome da cidade onde você nasceu: ')).strip()
# print(nc[:5].title() == 'Santo')
