'''Considerando listas não ordenada de valores inteiros, implemente uma função chamada
separa que receba como parâmetro uma lista da classe ListaNaoOrdenada e um valor inteiro
n e divida a lista em duas, de tal forma que a segunda lista comece no primeiro nó logo
após a primeira ocorrência de n na lista original.
'''
from EDListas import *

def separaListas( lista1, n):
        if ( lista1.buscar(n) ):
            
            lista2 = ListaNaoOrdenada()
            i = 0
            achou = False
            #começando do inicio da lista1
            noAtual = lista1.inicio
            tam = lista1.tamanho()

            #preenchendo a lista2 a partir dos nós da lista1 que vem depois do nó n
            while ( i <  tam):
                #se achou então inserimos o que vem depois do nó n
                if ( noAtual.getValor() == n):
                    achou = True
                #se ja achamos o nó n então inserimos o nó atual
                elif ( achou ):
                    lista2.inserir( noAtual.getValor())
                #passando para o próximo nó
                noAtual = noAtual.getProximo()
                i += 1 #incrementando o contador
            #"cortando" os nós que vem depois do item n da lista1
            noAtual = lista1.inicio
            while ( True ):
                if ( noAtual.getValor() == n):
                    noAtual.setProximo(None)
                    break
                else:
                    noAtual = noAtual.getProximo()
            #imprimindo os elementos da duas listas...
            print("Elementos da lista 1:")
            lista1.imprimir()
            print('-----------------------')
            print("Elementos da lista 2:")
            lista2.imprimir()
        else:
            return 'Elemento não encontrado na lista!!!'
#testando a função
lista1 = ListaNaoOrdenada()
lista1.inserir(5)
lista1.inserir(4)
lista1.inserir(3)
lista1.inserir(2)
lista1.inserir(1)
lista1.inserir(0)
print("Lista 1 antiga:")
lista1.imprimir()
print('-----------------------------')
print("Aplicando função...")
separaListas(lista1, 0)
        
