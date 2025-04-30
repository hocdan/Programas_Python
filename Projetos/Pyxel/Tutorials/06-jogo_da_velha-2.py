import pyxel

#declarando variaveis que serao utilizadas pelo jogo
global jogo, jogoRec, menu, botaoVelha, botaoZerar, velha, zerar, pontosX, pontosO, vencedorAtual, rodada
#matriz que guarda os valores das jogadas (0=vazio, 1=jogador X, 2=jogador O)
jogo = [ [0, 1, 0],
        [0, 2, 2],
        [1, 0, 0] ]
#setando valores das dimensoes dos locais jogaveis (matriz de retangulos com x, y, altura, largura)
jogoRec = [ [100, 50, 100, 100], [210, 50, 100, 100], [320, 50, 100, 100],
            [100, 160, 100, 100], [210, 160, 100, 100], [320, 160, 100, 100],
            [100, 270, 100, 100], [210, 270, 100, 100], [320, 270, 100, 100] ]
menu = [10, 430, 500, 180]
botaoVelha = [425, 440, 75, 75]
botaoZerar = [425, 525, 75, 75]
#setando valores iniciais dos jogadores e do jogo
velha, zerar, pontosX, pontosO, vencedorAtual, rodada = 0, 0, 0, 0, 0, 0

#funcao responsavel por checar a existencia de toque em uma determinada area retangular
def checarToque(x0, y0, x1, y1, largura, altura):
    toque = False
    if ( (x0 >= x1 and x0 <= (x1+largura)) and (y0 >= y1 and y0 <= (y1+altura)) ):
        toque = True
    return toque

