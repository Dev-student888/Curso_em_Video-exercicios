# Crie um programa que leia nome, ano de nascimento e
# carteira de trabalho e cadastre-os(com idade) em um dicionário se
# por acaso a CTPS for diferente de ZERO, o dicionário receberá
# também o ano de contratação e o salário. Calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
pessoa_fisica = dict()

pessoa_fisica['nome'] = str(input('Nome: ')).strip()
ano = int(input('Ano de Nascimento: '))
n_y = datetime.now().year
pessoa_fisica['idade'] = n_y - ano
pessoa_fisica['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa_fisica['ctps'] == 0:
    print('-=' * 30)
    for k, v in pessoa_fisica.items():
        print(f'  - {k} tem o valor {v}')
while pessoa_fisica['ctps'] < 0:
    del pessoa_fisica['ctps']
    print('Erro! Por favor, tente novamente!')
    print('Por favor NÃO digite números negativos!')
    pessoa_fisica['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
else:
    pessoa_fisica['contratação'] = int(input('Ano de Contratação: '))
    pessoa_fisica['salário'] = float(input('Salário: R$'))
    pessoa_fisica['aposentadoria'] = pessoa_fisica['idade'] + ((pessoa_fisica['contratação'] + 35) - n_y)
    print('-=' * 30)
    for k, v in pessoa_fisica.items():
        print(f'  - {k} tem o valor {v}')
