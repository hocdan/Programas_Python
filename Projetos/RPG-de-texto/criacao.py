'''
    Programa que abre a janela de criacao do personagem

    Tem duas funções:

    1- Preencher os dados do jogador e salvá-los em um arquivo
    2- Irá chamar o programa Rota01.py e daí iniciar a jornada
    do jogador no RPG de texto: ?????
'''

from Objetos import *
from time import sleep
import os
import sys


#funcao para limpar a tela
def limpar():
    #para sistemas linux e mac
    if os.name == 'posix':
        _ = os.system('clear')
    #para sistemas windows
    else:
        _ = os.system('cls')

def run():
    #janela de criacao do personagem
    print("\n---------- JANELA DE CRIACAO ----------\n")
    nome = input("> Nome do Heroi: ")
    jogador = Heroi(nome, 1, 0, 0, 10, 5) #criando Heroi
    
    escolhendo = True
    while escolhendo:
        print("\n[Parece que seus parentes deixaram um presente antes de ir embora, aceite-o.]\n")
        print("\n> ESCOLHA UM EQUIPAMENTO INICIAL:\n")
        #escolha de equipamento inicial 
        print("1 -> Uma espada desgastada, 10 moedas de ouro e uma pocao de cura.")
        print("2 -> Uma adaga enferrujada, capuz e 5 moedas de ouro.")
        print("3 -> Um elmo partido, um peitoral velho e 5 moedas de ouro.")
        print("4 -> Um cajado meio quebrado, anel sujo e 5 moedas de ouro.")
        print("5 -> Um saco de moedas e um talisma misterioso.")
        print("(OBS: Não se esqueça de equipá-los depois...)\n")
        escolha = input("-> ")
        
        if escolha == '1':
            print("\nGosta de uma luta, hein?")
            jogador.adicionarTitulo("O ataque é a melhor defesa!")
            #gerando itens do equipamento escolhido e entregando ao Heroi
            espada = Equipamento('Arma', 'Espada desgastada.', 'Presente de família...', 0, 5, 'COMUM')
            pocaoCura = Item('Pocao de Vida', 'Um líquido vermelho de sabor amargo.', 'CURAR')
            jogador.adicionarMoedas(10)
            jogador.adicionarItem(espada)
            jogador.adicionarItem(pocaoCura)
            escolhendo = False
        elif escolha == '2':
            print("\nVamos pela surdina...")
            jogador.adicionarTitulo("Na calada da Noite")          
            #gerando itens do equipamento escolhido e entregando ao Heroi
            adaga = Equipamento('Arma', 'Adaga enferrujada.', 'Presente de família...', 0, 3, 'COMUM')
            capuz = Equipamento('Cabeca', 'Capuz de couro.', 'Presente de família...', 2, 1, 'COMUM')
            jogador.adicionarMoedas(5)
            jogador.adicionarItem(adaga)
            jogador.adicionarItem(capuz)
            escolhendo = False
        elif escolha == '3':
            print("\nAguentar porrada também é importante!")
            jogador.adicionarTitulo("A defesa é o melhor ataque!")  
            #gerando itens do equipamento escolhido e entregando ao Heroi
            elmo = Equipamento('Cabeca', 'Elmo de ferro partido.', 'Presente de família...', 4, 1, 'COMUM')
            peitoral = Equipamento('Peito', 'Peitoral de ferro velho.', 'Presente de família...', 6, 0, 'COMUM')
            jogador.adicionarMoedas(5)
            jogador.adicionarItem(elmo)
            jogador.adicionarItem(peitoral)
            escolhendo = False
        elif escolha == '4':
            print("\nA magia sempre compensa...para quem é bem equipado!")
            jogador.adicionarTitulo("Aprendiz da Magia")
            #gerando itens do equipamento escolhido e entregando ao Heroi
            cajado = Equipamento('Arma', 'Cajado de madeira lascada.', 'Presente de família...', 2, 3, 'COMUM')
            anel = Equipamento('Anel', 'Anel empoeirado por conta do tempo.', 'Presente de família...', 1, 2, 'COMUM')
            jogador.adicionarMoedas(5)
            jogador.adicionarItem(cajado)
            jogador.adicionarItem(anel)
            escolhendo = False
        elif escolha == '5':
            print("\nUma pequena fortuna nunca faz mal.")
            jogador.adicionarTitulo("Apostando tudo e mais um pouco")
            #gerando itens do equipamento escolhido e entregando ao Heroi
            talisma = Item('Talisma', 'Um talisma com formato hexagonal.', 'CHAVE')
            jogador.adicionarMoedas(50)
            jogador.adicionarItem(talisma)
            escolhendo = False
        else:
            print("\nSinto muito mas a sua escolha de equipamento não é válida!!!")

    #salvando dados do jogador em um arquivo a parte, para futuras consultas e edicoes ao longo do jogo
    localArquivo = os.path.join(os.getcwd() + '/Jogador/', 'jogador_'+nome)
    with open(localArquivo, 'w') as arquivo:
        arquivo.write(jogador.nome+'\n')
        arquivo.write(str(jogador.nivel)+'\n')
        arquivo.write(str(jogador.xpAtual)+'\n')
        arquivo.write(str(jogador.moedas)+'\n')
        arquivo.write(str(jogador.vida)+'\n')
        arquivo.write(str(jogador.ataque)+'\n')
        #convertendo lista de equipamentos para o formato de string
        arquivo.write("[\n") #sinalizando inicio da escrita de objetos em uma lista
        for item in jogador.equipamentos:
            #repassando valores individuais de um objeto da lista
            arquivo.write('(') #sinalizando inicio da escrita de um objeto
            if (item != None):
                arquivo.write(item.regiao+'|')
                arquivo.write(item.nome+'|')
                arquivo.write(item.info+'|')
                arquivo.write(str(item.vida)+'|')
                arquivo.write(str(item.ataque)+'|')
                arquivo.write(item.raridade)
            else:
                arquivo.write("VAZIO")
            arquivo.write(')\n') #sinalizando final da escrita de um objeto
        arquivo.write("]\n") #sinalizando final da escrita de objetos em uma lista
        #convertendo lista do inventario para o formato de string
        arquivo.write("[\n") #sinalizando inicio da escrita de objetos em uma lista
        for item in jogador.inventario:
            #repassando valores individuais de um objeto na lista
            arquivo.write('(') #sinalizando inicio da escrita de um objeto
            #verificando se o item no inventario é do tipo EQUIPAMENTO ou ITEM
            if (item != None and type(item) is Equipamento):
                arquivo.write(item.regiao+'|')
                arquivo.write(item.nome+'|')
                arquivo.write(item.info+'|')
                arquivo.write(str(item.vida)+'|')
                arquivo.write(str(item.ataque)+'|')
                arquivo.write(item.raridade)
            elif (item != None and type(item) is Item):
                arquivo.write(item.nome+'|')
                arquivo.write(item.info+'|')
                arquivo.write(item.efeito)
            arquivo.write(')\n') #sinalizando final da escrita de um objeto
        arquivo.write("]\n") #sinalizando final da escrita de objetos em uma lista
        arquivo.write(jogador.titulo+'\n')
        arquivo.write(str(jogador.titulos)+'\n')
        #finalizando criacao e iniciando jornada na rota 1
        print("\nSuas coisas foram salvas, {}!\n".format(jogador.nome))
        print("Adentrando o mundo de Kiurni...\n")
        sleep(2)
        return "rota01"

#executando janela de criacao
if __name__ == '__main__':
    run()


