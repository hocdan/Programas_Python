from tkinter import *
from functools import partial
import random

'''
    Aplicacao grafica do jogo Adivinhe o numero!
    
    Um jogo simples de adivinhar o numero conforme a faixa em que se encontra
    A medida que o usuario for dando palpites a faixa vai diminuindo...
'''

#variaveis do jogo
acertou = False
tentativas = 0
menor = 0
maior = 1000
numero = random.randint(menor, maior) #numero aleatorio N, tal que menor <= N <= maior
palpite = ""

#Funcao responsavel pelas acoes
def acao(botao):
    
    global palpite, tentativas, menor, maior, numero, acertou
    
    #identificando qual botao foi acionado e realiando as devidas operacoes...
    
    if ( botao["text"] == "ARRISCAR!"):
        #guardando numero dado pelo usuario, se valido!
        if ( str(entrada.get()).isnumeric()):
            palpite = entrada.get()
        else:
            pass
        #se houver algum numero valido fornecido, comparar...
        if ( palpite != "" and not acertou):
            tentativas += 1
            #se o palpite estiver certo...
            if ( int(palpite) == numero):
                acertou = True
                info1["text"] = "Parabens, voce acertou o numero {}!".format(numero)
            else:
                #calculando novo intervalo com base no ultimo palpite
                if ( (int)(palpite) < numero):
                    menor = palpite
                elif ( (int)(palpite) > numero):
                    maior = palpite
                #atualizando info
                info1["text"] = "O numero se encontra entre {} e {}!".format(menor, maior)
            #atualizando info2, independe do resultado do palpite
            info2["text"] = "Numero de tentativas: {}".format(tentativas)    
    elif ( botao["text"] == "GERAR NOVAMENTE"):
        #gerando novo numero aleatorio e resetando variaveis e informacoes
        acertou = False
        tentativas = 0
        menor = 0
        maior = 1000
        numero = random.randint(menor, maior)
        palpite = ""
        info1["text"] = "O numero se encontra entre {} e {}!".format(menor, maior)
        info2["text"] = "Numero de tentativas: {}".format(tentativas)

janela = Tk() #criando uma janela para a aplicacao

#Criando visores
titulo = Label(janela, text="ADIVINHE O NUMERO!")
titulo.place(x=150, y=20) #posicionando o titulo

info1 = Label(janela, text="O numero se encontra entre {} e {}!".format(menor, maior))
info1.place(x=100, y=50) #posicionando texto informativo

info2 = Label(janela, text="Numero de tentativas: {}".format(tentativas))
info2.place(x=130, y=80) #posicionando texto informativo

#Criando campo de entrada
entrada = Entry(janela)
entrada.place(x=130, y=120)
              
#Criando botoes
botaoArriscar = Button(janela, width=10, height=5, text="ARRISCAR!", command=acao)
botaoArriscar["command"] = partial(acao, botaoArriscar) #vinculando botao a funcao acao
botaoArriscar.place(x=80, y=160) #posicionando botao ARRISCAR!

botaoGerar = Button(janela, width=16, height=5, text="GERAR NOVAMENTE", command=acao)
botaoGerar["command"] = partial(acao, botaoGerar) #vinculando botao a funcao acao
botaoGerar.place(x=200, y=160) #posicionando botao GERAR

#Alterando propriedades da janela
janela.geometry("400x300+500+100")

janela.mainloop() #rodando aplicacao, loop principal

