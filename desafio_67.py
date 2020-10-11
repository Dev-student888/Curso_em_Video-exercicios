# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando
# o número solicitado for negativo.

while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    if t < 0:
        break
    c = 1
    print('-'*30)
    while c <= 10:
        r = t * c
        print(f'{t} x {c:2d} = {r:2d}')
        c += 1
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
