'''
    DECLARACAO DE OBJETOS (mapas e seus itens)

    Mapa simples (para jogador Snake): em desenvolvimento

'''

class WorldItem_SNAKE:
    #Itens do tipo "estrutura" presentes no mundo (8x8)
    TIJOLO = (0, 3)
    CAIXA = (1, 3)
    GELO = (2, 3)
    FOGO = (3, 3)
    VAZIO = (1, 2)
    #Itens do tipo "consumiveis" no mundo (8x8)
    COMIDA = (0, 2) #coordenadas de acordo com o arquivo do tilemap!!!
    MOEDA = (2, 2)
    CRISTAL = (3, 2)
    #itens do tipo "jogador" no mundo (8x8)
    JOGADOR = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0),
               (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1)
               ] #coordenadas de acordo com o arquivo do tilemap!!!

class World_SNAKE:
    #constantes das dimensoes do mapa do arquivo tilemap
    LARGURA = 16
    ALTURA = 16
    TAMANHO = 8 #dimensoes em pixels dos itens no tilemap
    
    def __init__(self, tilemap, SNAKE):
        self.SNAKE = SNAKE #adicionando informacoes do jogador ao mundo
        self.tilemap = tilemap
        self.world_map = [] #matriz que ira conter toda a info sobre posicao de estruturas, itens e jogador 
        #iterando sobre arquivo do tilemap repassado para gerar o mundo e povoando com os valores dos itens
        for y in range(self.ALTURA):
            self.world_map.append([]) # gerando linhas
            for x in range(self.LARGURA):
                #povoando colunas com itens de acordo com o arquivo do tilemap repassado
                if ( self.tilemap.pget(x, y) == WorldItem_SNAKE.TIJOLO):
                    self.world_map[y].append(WorldItem_SNAKE.TIJOLO)
                elif ( self.tilemap.pget(x, y) == WorldItem_SNAKE.CAIXA ):
                    self.world_map[y].append(WorldItem_SNAKE.CAIXA)
                elif ( self.tilemap.pget(x, y) == WorldItem_SNAKE.GELO ):
                    self.world_map[y].append(WorldItem_SNAKE.GELO)
                elif ( self.tilemap.pget(x, y) == WorldItem_SNAKE.FOGO ):
                    self.world_map[y].append(WorldItem_SNAKE.FOGO)
                elif ( self.tilemap.pget(x, y) == WorldItem_SNAKE.COMIDA ):
                    self.world_map[y].append(WorldItem_SNAKE.COMIDA)
                elif ( self.tilemap.pget(x, y) == WorldItem_SNAKE.MOEDA ):
                    self.world_map[y].append(WorldItem_SNAKE.MOEDA)
                elif ( self.tilemap.pget(x, y) == WorldItem_SNAKE.CRISTAL ):
                    self.world_map[y].append(WorldItem_SNAKE.CRISTAL)
                elif ( self.tilemap.pget(x, y) in WorldItem_SNAKE.JOGADOR):
                    print("GUARDANDO")
                    self.world_map[y].append(self.tilemap.pget(x, y)) #guardando sprite especifica do segmento do corpo do jogador
                else:
                    self.world_map[y].append(WorldItem_SNAKE.VAZIO) #falta de valor igual espaco vazio
    
    def printSnake(self):
        print("Segmentos ativos: ", end="")
        for parte in self.SNAKE.corpo:
            print("[ ({}, {}) | direcao = {} | tipo = {} | frente = {} | costa = {}] ".format(
                parte.posX, parte.posY, parte.direcao, parte.tipo, parte.frente, parte.costa
            ), end="")

    def printWorld(self):
        print("Valores atuais no tilemap:")
        for y in range(self.ALTURA):
            for x in range(self.LARGURA):
                print(self.world_map[y][x], end="")
            print(" {}".format(y))

    #funcao responsavel por desenhar os itens do mapa utilizando o banco de pixels correto
    def draw_worldItens(self, pyxel, posX, posY, sprite_bank, worldItem):
        pyxel.blt( 
            posX * self.TAMANHO, #posicao X onde sera desenhado o item
            posY * self.TAMANHO, #posicao Y onde sera desenhado o item
            sprite_bank, #especificando qual banco de sprites sera usado de referencia para desenhar
            worldItem[0] * self.TAMANHO, #posicao X do sprite no tilemap
            worldItem[1] * self.TAMANHO, #posicao Y do sprite no tilemap
            self.TAMANHO, #dimensao X do item
            self.TAMANHO #dimensao Y do item
        )

    #funcao responsavel por atualizar a localizacao do player no tilemap
    def loadSnakeOnTilemap(self):
        #percorrendo valores no tilemap e comparando com os valores dos segmentos da cobra (conversao necessaria)
        for y in range(self.ALTURA):
            for x in range(self.LARGURA):
                #no caso de existir um valor do tipo "corpo" nessa posicao do tilemap...
                if (self.world_map[y][x] in WorldItem_SNAKE.JOGADOR):
                    #verificar se existe um segmento no corpo com essas coordenadas...
                    existe = False
                    for parte in self.SNAKE.corpo:
                        #se coordenada (x,y) no tilemap tambem existir como coordenada de uma parte do corpo...
                        if ( (x*self.TAMANHO) == parte.posX and (y*self.TAMANHO) == parte.posY):
                            existe = True
                            break #avisando que SIM existe uma parte do corpo com essas coordenadas e quebrando loop for
                    #checando a flag para verificar se existe mesmo um segmento do corpo ou o local esta vazio
                    if (not existe):
                        self.world_map[y][x] = WorldItem_SNAKE.VAZIO #preenchendo com vazio local onde nao existe cobra
                        existe = False
                else:
                    #no caso de nao existir, verificar se no vetor de segmentos ha uma parte que deve ser carregada no tilemap
                    if (self.world_map[y][x] not in WorldItem_SNAKE.JOGADOR):
                        for parte in self.SNAKE.corpo:
                            #se coordenada (x,y) no tilemap tambem existir como coordenada de uma parte do corpo...
                            if ( (x*self.TAMANHO) == parte.posX and (y*self.TAMANHO) == parte.posY):
                                    #preencher tilemap com valor tipo "corpo" especifico do segmento
                                    if (parte.tipo == "head"):
                                        print("CARREGANDO PARTE TIPO HEAD")
                                        if (parte.direcao == 'w'):
                                            self.world_map[y][x] = (1, 0)
                                            self.world_map[y+1][x] = WorldItem_SNAKE.VAZIO #evitando miragem
                                        elif (parte.direcao == 'a'):
                                            self.world_map[y][x] = (0, 0)
                                            self.world_map[y][x+1] = WorldItem_SNAKE.VAZIO #evitando miragem
                                        elif (parte.direcao == 's'):
                                            self.world_map[y][x] = (2, 0)
                                            self.world_map[y-1][x] = WorldItem_SNAKE.VAZIO #evitando miragem
                                        elif (parte.direcao == 'd'):
                                            self.world_map[y][x] = (3, 0)
                                            self.world_map[y][x-1] = WorldItem_SNAKE.VAZIO #evitando miragem
                                    elif (parte.tipo == "body"):
                                        print("CARREGANDO PARTE TIPO BODY")
                                        if (parte.direcao == 'w'):
                                            self.world_map[y][x] = (1, 1)
                                            self.world_map[y+1][x] = WorldItem_SNAKE.VAZIO #evitando miragem
                                        elif (parte.direcao == 'wa'):
                                            self.world_map[y][x] = (4, 1)
                                            self.world_map[y+1][x] = WorldItem_SNAKE.VAZIO #evitando miragem
                                        elif (parte.direcao == 'wd'):
                                            self.world_map[y][x] = (7, 1)
                                            self.world_map[y+1][x] = WorldItem_SNAKE.VAZIO #evitando miragem
                                        elif (parte.direcao == 'a'):
                                            self.world_map[y][x] = (0, 1)
                                            self.world_map[y][x+1] = WorldItem_SNAKE.VAZIO #evitando miragem
                                        elif (parte.direcao == 'as'):
                                            self.world_map[y][x] = (7, 1)
                                            self.world_map[y][x+1] = WorldItem_SNAKE.VAZIO #evitando miragem
                                        elif (parte.direcao == 'sa'):
                                            self.world_map[y][x] = (6, 1)
                                            self.world_map[y-1][x] = WorldItem_SNAKE.VAZIO #evitando miragem
                                        elif (parte.direcao == 's'):
                                            self.world_map[y][x] = (2, 1)
                                            self.world_map[y-1][x] = WorldItem_SNAKE.VAZIO #evitando miragem
                                        elif (parte.direcao == 'sd'):
                                            self.world_map[y][x] = (5, 1)
                                            self.world_map[y-1][x] = WorldItem_SNAKE.VAZIO #evitando miragem
                                        elif (parte.direcao == 'ds'):
                                            self.world_map[y][x] = (4, 1)
                                            self.world_map[y][x-1] = WorldItem_SNAKE.VAZIO #evitando miragem
                                        elif (parte.direcao == 'd'):
                                            self.world_map[y][x] = (3, 1)
                                            self.world_map[y][x-1] = WorldItem_SNAKE.VAZIO #evitando miragem
                                        elif (parte.direcao == 'dw'):
                                            self.world_map[y][x] = (6, 1)
                                            self.world_map[y][x-1] = WorldItem_SNAKE.VAZIO #evitando miragem
                                        elif (parte.direcao == 'aw'):
                                            self.world_map[y][x] = (5, 1)
                                            self.world_map[y][x+1] = WorldItem_SNAKE.VAZIO #evitando miragem
                                    elif (parte.tipo == "tail"):
                                        print("CARREGANDO PARTE TIPO TAIL")
                                        if (parte.direcao == 'w'):
                                            self.world_map[y][x] = (8, 1)
                                        elif (parte.direcao == 'wa'):
                                            self.world_map[y][x] = (10, 0)
                                        elif (parte.direcao == 'aw'):
                                            self.world_map[y][x] = (7, 0)
                                        elif (parte.direcao == 'a'):
                                            self.world_map[y][x] = (9, 0)
                                        elif (parte.direcao == 'as'):
                                            self.world_map[y][x] = (5, 0)
                                        elif (parte.direcao == 'sa'):
                                            self.world_map[y][x] = (11, 0)
                                        elif (parte.direcao == 's'):
                                            self.world_map[y][x] = (4, 0)
                                        elif (parte.direcao == 'sd'):
                                            self.world_map[y][x] = (11, 1)
                                        elif (parte.direcao == 'ds'):
                                            self.world_map[y][x] = (6, 0)
                                        elif (parte.direcao == 'd'):
                                            self.world_map[y][x] = (9, 1)
                                        elif (parte.direcao == 'dw'):
                                            self.world_map[y][x] = (8, 0)
                                        elif (parte.direcao == 'wd'):
                                            self.world_map[y][x] = (10, 1)
    
    '''
        Funcao responsavel por checar colisoes do jogador com os itens no mundo...
        OBS: SEMPRE REALIZAR CONVERSAO DE COORDENADAS DO JOGADOR E DO TILEMAP ( (8, 24) == (1, 3) com T=8)

        Funcao ira devolver valores de acordo com o elemento que foi colidido, onde:
        - return "tijolo/caixa" -> significa que o jogador nao podera avancar para esse lugar
        - return "vazio" -> significa que o jogador podera avancar ao local sem problemas
        - return "moeda" -> significa que o jogador podera avancar ao local e adquirir pontuacao +500
        - return "cristal" -> significa que o jogador podera avancar ao local e adquirir pontuacao +1000
        - return "comida" -> significa que o jogador podera avancar e crescer seu tamanho em 1 (caso ultrapasse o
        local valido para mover durante esse processo acabara resultando em morte para o jogador)
        - return "corpo" -> significa que o jogador colidiu com uma parte de seu corpo e isso resulta em morte
        - return "fogo" -> significa que o jogador colidiu com um local em chamas e por isso ira avancar ao local
        em troca da perca de 1 segmento de seu corpo (caso nao haja segmentos alem da cauda e da cabeca, morte)
    '''
    def checkCollision(self, direcao):
        #verificando local futuro onde o jogador estara ao se mover...convertido para tilemap
        posSnakeX = int((self.SNAKE.corpo[0].posX/self.TAMANHO))
        posSnakeY = int((self.SNAKE.corpo[0].posY/self.TAMANHO))
        print("Posicao do jogador (tilemap): [ {}, {}]".format(posSnakeX, posSnakeY))
        #eliminando movimentos invalidos logo de cara (como cobra andando sobre si mesma em direcao oposta)
        if (direcao == 'w' and self.SNAKE.corpo[0].direcao == 's'):
            return "invalido"
        elif (direcao == 's' and self.SNAKE.corpo[0].direcao == 'w'):
            return "invalido"
        elif (direcao == 'a' and self.SNAKE.corpo[0].direcao == 'd'):
            return "invalido"
        elif (direcao == 'd' and self.SNAKE.corpo[0].direcao == 'a'):
            return "invalido"
        #simulando alteracao da posicao do jogador para futuras comparacoes
        if ( direcao == 'w'):
            posItemX = posSnakeX
            posItemY = posSnakeY-1
        elif ( direcao == 'a'):
            posItemX = posSnakeX-1
            posItemY = posSnakeY
        elif ( direcao == 's'):
            posItemX = posSnakeX
            posItemY = posSnakeY+1
        elif ( direcao == 'd'):
            posItemX = posSnakeX+1
            posItemY = posSnakeY
        else:
            return "invalido"
        #verificando valor no tilemap equivalente ao local do futuro deslocamento
        print("Posicao futura ao se mover: [ {}, {}]".format(posItemX, posItemY))
        if ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.TIJOLO):
            print("Tem uma parede de tijolos na minha frente...nao posso passar!")
            return "tijolo"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.CAIXA):
            print("Tem uma caixa na minha frente...nao posso passar!")
            return "caixa"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.GELO):
            print("Uhhh, que frio...nao posso passar!")
            return "gelo"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.FOGO):
            print("OUCH! Me queimei...")
            return "fogo"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.MOEDA):
            print("Mais uma moeda para a colecao!")
            return "moeda"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.CRISTAL):
            print("Que cristal bonito...")
            return "cristal"
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.COMIDA):
            print("comida")
            '''#verificando novamente posicao futura, ja que ao comer jogador ira aumentar 1 de tamanho
            if ( direcao == 'w'):
                posItemY -= 1
            elif ( direcao == 'a'):
                posItemX -= 1
            elif ( direcao == 's'):
                posItemY += 1
            elif ( direcao == 'd'):
                posItemX += 1
            else:
                return "invalido"
            #se local de crescimento estiver livre entao aumentar em 1 os segmentos e mover cabeca
            if ( self.tilemap.pget(posItemX, posItemY) not in [WorldItem_SNAKE.TIJOLO, WorldItem_SNAKE.CAIXA] and self.tilemap.pget(posItemX, posItemY) not in WorldItem_SNAKE.JOGADOR):
                self.SNAKE.direcao = direcao
                self.SNAKE.grow()
                print("Yum yum...delicia!")
                return "comida"
            print("Nao posso comer! seria o meu fim...")
            return "invalido"'''
        elif ( self.world_map[posItemY][posItemX] == WorldItem_SNAKE.VAZIO):
            print("Caminho livre...em frente!")
            return "vazio"
        elif ( self.world_map[posItemY][posItemX] in WorldItem_SNAKE.JOGADOR):
            print("OUCH! Bati em mim mesmo...")
            return "corpo"
        else:
            print("Nao sei o que esta na minha frente...")
            return "invalido"

