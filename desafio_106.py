# Faça um mini-sistema que utilize o Interactive Help
# do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra 'FIM',
# o programa se encerrará.
# OBS.: use cores.

def ajuda():
    while True:
        print("\033[0;34;40m" + "~~" + "~" * 23 + "~~" + "\033[m")
        print("\033[0;34;40m  SISTEMA DE AJUDA PyHELP  \033[m")
        print("\033[0;34;40m" + "~~" + "~" * 23 + "~~" + "\033[m")
        valor = str(input("Função ou Biblioteca > "))
        if valor in 'FIMfim':
            print("\033[0;31;40m" + "~" * 4 + "~" * 9 + "\033[m")
            print("\033[0;31;40m  ATÉ LOGO!  \033[m")
            print("\033[0;31;40m" + "~" * 4 + "~" * 9 + "\033[m")
            break
        if valor.isidentifier():
            print("\033[0;30;42m" + "~" * 36 + "~" * len(valor) + "\033[m")
            print(f"\033[0;30;42m  Acessando o manual do comando \'{valor}\'  \033[m")
            print("\033[0;30;42m" + "~" * 36 + "~" * len(valor) + "\033[m")
            print("\033[0;30;44m", end="")
            help(valor)
            print("\033[m", end="")


ajuda()
