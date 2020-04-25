# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
#
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres tem menos de 20 anos.

print('*' * 39)
print('\t\tFICHA DE RECONHECIMENTO')
print('*' * 39, end='\n')
nome = ''
idade = 0
sexo = ''
c = 0
i = 0
iv = 0
v = ''
ml = 0
for i in range(1, 5):
    print('PESSOA {}:\n'.format(i))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    print('*' * 39, end='\n')
    c += idade
    if sexo in 'Mm' and idade > iv:
        iv = idade
        v = nome
    if sexo in 'Ff' and idade < 20:
        ml += 1
c = c / i
print('A média de idade deste grupo é de {}'.format(c))
print('O homem mais velho tem {} anos e se chama {}'.format(iv, v))
if ml == 1:
    print('Neste grupo há {} mulher com menos de 20 anos!'.format(ml))
elif ml > 1 or ml == 0:
    print('Neste grupo há {} mulheres com menos de 20 anos!'.format(ml))
