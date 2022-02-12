'''
    Programa principal do jogo de RPG de texto: ?????
    
    -> Baseado em um sistema de rotas onde as decisoes irao direcionar o jogador
    pelo mundo e influenciar diretamente quais personagens encontrar, que obje-
    tos vai interagir e quais locais atravessar...
    -> Tudo por meio de texto e escolhas de ações que podem estar divididas em
    ate 3 opções. O jogador tambem poderá consultar seus dados, como: atribu-
    tos, equipamento e inventário, bem como saber a sua localizacao atual.
    -> Por enquanto so havera uma unica classe chamada de Heroi. 
'''

#realizando import das fases e de outras coisas
from Objetos import *
import os
import sys
#configurando para poder usar arquivos que se encontram em outro diretorio
novoDiretorio = os.path.join(os.getcwd() + '/Caminhos/')
sys.path.insert(1, novoDiretorio) #adicionando diretorio à variavel system's path 

import menu
import criacao
import rota01         

#Codigo principal
gamestate = "menu"
rodando = True
while rodando:
    if __name__ == "__main__":
        #inicializando jogo
        if (gamestate == "menu"):
            gamestate = menu.run()
        elif (gamestate == "criacao"):
            gamestate = criacao.run()
        elif (gamestate == "rota01"):
            gamestate = rota01.run()
        else:
            rodando = False
print("Encerrando jogo...")


