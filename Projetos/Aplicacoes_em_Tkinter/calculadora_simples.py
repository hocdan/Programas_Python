from tkinter import *
from functools import partial

'''
Programa simples que simula uma calculadora com operacoes basicas de:
-Somar, Subtrair, Multiplicar e Dividir
OBS:Por enquanto sem operacoes complexas envolvendo parenteses
'''
calculo = "" #string contendo dados da operacao (global)

#Funcao responsavel por calcular tudo
def calcular(botao):
    global calculo
    #identificando que botao foi acionado e realizando as devidas operacoes...
    if ( botao["text"] == "DEL"):
        calculo = calculo[0:len(calculo)-1]
        visor["text"] = calculo
    elif ( botao["text"] == "LIMPAR"):
        calculo = ""
        visor["text"] = "DIGITE ALGO PARA CALCULAR"
    elif ( botao["text"] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]):
        calculo = calculo + botao["text"] #concatenando digito numerico
        visor["text"] = calculo
    elif ( botao["text"] in ["+", "-", "*", "/"]):
        if (len(calculo) == 0 and botao["text"] in ["+", "-"]):
            calculo = calculo + botao["text"] + " " #concatenando operacao inicial
        elif (len(calculo) == 0 and botao["text"] in ["*", "/"]):
            pass #ignorando concatenacao, pois operacao nao faz sentido...
        else:
            calculo = calculo + " " + botao["text"] + " " #concatenando demais operacoes
        visor["text"] = calculo
    else:
        #se houver algo para calcular...e a operacao for valida...
        if (len(calculo) > 0 and calculo[-1] != " "):
            #separando a string por espacos em branco e analisando operacoes
            dados = calculo.split(' ')
            print(dados) #debug
            #percorrendo lista de dados e realizando operacoes de acordo
            resultado = 0
            pular = False
            for i in range(len(dados)):
                if (pular):
                    pular = False
                    continue
                print(dados[i]) #debug
                if (dados[i] not in ["+", "-", "*", "/"]):
                    resultado += (float)(dados[i])
                    pular = False
                else:
                    if (dados[i] == '+'):
                        resultado = resultado + (float)(dados[i+1])
                    elif (dados[i] == '-'):
                        resultado = resultado - (float)(dados[i+1])
                    elif (dados[i] == '*'):
                        resultado = resultado * (float)(dados[i+1])
                    elif (dados[i] == '/'):
                        resultado = resultado / (float)(dados[i+1])
                    #pulando iteracao para que nao repita o numero
                    pular = True
                    
            #atualizando visor com resultado de toda a operacao
            visor["text"] = str(resultado)
        
    
janela = Tk() #criando uma janela para a aplicacao

#Criando visor
visor = Label(janela, text="DIGITE ALGO PARA CALCULAR")
visor.place(x=20, y=40) #posicionando visor

#Criando botoes
botaoLimpar = Button(janela, width=10, height=7, text="DEL", command=calcular)
botaoLimpar["command"] = partial(calcular, botaoLimpar) #vinculando botao a funcao calcular
botaoLimpar.place(x=240, y=0) #posicionando botao DEL

botaoLimparTudo = Button(janela, width=10, height=7, text="LIMPAR", command=calcular)
botaoLimparTudo["command"] = partial(calcular, botaoLimparTudo) #vinculando botao a funcao calcular
botaoLimparTudo.place(x=320, y=0) #posicionando botao LIMPAR

botao0 = Button(janela, width=10, height=5, text="0", command=calcular)
botao0["command"] = partial(calcular, botao0) #vinculando botao a funcao calcular
botao0.place(x=240, y=270) #posicionando botao 0

botao1 = Button(janela, width=10, height=5, text="1", command=calcular)
botao1["command"] = partial(calcular, botao1) #vinculando botao a funcao calcular
botao1.place(x=0, y=100) #posicionando botao 1

botao2 = Button(janela, width=10, height=5, text="2", command=calcular)
botao2["command"] = partial(calcular, botao2) #vinculando botao a funcao calcular
botao2.place(x=80, y=100) #posicionando botao 2

botao3 = Button(janela, width=10, height=5, text="3", command=calcular)
botao3["command"] = partial(calcular, botao3) #vinculando botao a funcao calcular
botao3.place(x=160, y=100) #posicionando botao 3

botao4 = Button(janela, width=10, height=5, text="4", command=calcular)
botao4["command"] = partial(calcular, botao4) #vinculando botao a funcao calcular
botao4.place(x=0, y=185) #posicionando botao 4

botao5 = Button(janela, width=10, height=5, text="5", command=calcular)
botao5["command"] = partial(calcular, botao5) #vinculando botao a funcao calcular
botao5.place(x=80, y=185) #posicionando botao 5

botao6 = Button(janela, width=10, height=5, text="6", command=calcular)
botao6["command"] = partial(calcular, botao6) #vinculando botao a funcao calcular
botao6.place(x=160, y=185) #posicionando botao 6

botao7 = Button(janela, width=10, height=5, text="7", command=calcular)
botao7["command"] = partial(calcular, botao7) #vinculando botao a funcao calcular
botao7.place(x=0, y=270) #posicionando botao 7

botao8 = Button(janela, width=10, height=5, text="8", command=calcular)
botao8["command"] = partial(calcular, botao8) #vinculando botao a funcao calcular
botao8.place(x=80, y=270) #posicionando botao 8

botao9 = Button(janela, width=10, height=5, text="9", command=calcular)
botao9["command"] = partial(calcular, botao9) #vinculando botao a funcao calcular
botao9.place(x=160, y=270) #posicionando botao 9

botaoSoma = Button(janela, width=10, height=5, text="+", command=calcular)
botaoSoma["command"] = partial(calcular, botaoSoma) #vinculando botao a funcao calcular
botaoSoma.place(x=240, y=100) #posicionando botao +

botaoSub = Button(janela, width=10, height=5, text="-", command=calcular)
botaoSub["command"] = partial(calcular, botaoSub) #vinculando botao a funcao calcular
botaoSub.place(x=320, y=100) #posicionando botao -

botaoMult = Button(janela, width=10, height=5, text="*", command=calcular)
botaoMult["command"] = partial(calcular, botaoMult) #vinculando botao a funcao calcular
botaoMult.place(x=240, y=185) #posicionando botao X

botaoDiv = Button(janela, width=10, height=5, text="/", command=calcular)
botaoDiv["command"] = partial(calcular, botaoDiv) #vinculando botao a funcao calcular
botaoDiv.place(x=320, y=185) #posicionando botao /

botaoIgual = Button(janela, width=10, height=5, text="=", command=calcular)
botaoIgual["command"] = partial(calcular, botaoIgual) #vinculando botao a funcao calcular
botaoIgual.place(x=320, y=270) #posicionando botao =

#Alterando propriedades da janela
janela.geometry("400x355+100+50")

janela.mainloop() #rodando aplicacao, loop principal
