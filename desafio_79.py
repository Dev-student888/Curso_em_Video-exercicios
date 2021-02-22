# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
# ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

l = list()
while True:
    v = int(input('Digite um valor: '))
    if v in l:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        l.append(v)
    r = str(input('Quer continuar? [S/N] ')).upper().strip()
    if r == 'N':
        break
print('=-'*30)
l.sort()
print(f'Você digitou os valores {l}')
