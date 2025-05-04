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

        #carregando componentes do jogo (mundo e jogador)
        self.world = World_SNAKE(pyxel.tilemaps[0], 1, 3)
        self.player = Snake(8, 24, 0, 16, 0, 8, 8, 8)

        pyxel.run(self.update, self.draw)

    def update(self):
        if (pyxel.frame_count%8 == 0):
            #checando por movimentacao do jogador (a cada 1 segundo)
            if (pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP)):
                self.player.move('w', LARGURA_JANELA, ALTURA_JANELA)
            elif (pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)):
                self.player.move('a', LARGURA_JANELA, ALTURA_JANELA)
            elif (pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN)):
                self.player.move('s', LARGURA_JANELA, ALTURA_JANELA)
            elif (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)):
                self.player.move('d', LARGURA_JANELA, ALTURA_JANELA)
            elif (pyxel.btn(pyxel.KEY_SPACE)):
                self.player.grow()

    def draw(self):
        pyxel.cls(0)
        #desenhando mapa
        for y in range(self.world.ALTURA):
            for x in range(self.world.LARGURA):
                worldItem = self.world.world_map[y][x]
                self.world.draw_worldItens(pyxel, x, y, 0, worldItem)
        #desenhando jogador
        self.player.drawSnake(pyxel)

App()