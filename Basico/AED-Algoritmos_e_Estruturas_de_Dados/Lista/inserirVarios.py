'''Considerando as classes No e ListaNaoOrdenada, escreva o método“inserir_varios”
da classe ListaNaoOrdenada que receba uma tupla contendo dois ou maiselementos e
os insira na lista.
Observação: não é permitida a utilização de Listas em Python(da forma [ ])
'''
from EDListas import *

def inserirVarios(valores, lista):
        tam = len(valores)
        i = 0
        
        while ( i < tam):
            lista.inserir(valores[i])
            i += 1
#testando função inserirVarios
lista = ListaNaoOrdenada()
lista.inserir(3)
lista.inserir(2)
lista.inserir(1)
print("Lista antiga:")
lista.imprimir()
print('-------------')
valores = (0, -1, -2, -3)
inserirVarios(valores, lista)
print("Lista nova:")
lista.imprimir()
