# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
if sexo == 'M' or sexo == 'F':
    print('Informação armazenada com sucesso!')
else:
    while sexo != 'M' or sexo != 'F':
        r = str(input('Opção Inválida!\nGostaria de tentar novamente? [S/N] '))
        if r in 'Ss':
            sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
        else:
            print('Programa finalizado!')
            exit()
