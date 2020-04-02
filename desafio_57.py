# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = str(input('Digite o seu sexo [M/F]: ')).strip()
while sexo:
    if sexo == 'M' or sexo == 'F':
        print('Informação armazenada com sucesso!')
        exit()
    else:
        print('Opção Inválida!')
        r = str(input('Gostaria de tentar novamente? [S/N] '))
        if r in 'Ss':
            sexo = str(input('Digite seu sexo [M/F]: ')).strip()
        else:
            exit()
