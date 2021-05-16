from EDListas import *

'''
testando nó
no1 = No(1)
print(no1.getValor())
print(no1.getProximo())
no1.setProximo(2)
print(no1.getProximo())
no1.setValor(0)
print(no1.getValor())

'''
#testando lista não ordenada

lista = ListaNaoOrdenada()

print('Está vazia?',lista.vazia())
print('Tamanho da lista:',lista.tamanho())
print('Lista atual:', lista.imprimir())
#adicionando nós na lista
print('-----------------------------------')
for i in range(5):
    lista.inserir(i)
    print('Tamanho da lista:',lista.tamanho())
    print('Lista atual:')
    lista.imprimir()
    print('---------------------------------')
# manipulando itens da lista
# Primeiro valor da lista: print(lista.inicio.getValor())
# Segundo valor da lista: print(lista.inicio.getProximo().getValor())
lista.remover(3)
lista.imprimir()


    
    
