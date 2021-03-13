# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre
# o conteúdo da estrutura na tela.

boletim = dict()
boletim['nome'] = str(input('Nome: ')).strip()
boletim['media'] = float(input(f'Média de {boletim["nome"]}: '))
if boletim['media'] >= 7:
    boletim['situacao'] = 'Aprovado'
elif 5 < boletim['media'] < 7:
    boletim['situacao'] = 'Recuperação'
else:
    boletim['situacao'] = 'Reprovado'

print('-=' * 30)
print(f'\t- Nome é igual a {boletim["nome"]}')
print(f'\t- Média é igual a {boletim["media"]}')
print(f'\t- Situação é igual a {boletim["situacao"]}')
