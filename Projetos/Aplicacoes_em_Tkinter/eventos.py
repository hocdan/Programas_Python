from tkinter import *
from functools import partial #necessario para a funcao extra
'''
OBS: partial() reescreve uma funcao para que ela possa aceitar
parametros que de outra forma nao poderiam ser passados...como no
caso da criacao de botoes e sua vinculacao com uma funcao, ja que
botao nao pode ser definido por uma instancia dele mesmo!
'''

#funcao botao_clique
def botao_clique(botao):
    if ( botao["text"] == "Botao 1"):
        print("O botao 1 foi clicado!")
    elif ( botao["text"] == "Botao 2"):
        print("O botao 2 foi clicado!")

janela = Tk() #criando uma janela para a aplicacao

#criando botoes e vinculando eles a funcao botao_clique
botao1 = Button(janela, width=10, text="Botao 1")
botao1["command"] = partial(botao_clique, botao1)
botao1.place(x=100, y=100) #setando posicao do botao 1

botao2 = Button(janela, width=10, text="Botao 2")
botao2["command"] = partial(botao_clique, botao2)
botao2.place(x=200, y=100) #setando posicao do botao 2

#alterando propriedades da janela
janela.geometry("400x400+100+100")

janela.mainloop() #rodando aplicacao, loop principal
