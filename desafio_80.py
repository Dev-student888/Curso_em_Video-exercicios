# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção
# (sem usar o sort()). No final, mostre a lista ordenada na tela.

l = []

for i in range(5):
    v = int(input('Digite um número: '))
    if i == 0 or v > l[-1]:
        l.append(v)
        print('Adicionado ao final da lista... ')
    else:
        pos = 0
        while pos <= len(l):
            if v <= l[pos]:
                l.insert(pos, v)
                print(f'Adicionado na posição {pos} da lista... ')
                break
            pos += 1

print('=-'*30)
print(f'Os valores digitados em ordem foram {l}')
