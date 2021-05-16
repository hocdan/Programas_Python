from tkinter import *

janela = Tk() #criando a janela da aplicacao

#definindo funcao para quando o botao1 for apertado
def clique_botao1():
    print("O botao foi clicado!!!")
    rotulo1["text"] = "MAE DE CLEITON"

#criando botao dentro da janela, de dimensoes 10x5 pixels vinculado a uma funcao 
botao1 = Button(janela, width=10, height=2, text="OK!", command=clique_botao1)
botao1.place(x=100, y=50) #usando um layout para posicionar o widget botao na janela

#criando um rotulo dentro da janela
rotulo1 = Label(janela, text="Alguma coisa...")
rotulo1.place(x=100, y=150)

#alterando propriedades da janela
janela.geometry("400x300+200+100") #setando dimensoes e local da janela
janela["background"] = "gray" #alterando cor de fundo da janela

janela.mainloop() #rodando aplicacao, loop principal
