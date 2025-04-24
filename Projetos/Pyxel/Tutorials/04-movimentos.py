import pyxel
from models.player import Bacteria

#declarando constantes
LARGURA_JANELA = 160
ALTURA_JANELA = 120

class App():

    def __init__(self):
        pyxel.init(LARGURA_JANELA, ALTURA_JANELA, "MOVIMENTOS 1.0")
        pyxel.mouse(True)
        pyxel.load("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/Assets/bacterias.pyxres")
        
        self.player = Bacteria(0, 0, 0, 0, 0, 16, 16)
        
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
        else:
            self.player.move('o', LARGURA_JANELA, ALTURA_JANELA)


    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.player.posX, 
                self.player.posY, 
                self.player.imgBank, 
                self.player.pixelX, 
                self.player.pixelY, 
                self.player.largura, 
                self.player.altura,
                pyxel.COLOR_BLACK)
        
App()