# Faça um programa que tenha uma função notas() que
# pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação(opcional)
#
# Adicione também as docstrings da função.

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    print('-' * 30)
    d = {
        'total': len(n),
        'maior': max(n),
        'menor': min(n),
        'média': sum(n) / len(n)
    }
    if sit is True:
        if d['média'] < 5:
            d['situação'] = 'RUIM'
        elif d['média'] < 6:
            d['situação'] = 'RAZOÁVEL'
        elif d['média'] > 6:
            d['situação'] = 'BOA'

    return d


# Programa Principal
resp = notas(5, 3, 5, sit=True)
print(resp)
help(notas)
