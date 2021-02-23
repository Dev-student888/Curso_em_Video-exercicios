# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção
# (sem usar o sort()). No final, mostre a lista ordenada na tela.

l = []
mj = mn = 0

for i in range(0, 5):
    l.append(int(input('Digite um número: ')))
    if i == 0:
        mj = mn = l[i]
    else:
        if l[i] < mn:
            mn = l[i]
            l[i-1] = mn
        if l[i] > mj:
            mj = l[i]
            l[i+1] = mj

print(f'Lista: {l}')
