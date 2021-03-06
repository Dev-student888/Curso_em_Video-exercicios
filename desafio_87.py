# Aprimore o desafio anterior, mostrando no final:
#
# A) A Soma de todos os valores pares digitados.
# B) A Soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = s3 = mai = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para ({i}, {j}): '))
        if j == 2:
            s3 += matriz[i][j]
        if i == 1:
            if matriz[i][j] > mai:
                mai = matriz[i][j]
print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print()
for E in matriz:
    for e in E:
        if e % 2 == 0:
            s += e
print('-=' * 30)
print(f'A Soma de todos os valores pares digitados é {s}')
print(f'A Soma dos valores da terceira coluna é {s3}')
print(f'O Maior valor da segunda linha é {mai}')
