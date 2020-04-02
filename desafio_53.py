# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.


# EXEMPLO DO PROFESSOR:

frase = str(input('Digite uma frase: ')).strip().lower().split()
frase_sem_espaços = ''.join(frase)
inverso = ''
for letra in range(len(frase_sem_espaços) - 1, -1, -1):
    inverso += frase_sem_espaços[letra]
print('O inverso da frase {} é {}'.format(frase_sem_espaços, inverso))
if inverso == frase_sem_espaços:
    print('Esta frase É UM PALÍNDROMO!')
else:
    print('Esta frase NÃO É UM PALÍNDROMO!')

# EXEMPLO 2:
# f = str(input('Digite uma frase: ')).strip().lower().replace(' ', '')

# if f == f[::-1]:
#   print('Esta frase É UM PALÍNDROMO!')
# else:
#   print('Esta frase NÃO É UM PALÍNDROMO!')
