# Escreva um programa que leia um número inteiro
# qualquer e peça para o usuário escolher qual
# será a base de conversão:
#
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

n = int(input('Digite um número: '))
op = int(input('\nOPÇÕES:\n[1] - BINÁRIO\n[2] - OCTAL\n[3] - HEXADECIMAL\n'))

if op == 1:
    print(bin(n)[2:])
elif op == 2:
    print(oct(n)[2:])
elif op == 3:
    print(hex(n)[2:])
else:
    print('Opção inválida! Tente novamente!')
