# Crie um programa que tenha a função leiaInt(), que
# vai funcionar de forma semelhante à função input() do
# Python, só que fazendo a validação para aceitar apenas
# um valor numérico.
# Ex:
# n = leiaInt('Digite um n')
def leiaInt(x):
    if x.isdecimal() is True:
        return x
    else:
        return '\033[0:31mERRO! Digite um número inteiro válido.\033[m'


# Programa Principal
print('-' * 30)
n = leiaInt(input('Digite um número: '))
if n.isdecimal() is True:
    print(f'Você acabou de digitar o número {n}')
else:
    print(n)
