# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número
# de tipo inválido. Aproveite e crie também uma função leiaFloat()
# com a mesma funcionalidade.


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mERRO: por favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mERRO: por favor digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            if n == 0:
                return 0
            else:
                return f'{n:.2f}'


nm = leiaInt('Digite um número Inteiro: ')
fl = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {nm} e o real foi {fl}')
