from tkinter import *

'''
funcao responsavel por alterar texto a partir do que foi digitado
na caixa Editar quando o usuario apertar o botao OK
'''
def alterar_texto():
    print("'{}' foi substituido por '{}'".format(texto["text"], entrada.get()))
    texto["text"] = entrada.get()

janela = Tk() #criando uma janela para a aplicacao

#criando widget do tipo Entry(ou seja, que recebe valores)
entrada = Entry(janela)
entrada.place(x=100, y=200) #setando posicao do widget na janela

#criando botoes na janela
botao = Button(janela, width=10, text="OK!", command=alterar_texto)
botao.place(x=100, y=250) #setando posicao do botao OK!

#criando rotulos na janela
texto = Label(janela, text="Um texto qualquer...")
texto.place(x=100, y=100) #setando posicao do texto

#alterando propriedades da janela
janela.geometry("500x500+200+100")

janela.mainloop() #rodando aplicacao, loop principal
