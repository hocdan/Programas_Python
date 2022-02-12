'''

    Rota 01 do jogo RPG de texto: ?????

'''

from Objetos import *
from time import sleep
import os
import sys

#funcao para limpar a tela
def limpar():
    #para sistemas linux e mac
    if os.name == 'posix':
        _ = os.system('clear')
    #para sistemas windows
    else:
        _ = os.system('cls')

def run():
    #janela da primeira fase
    limpar()
    print("ROTA 01!!!")
    return "menu"

#executando rota01
if __name__ == '__main__':
    run()
