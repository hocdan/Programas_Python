'''
    Definicoes das classes que serao utilizadas no jogo de RPG de texto
    
    -> Classe Heroi: em teste
    -> Classe Equipamento: em desenvolvimento
    -> Classe Item: em desenvolvimento
'''

#definição da classe Heroi
class Heroi:

    #inicializando informaçoes basicas do jogador
    def __init__(self, nome, nivel, xpAtual, moedas, vida, ataque, equipamentos=None, inventario=None, titulo=None, titulos=None):
        #string, o nome pelo qual o jogador vai ser sempre chamado
        self.nome = nome
        #int, o nivel que o jogador tem
        self.nivel = nivel
        #int, quanto de experiencia o jogador tem
        self.xpAtual = xpAtual
        #int, o quanto o jogador pode comprar
        self.moedas = moedas
        #int, o quanto o jogador pode apanhar
        self.vida = vida
        #int, o quanto o jogador pode bater
        self.ataque = ataque
        #list, equipamentos (8 slots) que o jogador está usando
        if equipamentos is None:
            self.equipamentos = [None, None, None, None, None, None, None, None]
        else:
            self.equipamentos = equipamentos
        #list, objetos que o jogador leva consigo (infinito)
        if inventario is None:
            self.inventario = []
        else:
            self.inventario = inventario
        #string, uma nomeacao exclusiva que o jogador pode ter
        if titulo is None:
            self.titulo = ""
        #list, titulos que o jogador acumulou no jogo (infinito)
        if titulos is None:
            self.titulos = []
        else:
            self.titulos = titulos

    #metodos para alterar atributos
    def mudarTitulo(self, titulo):
        #chamado quando o jogador desejar alterar seu titulo
        if titulo in self.titulos:
            self.titulo = titulo

    def ganharXp(self, xp):
        self.xpAtual += xp
        if self.xpAtual > 100*self.nivel:
            self.xpAtual = self.xpAtual - (100*self.nivel) #resetando barra de xp
            self.nivel += 1 #o jogador entao ira passar de nivel

    def adicionarMoedas(self, moedas):
        self.moedas += moedas #acrescentando dinheiro ao jogador

    def removerMoedas(self, moedas):
        if (self.moedas - moedas < 0):
            return False #transação muito cara, jogador nao vai poder comprar
        else:
            self.moedas -= moedas
            return True #debitando compra do dinheiro do jogador

    def perderVida(self):
        if (self.vida >= 1):
            self.vida -= 1
            return True #o jogador sofreu dano
        else:
            return False #o jogador morreu

    def atacar(self):
        return self.ataque #devolvendo ataque do jogador para processar

    #metodos para manipular objetos do jogador
    def adicionarTitulo(self, titulo):
        self.titulos.append(titulo) #titulo adicionado à colecao do jogador
    
    def equiparArmamento(self, posicao, equipamento):
        #posicao: int e equipamento: objeto do tipo Equipamento
        equipar = False
        #verificando se o equipamento é do tipo Cabeca
        if posicao == 0 and equipamento.regiao == 'Cabeca':
            equipar = True #autorizando equipagem
        #verificando se o equipamento é do tipo Peitoral
        elif posicao == 1 and equipamento.regiao == 'Peito':
            equipar = True #autorizando equipagem
        #verificando se o equipamento é do tipo Maos
        elif posicao == 2 and equipamento.regiao == 'Maos':
            equipar = True #autorizando equipagem
        #verificando se o equipamento é do tipo Pernas
        elif posicao == 3 and equipamento.regiao == 'Pernas':
            equipar = True #autorizando equipagem
        #verificando se o equipamento é do tipo Pes
        elif posicao == 4 and equipamento.regiao == 'Pes':
            equipar = True #autorizando equipagem
        #verificando se o equipamento é do tipo Arma
        elif posicao == 5 and equipamento.regiao == 'Arma':
            equipar = True #autorizando equipagem
        #verificando se o equipamento é do tipo Amuleto
        elif posicao == 6 and equipamento.regiao == 'Amuleto':
            equipar = True #autorizando equipagem
        #verificando se o equipamento é do tipo Anel
        elif posicao == 7 and equipamento.regiao == 'Anel':
            equipar = True #autorizando equiṕagem
        #verificando se a equipagem é válida e o slot está vazio..
        if equipar and self.equipamentos[posicao] == None:
            #retirando equipamento do inventario e equipando no jogador
            self.equipamentos[posicao] = equipamento
            self.inventario.remove(equipamento)
            #atualizando atributos do jogador recem equipado
            self.vida += equipamento.vida
            self.ataque += equipamento.ataque
            return True #sucesso ao equipar item
        else:
            return False #erro ao equipar item

    def retirarArmamento(self, posicao):
        #posicao: int
        #verificando se ha equipamento a ser retirado na posicao dada
        if self.equipamentos[posicao] != None:
            #retirando beneficios do equipamento no jogador
            self.vida -= self.equipamentos[posicao].vida
            self.ataque -= self.equipamentos[posicao].ataque
            #movendo equipamento para o inventario do jogador
            self.inventario.append(self.equipamentos[posicao])
            self.equipamentos[posicao] = None
            return True #sucesso ao retirar item
        else:
            return False #erro ao retirar item
    
    def adicionarItem(self, item):
        #item: objeto do tipo Item
        self.inventario.append(item) #item adicionado ao inventario

    def removerItem(self, item):
        #item: objeto do tipo Item
        self.inventario.remove(item) #item removido do inventario        
    
    #metodos para visualizar informacoes do jogador
    def verPerfil(self):
        print("\n++++++++++  {}  ++++++++++".format(self.nome))
        if (self.titulo != ""):
            print("Titulo: {}".format(self.titulo))
        else:
            print("Titulo: vazio!")
        print("Nivel {} | Exp: {}/{}".format(self.nivel, self.xpAtual, self.nivel*100))
        print("Carteira: {} G".format(self.moedas))
        print("Vida: {}".format("S2 "*self.vida))
        print("Ataque: {}".format(self.ataque))
        print("+++++++++++{}+++++++++++++\n\n".format("+"*len(self.nome)))
    
    def verTitulos(self):
        print("\n===== TITULOS =====")
        for index, titulo in enumerate(self.titulos):
            print("#{} - {}".format(index, titulo))
        print("===================\n\n")

    def verEquipamento(self):
        print("\n========== EQUIPAMENTOS ==========")
        for equip in self.equipamentos:
            if equip is not None:
                print("> {}: {}".format(equip.regiao, equip.nome))
                print("- Descricao: {}".format(equip.info))
                print("- Status: +{} HP | +{} DMG".format(equip.vida, equip.ataque))
                print("- Raridade: {}\n".format(equip.raridade))
        print("==================================\n")

    def verInventario(self):
        numItens = 4 #numero de itens vistos em uma mesma linha
        print("\n========== INVENTARIO ==========")
        for index, item in enumerate(self.inventario):
            if index%numItens == 0 and index != 0:
                print("\n[{}- {}]  ".format(index, item.nome), end='')
            else:
                print("[{}- {}]  ".format(index, item.nome), end='')
        print("\n================================\n\n")

#definicao da classe Equipamento
class Equipamento:
    
    #inicializacando informacoes basicas do equipamento
    def __init__(self, regiao, nome, info, vida, ataque, raridade):
        self.regiao = regiao #string, regiao do corpo
        self.nome = nome #string, nome do equipamento
        self.info = info #string, descricao do equipamento
        self.vida = vida #int, quanto de vida o equipamento dá ao jogador
        self.ataque = ataque #int, quanto de ataque o equipamento dá ao jogador
        self.raridade = raridade #string, quanto mais raro melhor

#definicao da classe Item
class Item:

    #inicializando informacoes basicas do item
    def __init__(self, nome, info, efeito):
        self.nome = nome #string, nome do item
        self.info = info #string, descricao do item
        self.efeito = efeito #string, diz o que o item faz ao ser usado



