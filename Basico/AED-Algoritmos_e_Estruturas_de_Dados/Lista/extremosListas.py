'''Escreva um método “extremos” da classe ListaNaoOrdenada que cria dois novos
atributos “maior_numero” e “menor_numero” e obtem o maior e o menor elementoda
lista encadeada. Por fim, o método deve retornar uma tupla contendo os valores
dos atributos “maior_numero” e “menor_numero”.
Observação: não é permitida a utilização de Listas emPython (da forma [ ])
'''
from EDListas import *

def extremos(lista):
    extremos = ()
    tam = lista.tamanho()
    i = 0

    noAtual = lista.inicio
    maior = noAtual.getValor()
    menor = noAtual.getValor()
    while ( i < tam):
        if ( noAtual.getValor() > maior):
            maior = noAtual.getValor()
        elif ( noAtual.getValor() < menor):
            menor = noAtual.getValor()
        noAtual = noAtual.getProximo()
        i += 1
    extremos = menor, maior
    return extremos
#testando a função extremos
lista = ListaNaoOrdenada()
lista.inserir(5)
lista.inserir(4)
lista.inserir(7)
lista.inserir(9)
lista.inserir(0)
lista.inserir(-1)
print("Elementos da lista:")
lista.imprimir()
print('-------------------')
print("Menor e maior elementos da lista:", extremos(lista))

    
