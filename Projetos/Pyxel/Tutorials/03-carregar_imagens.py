import pyxel

class App():

    def __init__(self):
        pyxel.init(160, 120, title = "Hello pyxel! :)")
        pyxel.load("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/Assets/icones.pyxres")
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(pyxel.COLOR_WHITE)
        pyxel.blt(0, 0, 0, 8, 48, 8, 8) #icone da seta 8x8
        pyxel.blt(18, 0, 0, 0, 48, 8, 8, pyxel.COLOR_BLACK) #icone da lixeira 8x8 "transparente"
        pyxel.blt(36, 0, 0, 16, 48, 8, 8, pyxel.COLOR_BLACK) #icone da seta 2 8x8 "transparente"
        pyxel.blt(0, 16, 0, 0, 0, 40, 48) #icone da lixeira 40x48
        pyxel.blt(0, 64, 0, 0, 56, 48, 48, pyxel.COLOR_BLACK) #icone da seta 2 48x48 "transparente"


App()