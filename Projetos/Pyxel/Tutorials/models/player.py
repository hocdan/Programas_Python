'''
    DECLARACAO DE OBJETOS

    Jogador simples (bacteria): em desenvolvimento
    Jogador simples (snake): em desenvolvimento
'''

class Bacteria:
    #inicializacao dos atributos
    def __init__(self, posX, posY, imgBank, pixelX, pixelY, largura, altura, Dx=6):
        self.posX = posX
        self.posY = posY
        self.imgBank = imgBank
        self.pixelX = pixelX
        self.pixelY = pixelY
        self.largura = largura
        self.altura = altura
        self.Dx = Dx #quantidade de pixels movidos por frame
        self.dirAtual = 'o' #flag usada para saber em que direcao a bacteria esta se movendo (o = parada)

    def move(self, direcao, larguraJanela, alturaJanela):
        #checando direcao escolhida e se eh possivel (dentro da janela do jogo)
        if (direcao == 'w' and (self.posY-self.Dx) >= 0):
            #mudando direcao e informacoes para sprite do jogador ser atualizada na direcao UP
            self.dirAtual = 'w'
            self.pixelX = 48
            self.pixelY = 0
            self.posY -= self.Dx
        elif (direcao == 'a' and (self.posX-self.Dx) >= 0):
            #mudando direcao e informacoes para sprite do jogador ser atualizada na direcao LEFT
            self.dirAtual = 'a'
            self.pixelX = 32
            self.pixelY = 0
            self.posX -= self.Dx
        elif (direcao == 's' and (self.posY+self.Dx) <= (alturaJanela-self.altura)):
            #mudando direcao e informacoes para sprite do jogador ser atualizada na direcao DOWN
            self.dirAtual = 's'
            self.pixelX = 0
            self.pixelY = 16
            self.posY += self.Dx
        elif (direcao == 'd' and (self.posX+self.Dx) <= (larguraJanela-self.largura)):
            #mudando direcao e informacoes para sprite do jogador ser atualizada na direcao RIGHT
            self.dirAtual = 'd'
            self.pixelX = 16
            self.pixelY = 0
            self.posX += self.Dx
        elif (direcao == 'o'):
            #mudando direcao e informacoes para sprite do jogador ser atualizada na direcao STILL
            self.dirAtual = 'o'
            self.pixelX = 0
            self.pixelY = 0

class Snake:
    #inicializacao dos atributos
    def __init__(self, posX, posY, imgBank, pixelX, pixelY, largura, altura, Dx=6):
        self.posX = posX
        self.posY = posY
        self.imgBank = imgBank
        self.pixelX = pixelX
        self.pixelY = pixelY
        self.largura = largura
        self.altura = altura
        self.Dx = Dx #quantidade de pixels movidos por frame
        self.dirAtual = 's' #flag usada para saber em que direcao a bacteria esta se movendo

    def move(self, direcao, larguraJanela, alturaJanela):
        #checando direcao escolhida e se eh possivel (dentro da janela do jogo)
        if (direcao == 'w' and (self.posY-self.Dx) >= 0):
            #mudando direcao e informacoes para sprite do jogador ser atualizada na direcao UP
            self.dirAtual = 'w'
            self.pixelX = 8
            self.pixelY = 0
            self.posY -= self.Dx
        elif (direcao == 'a' and (self.posX-self.Dx) >= 0):
            #mudando direcao e informacoes para sprite do jogador ser atualizada na direcao LEFT
            self.dirAtual = 'a'
            self.pixelX = 0
            self.pixelY = 0
            self.posX -= self.Dx
        elif (direcao == 's' and (self.posY+self.Dx) <= (alturaJanela-self.altura)):
            #mudando direcao e informacoes para sprite do jogador ser atualizada na direcao DOWN
            self.dirAtual = 's'
            self.pixelX = 16
            self.pixelY = 0
            self.posY += self.Dx
        elif (direcao == 'd' and (self.posX+self.Dx) <= (larguraJanela-self.largura)):
            #mudando direcao e informacoes para sprite do jogador ser atualizada na direcao RIGHT
            self.dirAtual = 'd'
            self.pixelX = 24
            self.pixelY = 0
            self.posX += self.Dx
