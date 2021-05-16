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
import Menu         

#Codigo principal
gamestate = "menu"

if __name__ == "__main__":
    #inicializando menu
    if gamestate == "menu":
        Menu.run()



