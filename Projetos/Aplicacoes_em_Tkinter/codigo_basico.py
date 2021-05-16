from tkinter import *

janela = Tk() #iniciando uma aplicacao em tk, uma janela

janela.title("Janela principal") #alterando nome da janela
janela["background"] = "green" #alterando cor de fundo da janela
#redimensionando tela atraves do parametro "larguraXaltura+PosX+PosY"
janela.geometry("600x400+400+100")

janela.mainloop() #rodando aplicacao, loop principal
