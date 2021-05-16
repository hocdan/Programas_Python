# Algoritmo de ordenação Insertion Sort
'''
Insertion Sort, ou ordenação por inserção, é o algoritmo de ordenação que, dado uma estrutura (array, lista)
constrói uma matriz final com um elemento de cada vez, uma inserção por vez.
Assim como algoritmos de ordenação quadrática, é bastante eficiente para problemas com pequenas entradas,
sendo o mais eficiente entre os algoritmos desta ordem de classificação.

Podemos fazer uma comparação do Insertion Sort com o modo de como algumas pessoas organizam um baralho num jogo de cartas.
Imagine que você está jogando cartas. Você está com as cartas na mão e elas estão ordenadas.
Você recebe uma nova carta e deve colocá-la na posição correta da sua mão de cartas, de forma que as cartas obedeçam a
ordenação.

A cada nova carta adicionada à sua mão de cartas, a nova carta pode ser menor que algumas das cartas que você
já tem na mão ou maior, e assim, você começa a comparar a nova carta com todas as cartas na sua mão até
encontrar sua posição correta. Você insere a nova carta na posição correta, e, novamente, sua mão é composta
de cartas totalmente ordenadas.
Então, você recebe outra carta e repete o mesmo procedimento. Então outra carta, e outra, e assim por diante,
até você não receber mais cartas.

Esta é a ideia por trás da ordenação por inserção. Percorra as posições do array, começando com o índice 1 (um).
Cada nova posição é como a nova carta que você recebeu, e você precisa inseri-la no lugar correto no subarray
ordenado à esquerda daquela posição.
'''
#biblioteca para limpar tela
import os

class Insertion_sort():

    def ordenar(self, vetor1):
        #criando vetor auxiliar com o tamanho do original
        vetor2 = []
        for i in range(len(vetor1)):
            vetor2.append(0)

        #Fazendo comparações dos itens do vetor1 com o vetor2 e reordenando
        final = 0
        for i in range(len(vetor1)):
            #caso seja o primeiro item a comparar
            if ( final == 0):
                vetor2[final] = vetor1[i]
                final += 1
                self.visualizar(vetor2)
                continue
            #caso seja maior que o antigo maior
            elif ( vetor1[i] > vetor2[final-1]):
                vetor2[final] = vetor1[i]
                final += 1
                self.visualizar(vetor2)
                continue
            #caso seja menor que o maior atual, irá andar da direita para a esquerda ate ser maior que alguem...
            elif ( vetor1[i] < vetor2[final-1] ):
                temp = final-1
                while ( temp >= 0 and vetor1[i] < vetor2[temp]):
                    vetor2[temp+1] = vetor2[temp]
                    vetor2[temp] = vetor1[i]
                    temp -= 1
                    self.visualizar(vetor2)
                final += 1
        return vetor2

    def visualizar(self, vetor):
        #visualização por pontos e números (identados)
        print('Insertion Sort em andamento...')
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
                
