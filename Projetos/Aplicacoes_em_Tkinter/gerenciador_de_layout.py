#um gerenciador de layout define a organizacao dos widgets dentro de um container
#1- place: os widgets sao dispostos conforme suas coordenadas x e y (desaconselhavel)
#2- pack: empacota(junta todos) os widgets na horizontal ou vertical (um pouco complicado)
#3- grid: os widgets sao inseridos num sistema de celulas de uma tabela (mais utilizado)

from tkinter import *

janela = Tk() #criando janela da aplicacao
janela.geometry("600x400+100+100") #janela de dimensao 600x400 na posicao (100, 100)

#Adicionando um componente
lb = Label(janela, text="Uma frase qualquer")
lb2 = Label(janela, text="Outra frase qualquer")

#Gerenciando componente
lb.place(x=100, y=100) #com place
lb.place(x=200, y=100) #com place
lb.pack(side=LEFT, expand=True) #com pack
lb2.pack(side=LEFT, expand=True) #com pack
#OBS: para ver o funcionamento de grid abra outro arquivo

janela.mainloop() #rodando aplicacao, loop principal