class App():
    
    def __init__(self):
        pyxel.init(520, 620, title = "Jogo da velha 1.0")
        pyxel.mouse(True)
        #carregando imagens dos icones
        pyxel.load("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/Assets/icones.pyxres")
        #carregando fontes customizadas para o jogo
        self.fonte1 = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/Fonts/courB24.bdf")
        self.fonte2 = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/Fonts/gb24st.bdf")
        self.fonte3 = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/Fonts/VictoriaBold-8.bdf")
        self.fonte4 = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/Fonts/helvB24.bdf")
        pyxel.run(self.update, self.draw)

    def update(self):
        global rodada, pontosX, pontosO, vencedorAtual
        if (pyxel.btnp(pyxel.KEY_Q)):
            pyxel.quit()

        #checando possibilidade de vitoria
        if (vencedorAtual == 0 or vencedorAtual == 3):
            if ( (jogo[0][0] == 1 and jogo[0][1] == 1 and jogo[0][2] == 1) or
                (jogo[0][0] == 1 and jogo[1][1] == 1 and jogo[2][2] == 1) or
                (jogo[0][0] == 1 and jogo[1][0] == 1 and jogo[2][0] == 1) or
                (jogo[1][0] == 1 and jogo[1][1] == 1 and jogo[1][2] == 1) or
                (jogo[2][0] == 1 and jogo[2][1] == 1 and jogo[2][2] == 1) or
                (jogo[0][1] == 1 and jogo[1][1] == 1 and jogo[2][1] == 1) or
                (jogo[0][2] == 1 and jogo[1][2] == 1 and jogo[2][2] == 1) or
                (jogo[2][0] == 1 and jogo[1][1] == 1 and jogo[0][2] == 1)):
                pontosX += 1
                vencedorAtual = 1
            elif ( (jogo[0][0] == 2 and jogo[0][1] == 2 and jogo[0][2] == 2) or
                (jogo[0][0] == 2 and jogo[1][1] == 2 and jogo[2][2] == 2) or
                (jogo[0][0] == 2 and jogo[1][0] == 2 and jogo[2][0] == 2) or
                (jogo[1][0] == 2 and jogo[1][1] == 2 and jogo[1][2] == 2) or
                (jogo[2][0] == 2 and jogo[2][1] == 2 and jogo[2][2] == 2) or
                (jogo[0][1] == 2 and jogo[1][1] == 2 and jogo[2][1] == 2) or
                (jogo[0][2] == 2 and jogo[1][2] == 2 and jogo[2][2] == 2) or
                (jogo[2][0] == 2 and jogo[1][1] == 2 and jogo[0][2] == 2)):
                pontosO += 1
                vencedorAtual = 2
        #checando clique do mouse nos retangulos de colisao/locais jogaveis no jogo
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            elemento = 0 #necessario para realizar a conversao entre as duas matrizes (para assim iterar sobre as duas com a mesma logica)
            for i in range(len(jogo)): #percorrendo linhas
                for j in range(len(jogo[i])): #percorrendo colunas
                    if (checarToque(pyxel.mouse_x, pyxel.mouse_y, jogoRec[elemento][0], jogoRec[elemento][1], jogoRec[elemento][2], jogoRec[elemento][3])):
                        #checando se eh a vez de X e se X fez uma jogada valida, se sim...alterar valor para 1
                        if (rodada%2 == 0 and jogo[i][j] == 0):
                            jogo[i][j] = 1
                            rodada += 1
                        #checando se eh a vez de O e se O fez uma jogada valida, se sim...alterar valor para 2
                        elif (rodada%2 != 0 and jogo[i][j] == 0):
                            jogo[i][j] = 2
                            rodada += 1
                    elemento += 1
        #checando clique do mouse no botao de VELHA
        if (checarToque(pyxel.mouse_x, pyxel.mouse_y, botaoVelha[0], botaoVelha[1], botaoVelha[2], botaoVelha[3]) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)):
            #limpando matriz de valores do jogo (retirando Xs e Os)
            for i in range(len(jogo)): #percorrendo linhas
                for j in range(len(jogo[i])): #percorrendo colunas
                    jogo[i][j] = 0
            rodada += 1
            vencedorAtual = 0
        #checando clique do mouse no botao de ZERAR
        if (checarToque(pyxel.mouse_x, pyxel.mouse_y, botaoZerar[0], botaoZerar[1], botaoZerar[2], botaoZerar[3]) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)):
            #limpando matriz de valores do jogo (retirando Xs e Os)
            for i in range(len(jogo)): #percorrendo linhas
                for j in range(len(jogo[i])): #percorrendo colunas
                    jogo[i][j] = 0
            rodada = 0
            pontosX = 0
            pontosO = 0
            vencedorAtual = 0
    def draw(self):
        pyxel.cls(pyxel.COLOR_CYAN) #cor de fundo
        #desenhando zonas de colisao
        #for rec in jogoRec:
        #    pyxel.rect(rec[0], rec[1], rec[2], rec[3], pyxel.COLOR_BLACK)
        #desenhando linhas da cruzada
        pyxel.line(205, 50, 205, 370, pyxel.COLOR_BLACK)
        pyxel.line(315, 50, 315, 370, pyxel.COLOR_BLACK)
        pyxel.line(100, 155, 420, 155, pyxel.COLOR_BLACK)
        pyxel.line(100, 265, 420, 265, pyxel.COLOR_BLACK)
        #desenhando Xs e Os, a depender do estado atual do jogo
        elemento = 0 #necessario para realizar a conversao entre as duas matrizes (para assim iterar sobre as duas com a mesma logica)
        for i in range(len(jogo)): #percorrendo linhas
            for j in range(len(jogo[i])): #percorrendo colunas
                if (jogo[i][j] == 1): #desenhando um X (posicao baseada no retangulo de colisao)
                    pyxel.line(jogoRec[elemento][0]+5, jogoRec[elemento][1]+5, jogoRec[elemento][0]+90, jogoRec[elemento][1]+90, pyxel.COLOR_BLACK)
                    pyxel.line(jogoRec[elemento][0]+5, jogoRec[elemento][1]+90, jogoRec[elemento][0]+90, jogoRec[elemento][1]+5, pyxel.COLOR_BLACK)
                elif (jogo[i][j] == 2): #desenhando um O (posicao baseada no retangulo de colisao)
                    pyxel.circb(jogoRec[elemento][0]+50, jogoRec[elemento][1]+50, 50, pyxel.COLOR_BLACK)
                elemento += 1 #atualizando proximo elemento da matriz de colisao a ser lido
        #desenhando retangulo e informacoes do menu
        pyxel.rect(menu[0], menu[1], menu[2], menu[3], pyxel.COLOR_NAVY)
        if (rodada%2 == 0):
            pyxel.text(menu[0]+27, menu[1]+10, "TURNO DO JOGADOR X", pyxel.COLOR_PEACH, self.fonte4)
        else:
            pyxel.text(menu[0]+27, menu[1]+10, "TURNO DO JOGADOR O", pyxel.COLOR_PEACH, self.fonte4)
        pyxel.text(menu[0]+110, menu[1]+65, "X: {}".format(pontosX), pyxel.COLOR_PEACH, self.fonte4)
        pyxel.text(menu[0]+260, menu[1]+65, "O: {}".format(pontosO), pyxel.COLOR_PEACH, self.fonte4)
        if (vencedorAtual == 1):
            pyxel.text(menu[0]+10, menu[1]+125, "VITORIA DO JOGADOR X!", pyxel.COLOR_PEACH, self.fonte4)
        elif (vencedorAtual == 2):
            pyxel.text(menu[0]+10, menu[1]+125, "VITORIA DO JOGADOR O!", pyxel.COLOR_PEACH, self.fonte4)
        elif (vencedorAtual == 3):
            pyxel.text(menu[0]+60, menu[1]+125, "DEU VELHA!", pyxel.COLOR_PEACH, self.fonte4)
        else:
            pyxel.text(menu[0]+30, menu[1]+125, "JOGO EM ANDAMENTO", pyxel.COLOR_PEACH, self.fonte4)
        #desenhando botoes
        pyxel.rect(botaoVelha[0], botaoVelha[1], botaoVelha[2], botaoVelha[3], pyxel.COLOR_GREEN)
        pyxel.blt(botaoVelha[0]+14, botaoVelha[1]+14, 0, 0, 56, 48, 48, pyxel.COLOR_BLACK)
        pyxel.rect(botaoZerar[0], botaoZerar[1], botaoZerar[2], botaoZerar[3], pyxel.COLOR_RED)
        pyxel.blt(botaoZerar[0]+18, botaoZerar[1]+12, 0, 0, 0, 40, 48, pyxel.COLOR_BLACK)

App()