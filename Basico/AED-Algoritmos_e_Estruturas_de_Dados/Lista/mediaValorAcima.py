'''Considerando as classes No e ListaNaoOrdenada, escreva o método
MediaValorAcima da classe ListaNaoOrdenada que calcula a média com base
nos valorescontidos na lista encadeada ordenada e imprime na tela a média
e todos os valores maiores ou iguais à média.
Obs.: não é permitida a utilização de Listas em Python (da forma [ ]).
'''
from EDListas import *

def mediaValorAcima(lista):
    media = 0
    tamanho = lista.tamanho()
    #percorrendo e somando os valores da lista
    noAtual = lista.inicio
    while ( noAtual != None):
        media += noAtual.valor
        noAtual = noAtual.getProximo()
    media = media/tamanho
    #imprimindo apenas os valores maiores ou iguais a media
    noAtual = lista.inicio
    while( noAtual != None):
        if ( noAtual.valor >= media):
            print(str(noAtual.valor) + " ", end="")
        noAtual = noAtual.getProximo()
    print("")

lista = ListaNaoOrdenada()
lista.inserir(10)
lista.inserir(9)
lista.inserir(8)
lista.inserir(7)
lista.inserir(6)
lista.inserir(5)
lista.inserir(4)
lista.inserir(3)
lista.inserir(2)
lista.inserir(1)
print('Lista atual:')
lista.imprimir()
print('-'*30)
print('Valores da lista >= a média:')
mediaValorAcima(lista)
print('-'*30)
