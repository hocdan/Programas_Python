import pyxel

class App():
    def __init__(self):
      pyxel.init(160, 120, title = "Hello Pyxel :)")
      pyxel.images[0].load(0, 0, "/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/Assets/pyxel_logo_38x16.png")
      pyxel.run(self.update, self.draw)

    def update(self):
      if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    def draw(self):
      pyxel.cls(pyxel.COLOR_BLACK)
      pyxel.text(55, 41, "Hello, pyxel!", pyxel.frame_count % 16) #mostra o texto variando a cor com base no frame atual
      pyxel.blt(61, 66, 0, 0, 0, 38, 16) #posiciona e mostra imagem da logo Pyxel

App()
