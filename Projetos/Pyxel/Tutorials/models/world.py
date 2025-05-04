'''
    DECLARACAO DE OBJETOS (mapas e seus itens)

    Mapa simples (para jogador Snake): em desenvolvimento

'''

class WorldItem_SNAKE:
    #Itens do tipo "estrutura" presentes no mundo (8x8)
    TIJOLO = (0, 3) #coordenadas de acordo com o arquivo do tilemap!!!
    CAIXA = (1, 3)
    GELO = (2, 3)
    FOGO = (3, 3)
    VAZIO = (1, 2)
    #Itens do tipo "consumiveis" no mundo (8x8)
    COMIDA = (0, 2) #coordenadas de acordo com o arquivo do tilemap!!!
    MOEDA = (2, 2)
    #itens do tipo "jogador" no mundo (8x8)
    JOGADOR = (2, 0) #coordenadas de acordo com o arquivo do tilemap!!!

class World_SNAKE:
    #constantes das dimensoes do mapa do arquivo tilemap
    LARGURA = 16
    ALTURA = 16
    TAMANHO = 8 #dimensoes em pixels dos itens no tilemap
    
    def __init__(self, tilemap, player_posX, player_posY):
        self.tilemap = tilemap
        self.world_map = [] #matriz que ira conter toda a info sobre posicao de estruturas, itens e jogador 
        self.player_posX = player_posX #posicao X do jogador na matriz do tilemap
        self.player_posY = player_posY #posicao Y do jogador na matriz do tilemap
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
                elif ( self.tilemap.pget(x, y) == WorldItem_SNAKE.JOGADOR ):
                    self.world_map[y].append(WorldItem_SNAKE.VAZIO) #fundo por tras da localizacao do jogador eh vazio
                    self.player_posX = x
                    self.player_posY = y
                else:
                    self.world_map[y].append(WorldItem_SNAKE.VAZIO) #falta de valor igual espaco vazio
    
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
