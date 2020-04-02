# Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.


n = int(input('Digite um número inteiro para ver sua tabuada: '))
print('=' * 40, end='\n\t\t\t\t')
print('TABUADA DO {}'.format(n))
print('=' * 40)
for i in range(1, 11):
    print('{} x {:2} = {}'.format(n, i, i*n))
print('=' * 40)
