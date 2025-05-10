import pyxel
import random

from models.player import Snake
from models.world import *

#declarando constantes
LARGURA_JANELA = 128
ALTURA_JANELA = 137 #onde 128 pixels sao dedicados ao jogo e 9 pixels as informacoes do jogador (vida e pontos)
TAMANHO = 8 #referencia das dimensoes em pixels dos sprites no tilemap

class App():

    def __init__(self):
        pyxel.init(LARGURA_JANELA, ALTURA_JANELA, "SNAKE 1.0", fps=60)
        pyxel.mouse(True)
        pyxel.load("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/Assets/snake.pyxres")
        #carregando fonte das letras
        self.fonte = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/Fonts/VictoriaBold-8.bdf")

        #carregando componentes do jogo (mundo e jogador)
        self.player = Snake(8, 24, 0, 16, 0, 8, 8, 8, vidas=5, pontos=100)
        self.world = World_SNAKE(pyxel.tilemaps[0], self.player)
        self.INPUT = 's' #flag de controle para a direcao passiva da cobra
        self.GAME_OVER = False 


        pyxel.run(self.update, self.draw)

    def update(self):
        #checando se jogador ja utilizou todas as vidas ao jogar
        if (self.player.vidas <= 0):
            self.GAME_OVER = True
        if (not self.GAME_OVER):
            #checando constantemente input do usuario, caso jogo nao tenha finalizado
            if (pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP)):
                self.INPUT = 'w'
            elif (pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)):
                self.INPUT = 'a'
            elif (pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN)):
                self.INPUT = 's'
            elif (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)):
                self.INPUT = 'd'
            #checando movimentos invalidos e nao deixando valor ser repassado na atualizacao
            if ( self.world.checkCollision(self.INPUT) == "invalido"):
                self.INPUT = self.world.SNAKE.corpo[0].direcao #restaurando direcao valida
            #atualizando mudanca de movimento a cada 0.5 segundos
            if (pyxel.frame_count%20 == 0):
                if ( self.world.checkCollision(self.INPUT) == "comida"):
                    self.world.grow()
                    if (self.world.checkCollision(self.INPUT) not in ["tijolo", "caixa", "corpo", "invalido"]):
                        self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "fogo"):
                    self.player.vidas -= 1
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "vida"):
                    self.player.vidas += 1
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "moeda"):
                    self.player.pontos += 500
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) == "cristal"):
                    self.player.pontos += 2000
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) not in ["tijolo", "caixa", "corpo", "invalido"]):
                    self.player.move(self.INPUT, LARGURA_JANELA, ALTURA_JANELA)
                elif ( self.world.checkCollision(self.INPUT) in ["tijolo", "caixa", "corpo"] ):
                    self.player.vidas -= 1
                
                #comandos especiais em fase de desenvolvimento
                if (pyxel.btn(pyxel.KEY_SPACE)):
                    self.player.grow() #EM TESTE!!!
                elif (pyxel.btn(pyxel.KEY_I)):
                    self.world.printSnake()
                    self.world.printWorld()
                    pyxel.quit()
        else:
            #checando se usuario ira querer reiniciar jogo
            if (pyxel.btn(pyxel.KEY_R)):
                #carregando componentes do jogo (mundo e jogador)
                self.player = Snake(8, 24, 0, 16, 0, 8, 8, 8, vidas=3, pontos=0)
                self.world = World_SNAKE(pyxel.tilemaps[0], self.player)
                self.INPUT = 's' #flag de controle para a direcao passiva da cobra
                self.GAME_OVER = False 
        #chance de gerar comidas randomicas a cada 10 segundos em locais vazios do mapa
        if (pyxel.frame_count%64 == 0):
            posXrandom = random.randint(0, 127)
            posYrandom = random.randint(0, 127)
            self.world.addItem(posXrandom, posYrandom, WorldItem_SNAKE.COMIDA)

    def draw(self):
        pyxel.cls(0)
        if (not self.GAME_OVER):
            self.world.loadSnakeOnTilemap() #atualizando valores do jogador no tilemap
            #desenhando mapa
            for y in range(self.world.ALTURA):
                for x in range(self.world.LARGURA):
                    worldItem = self.world.world_map[y][x]
                    self.world.draw_worldItens(pyxel, x, y, 0, worldItem)
            #desenhando informacoes do jogador (pontuacao e vidas)
            pyxel.text(80, 130, "POINTS:{}".format(self.player.pontos), pyxel.COLOR_WHITE)
            pyxel.text(2, 130, "LIFE: ", pyxel.COLOR_WHITE)
            for vidas in range(self.player.vidas):
                if (vidas == 5):
                    pyxel.text(71, 129, "+{}".format(self.player.vidas-vidas), pyxel.COLOR_WHITE) #finalizando impressao de coracoes caso > 5
                    break
                pyxel.blt(21+(vidas*10), 128, 0, 32, 16, 8, 8) #desenhando icones de coracao
            
        else:
            #desenhando tela de fim de jogo
            pyxel.text(30, 45, "GAME OVER", pyxel.COLOR_WHITE, self.fonte)
            pyxel.text(15, 75, "> Press R to restart game", pyxel.COLOR_WHITE)
            pyxel.text(15, 85, "> Press ESC to exit game", pyxel.COLOR_WHITE)



App()