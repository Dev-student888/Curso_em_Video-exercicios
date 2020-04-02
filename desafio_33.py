# Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR

# EXEMPLO 1

# n = str(input('Digite três números aleatórios(coloque espaços entre cada um): ')).strip()
# d = n.split()
# mj = d[0]
# mn = d[2]
# if d[1]>d[0] and d[1]>d[2]:
#     mj = d[1]
# elif d[2]>d[0] and d[2]>d[1]:
#     mj = d[2]

# if d[0]<d[1] and d[0]<d[2]:
#     mn = d[0]
# elif d[1]<d[2] and d[1]<d[0]:
#     mn = d[1]

# print('O maior número é {}'.format(mj))
# print('O menor número é {}'.format(mn))

# EXEMPLO 2

# Também é possível usar as funções max() e min() juntamente com uma
# lista que guardará estes três números

n = str(input('Digite três números: ')).strip()
if n.isspace() == False:
    l = list(n)
else:
    l = n.split()
print('O maior valor digitado foi {}'.format(max(l)))
print('O menor valor digitado foi {}'.format(min(l)))
