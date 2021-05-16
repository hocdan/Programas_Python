#Algoritmo de ordenação: Quick Sort
'''
O quicksort adota a estratégia de divisão e conquista.
A estratégia consiste em rearranjar as chaves de modo que as chaves "menores"
precedam as chaves "maiores".

Em seguida o quicksort ordena as duas sublistas de chaves menores e maiores
recursivamente até que a lista completa se encontre ordenada. Os passos são:
1-Escolha um elemento da lista, denominado pivô;
2-Particiona: rearranje a lista de forma que todos os elementos anteriores ao
pivô sejam menores que ele, e todos os elementos posteriores ao pivô sejam
maiores que ele. Ao fim do processo o pivô estará em sua posição final e haverá
duas sub listas não ordenadas. Essa operação é denominada partição;
3-Recursivamente ordene a sub lista dos elementos menores e a sub lista dos
elementos maiores;

O caso base da recursão são as listas de tamanho zero ou um, que estão sempre
ordenadas.
O processo é finito, pois a cada iteração pelo menos um elemento é posto em sua
posição final e não será mais manipulado na iteração seguinte.

A escolha do pivô e os passos do Particiona podem ser feitos de diferentes
formas e a escolha de uma implementação específica afeta fortemente a
performance do algoritmo.
'''
import os

class Quick_sort():

    def particao(self, vetor, start, end):
        inicio = start
        fim = end
        pivo = ((inicio+fim+1) // 2)
        while( inicio <= fim ):
            self.visualizar(vetor)
            #incrementando posição inicial enquanto os elementos da esquerda forem menores que o meio(pivô)
            while ( vetor[inicio] < vetor[pivo]):
                inicio += 1
            #incrementando posição final enquanto os elementos da direta forem maiores que o meio(pivô)
            while ( vetor[fim] > vetor[pivo]):
                fim -= 1
            #se o inicio não ultrapasou o meio é porque as "casas" restantes não estão ordenadas, então fazemos trocas entre os elementos da esquerda e direita
            if ( inicio <= fim):
                aux = vetor[inicio]
                vetor[inicio] = vetor[fim]
                vetor[fim] = aux
                inicio += 1
                fim -= 1
            self.visualizar(vetor)
        #se a parte esquerda ainda não andou todo o vetor...
        if ( fim > 0):
            self.particao(vetor, 0, fim)
        #se a parte esquerdd ainda não andou todo o vetor...
        if ( inicio < len(vetor)-1):
            self.particao(vetor, inicio, len(vetor)-1)
        return None
                
    def ordenar(self, vetor):
        inicio = 0
        fim = len(vetor)-1
        pivo = ((inicio + fim+1) // 2)
        print(">>> " + str(pivo))
        while( inicio <= fim ):
            self.visualizar(vetor)
            #incrementando posição inicial enquanto os elementos da esquerda forem menores que o meio(pivô)
            while ( vetor[inicio] < vetor[pivo]):
                inicio += 1
            #incrementando posição final enquanto os elementos da direta forem maiores que o meio(pivô)
            while ( vetor[fim] > vetor[pivo]):
                fim -= 1
            #se o inicio não ultrapasou o meio é porque as "casas" restantes não estão ordenadas, então fazemos trocas entre os elementos da esquerda e direita
            if ( inicio <= fim):
                aux = vetor[inicio]
                vetor[inicio] = vetor[fim]
                vetor[fim] = aux
                inicio += 1
                fim -= 1
            self.visualizar(vetor)
        #se a parte direita ainda não andou todo o vetor...
        if ( fim > 0):
            self.particao(vetor, 0, fim)
        #se a parte esquerda ainda não andou todo o vetor...
        if ( inicio < len(vetor)-1):
            self.particao(vetor, pivo, len(vetor)-1)
        #caso tanto a direita como a esquerda já tenham rodado o vetor todo...
        return vetor

    def visualizar(self, vetor):
        #visualização por pontos e números (identados)
        print('Quick Sort em andamento...')
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
            
       
