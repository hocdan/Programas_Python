# Algoritmo de ordenação Bubble Sort
'''
É um algoritmo de ordenação dos mais simples.
A ideia é percorrer o vector diversas vezes, e a cada passagem fazer flutuar para o topo o maior elemento da sequência.
Essa movimentação lembra a forma como as bolhas em um tanque de água procuram seu próprio nível,
e disso vem o nome do algoritmo.
No melhor caso, o algoritmo executa n operações relevantes, onde n representa o número de elementos do vector.
No pior caso, são feitas n^2 operações.
A complexidade desse algoritmo é de ordem quadrática.
Por isso, ele não é recomendado para programas que precisem de velocidade e operem com quantidade elevada de dados.
'''
#biblioteca para limpar tela
import os

class Bubble_sort():

    def ordenar(self, vetor):
        #loop
        while (True):
            trocas = 0
            #verificando se o da frente é maior, para cada elemento do vetor
            for i in range(len(vetor)-1):
                if ( vetor[i] > vetor[i+1]):
                    temp = vetor[i]
                    vetor[i] = vetor[i+1]
                    vetor[i+1] = temp
                    trocas += 1
                    #mostrando vetor a cada troca
                    self.visualizar(vetor)
            #se não ocorreram trocas já está ordenado...
            if ( trocas == 0):
                break
        return vetor

    def visualizar(self, vetor):
        #visualização por pontos e números (identados)
        print('Bubble Sort em andamento...')
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
                
