# Algoritmo de ordenação: Selection Sort
'''
A ordenação por seleção (do inglês, selection sort) é um algoritmo de ordenação
baseado em se passar sempre o menor valor do vetor para a primeira posição
(ou o maior dependendo da ordem requerida), depois o de segundo menor valor
para a segunda posição, e assim é feito sucessivamente com os n-1 elementos
restantes, até os últimos dois elementos.
'''
import os

class Selection_sort():

    def ordenar(self, vetor):
        #percorrendo cada elemento do vetor e comparando com o resto
        for i in range(len(vetor)-1):
            self.visualizar(vetor)
            menor = i
            for j in range(i+1, len(vetor)):
                if ( vetor[j] < vetor[menor]):
                    menor = j
            if ( vetor[menor] != vetor[i]):
                aux = vetor[i]
                vetor[i] = vetor[menor]
                vetor[menor] = aux
        return vetor

    def visualizar(self, vetor):
        #visualização por pontos e números (identados)
        print('Selection Sort em andamento...')
        print('-'*len(vetor))
        for item in vetor:
            if ( item >= 100 and item <= 999):
                print(str(item)+'|',end="")
            elif ( item >= 10 and item <= 99):
                print(str(item)+' |',end="")
            else:
                print(str(item)+'  |',end="")
            for i in range(item):
                print('*',end="")
            print()
        print('-'*len(vetor))
        os.system('cls' if os.name == 'nt' else 'clear')
                
