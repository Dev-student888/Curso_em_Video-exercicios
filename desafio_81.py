# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
#
# A) Quantos números foram digitados.
#
# B) A lista de valores ordenada de forma decrescente.
#
# C) Se o valor 5 foi digitado e está ou não na lista.

l = list()

r = 'S'
while r == 'S':
    l.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()
if r not in 'SN':
    print('Erro! Por favor tente novamente!')
    r = str(input('Quer continuar? [S/N] ')).upper().strip()
print('=-'*30)
print(f'Você digitou {len(l)} elementos.')
l.sort(reverse=True)
print(f'Os valores em ordem decrescente são {l}')
if 5 in l:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
