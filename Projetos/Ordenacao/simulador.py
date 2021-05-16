#Simulador dos algoritmos de ordenação

#Importando biblioteca para geração de números aleatórios
import random

#Importando algoritmos de ordenação
from bubble_sort import *
from insertion_sort import *
from selection_sort import *
from quick_sort import *

#Programa principal
while (True):
    
    print('Algoritmos de ordenação 1.0\n')
    
    #Criando e embaralhando vetor com números aleatórios
    n = int(input('Total de elementos:'))
    lista = [item for item in range(1,n+1)]
    random.shuffle(lista)
    
    #Aplicando o algoritmo
    print('\nAlgoritmos disponíveis:')
    print('1-Bubble Sort')
    print('2-Insertion Sort')
    print('3-Selection Sort')
    print('4-Quick Sort')
    acao = int(input('-->'))
    if ( acao == 1):
        bolha = Bubble_sort()
        lista = bolha.ordenar(lista)
    elif ( acao == 2):
        insercao = Insertion_sort()
        lista = insercao.ordenar(lista)
    elif ( acao == 3):
        selecao = Selection_sort()
        lista = selecao.ordenar(lista)
    elif ( acao == 4):
        rapido = Quick_sort()
        lista = rapido.ordenar(lista)
    else:
        print('Escolha inválida...')
    #Mostrando resultado final
    print(lista)
    #Continuar?
    resposta = input('Ordenar novamente(s/n)?')
    if ( resposta == 'n' or resposta == 'N'):
        break
