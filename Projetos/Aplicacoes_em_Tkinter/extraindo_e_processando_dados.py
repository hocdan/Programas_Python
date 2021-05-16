from tkinter import *

'''
Funcao que ira somar as entradas e gravar o resultado no label
resultado, sempre que o usuario apertar SOMAR
'''
def somar():
    #verificando se os valores passados sao numericos
    if (str(entrada1.get().isnumeric()) and str(entrada2.get().isnumeric())):
        valor1 = (float)(entrada1.get()) #convertendo
        valor2 = (float)(entrada2.get()) #convertendo
        print("{} + {} = {}".format(valor1, valor2, valor1+valor2))
        resultado["text"] = str(valor1+valor2)
    else:
        print("Soma invalida!!!")
        resultado["text"] = "VAZIO"

janela = Tk() #criando janela para a aplicacao

#criando 2 widgets do tipo Entry na janela
entrada1 = Entry(janela)
entrada1.place(x=100, y=100) #setando posicao da entrada 1
entrada2 = Entry(janela)
entrada2.place(x=100, y=130) #setando posicao da entrada 2

#criando 1 widget do tipo Button na janela
botaoSomar = Button(janela, width=20, text="SOMAR", command=somar)
botaoSomar.place(x=100, y=160) #setando posicao do botao Somar

#criando um rotulo para imprimir o resultado
resultado = Label(janela, text="VAZIO")
resultado.place(x=100, y=200) #setando posicao de resultado

#alterando propriedades da janela
janela.geometry("500x500+200+100")

janela.mainloop() #rodando aplicacao, loop principal
