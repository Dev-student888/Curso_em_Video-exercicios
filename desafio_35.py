# Desenvolva um programa que leia o comprimento de três retas e diga
# ao usuário se elas podem ou não formar um triângulo

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento de uma segunda reta: '))
r3 = float(input('Digite o comprimento de uma terceira reta: '))

if abs(r2) - abs(r3) < r1 < r2 + r3 and abs(r1) - abs(r3) < r2 < r1 + r3 and abs(r1) - abs(r2) < r3 < r1 + r2:
    print('As retas A, B e C podem formar um triângulo!\n')
else:
    print('As retas A, B e C não podem formar um triângulo!\n')
