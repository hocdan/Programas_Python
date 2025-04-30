import pyxel
from models.player import Snake
from models.world import *

#declarando constantes
LARGURA_JANELA = 128
ALTURA_JANELA = 128
TAMANHO = 8

class App():

    def __init__(self):
        pyxel.init(LARGURA_JANELA, ALTURA_JANELA, "TILE MAP 1.0")
        pyxel.mouse(True) #ativando visibilidade do cursor do mouse
        pyxel.load("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/Assets/snake.pyxres")

        #criando mundo para o jogo Snake (usando o tilemap do bank 0 do arquivo snake.pyxres)
        self.world = World_SNAKE(pyxel.tilemaps[0], 1, 3)
        #criando jogador tipo Snake
        self.player = Snake(8, 8, 0, 0, 0, 8, 8)

        pyxel.run(self.update, self.draw)

    def update(self):
        #checando por movimentacao do jogador
        if (pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP)):
            self.player.move('w', LARGURA_JANELA, ALTURA_JANELA)
        elif (pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)):
            self.player.move('a', LARGURA_JANELA, ALTURA_JANELA)
        elif (pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN)):
            self.player.move('s', LARGURA_JANELA, ALTURA_JANELA)
        elif (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)):
            self.player.move('d', LARGURA_JANELA, ALTURA_JANELA)

    def draw(self):
        pyxel.cls(0)

        #desenhando mapa
        for y in range(self.world.ALTURA):
            for x in range(self.world.LARGURA):
                worldItem = self.world.world_map[y][x] #armazenando cada item presente na matriz mapa do mundo
                self.world.draw_worldItens(pyxel, x, y, 0, worldItem) #desenhando itens de acordo com seu valor e posicao

        #desenhando jogador
        pyxel.blt(self.player.posX, 
                self.player.posY, 
                self.player.imgBank, 
                self.player.pixelX, 
                self.player.pixelY, 
                self.player.largura, 
                self.player.altura,
                pyxel.COLOR_BLACK)

App()