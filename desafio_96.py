# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular(largura e
# comprimento) e mostre self área do terreno.

def área():
    print(' Controle de Terrenos')
    print('-' * 22)
    l = float(input('LARGURA (m): '))
    c = float(input('COMPRIMENTO (m): '))
    print(f'A área de um terreno {l}x{c} é de {l * c}m².')


área()
