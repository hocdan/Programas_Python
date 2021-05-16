'''Escreva o método MultiplicaImpar da classe ListaNaoOrdenada que
retorna o somatório dos elementos pares da lista encadeada.
'''
from EDListas import *

def multiplicaImpar(lista):
    somatorio = 0
    noAtual = lista.inicio
    i = 0
    tam = lista.tamanho()
    
    while( i < tam):
        if ( noAtual.getValor()%2 == 0):
            somatorio += noAtual.getValor()
        noAtual = noAtual.getProximo()
        i += 1
    return somatorio
#testando a função multiplicaImpar
lista = ListaNaoOrdenada()
#lista.inserir(10)
lista.inserir(9)
lista.inserir(8)
lista.inserir(7)
#lista.inserir(6)
lista.inserir(5)
lista.inserir(4)
lista.inserir(3)
#lista.inserir(2)
lista.inserir(1)
lista.inserir(0)
print("Elementos da lista:")
lista.imprimir()
print('-------------------')
print("Somatório dos elementos pares igual a: ", multiplicaImpar(lista))

