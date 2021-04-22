# Crie um programa em Python que teste se o site Pudim está
# acessível pelo computador usado.


def internet():
    from urllib.error import URLError
    from urllib.request import urlopen
    try:
        urlopen('http://www.pudim.com.br')
    except URLError:
        print('\033[0;31mO site Pudim não está acessível no momento!\033[m')
    else:
        print('\033[0;32mConsegui acessar o site Pudim com sucesso!\033[m')


internet()
