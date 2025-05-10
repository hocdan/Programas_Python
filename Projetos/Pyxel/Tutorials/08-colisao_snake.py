import pyxel

from models.player import Snake
from models.world import *

#declarando constantes
LARGURA_JANELA = 128
ALTURA_JANELA = 128
TAMANHO = 8 #referencia das dimensoes em pixels dos sprites no tilemap

class App():

    def __init__(self):
        pyxel.init(LARGURA_JANELA, ALTURA_JANELA, "SNAKE 1.0", fps=60)
        pyxel.mouse(True)
        pyxel.load("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/Assets/snake.pyxres")
        #carregando fonte das letras
        self.fonte = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/Fonts/VictoriaBold-8.bdf")

        #carregando componentes do jogo (mundo e jogador)
        self.player = Snake(8, 24, 0, 16, 0, 8, 8, 8)
        self.world = World_SNAKE(pyxel.tilemaps[0], self.player)
        self.INPUT = 's' #flag de controle para a direcao passiva da cobra
        self.GAME_OVER = False 


        pyxel.run(self.update, self.draw)

    def update(self):
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
            if (pyxel.frame_count%16 == 0):
                #realizando mudanca de movimento
                if (self.INPUT == 'w'):
                    if ( self.world.checkCollision('w') not in ["tijolo", "caixa", "corpo", "invalido"]):
                        self.player.move('w', LARGURA_JANELA, ALTURA_JANELA)
                    elif ( self.world.checkCollision('w') in ["tijolo", "caixa", "corpo"] ):
                        self.GAME_OVER = True
                elif (self.INPUT == 'a'):
                    if ( self.world.checkCollision('a') not in ["tijolo", "caixa", "corpo", "invalido"]):
                        self.player.move('a', LARGURA_JANELA, ALTURA_JANELA)
                    elif ( self.world.checkCollision('a') in ["tijolo", "caixa", "corpo"] ):
                        self.GAME_OVER = True
                elif (self.INPUT == 's'):
                    if ( self.world.checkCollision('s') not in ["tijolo", "caixa", "corpo", "invalido"]):
                        self.player.move('s', LARGURA_JANELA, ALTURA_JANELA)
                    elif ( self.world.checkCollision('s') in ["tijolo", "caixa", "corpo"] ):
                        self.GAME_OVER = True
                elif (self.INPUT == 'd'):
                    if ( self.world.checkCollision('d') not in ["tijolo", "caixa", "corpo", "invalido"]):
                        self.player.move('d', LARGURA_JANELA, ALTURA_JANELA)
                    elif ( self.world.checkCollision('d') in ["tijolo", "caixa", "corpo"] ):
                        self.GAME_OVER = True
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
                self.player = Snake(8, 24, 0, 16, 0, 8, 8, 8)
                self.world = World_SNAKE(pyxel.tilemaps[0], self.player)
                self.INPUT = 's' #flag de controle para a direcao passiva da cobra
                self.GAME_OVER = False 

    def draw(self):
        pyxel.cls(0)
        if (not self.GAME_OVER):
            self.world.loadSnakeOnTilemap() #atualizando valores do jogador no tilemap
            #desenhando mapa
            for y in range(self.world.ALTURA):
                for x in range(self.world.LARGURA):
                    worldItem = self.world.world_map[y][x]
                    self.world.draw_worldItens(pyxel, x, y, 0, worldItem)
        else:
            #desenhando tela de fim de jogo
            pyxel.text(30, 45, "GAME OVER", pyxel.COLOR_WHITE, self.fonte)
            pyxel.text(15, 75, "> Press R to restart game", pyxel.COLOR_WHITE)
            pyxel.text(15, 85, "> Press ESC to exit game", pyxel.COLOR_WHITE)



App()