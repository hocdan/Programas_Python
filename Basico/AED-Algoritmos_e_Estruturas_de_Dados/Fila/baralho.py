'''6) Implemente uma o jogo de baralho 21 usando uma fila para o baralho.
http://jogosdecartas.hut.com.br/vinte-e-um/
Primeiro gere as cartas de A até 10 (incluindo K, J, Q) para cada naipe
(copas, paus, espada e ouros); Depois, embaralhe a lista de cartas e
inseria numa fila;
Ao retirar uma carta verique o valor da carta e some os pontos até que
sejam menores ou iguais a 21, se passar de 21 perdeu. O jogador pode
para antes de estourar.
'''
import random
from ED import *

deck = {'♥': [], '♣': [], '♠': [], '♦': []}

def geraBaralho(deck):
    baralho = Fila()
    #preenchendo dicionário
    for chave in deck.keys():
        for num in range(1, 14):
            if ( num == 1):
                deck[chave].append('A')
            elif ( num == 11):
                deck[chave].append('J')
            elif ( num == 12):
                deck[chave].append('Q')
            elif ( num == 13):
                deck[chave].append('K')
            else:
                deck[chave].append(str(num))
    #colocando e embaralhando as cartas em uma lista
    cartas = []
    for k, v in deck.items():
        for item in v:
            cartas.append(item+k)
    random.shuffle(cartas)
    #preenchendo a fila com as cartas
    for carta in cartas:
        baralho.enfileirar(carta)
    return baralho

#puxando cartas e tentando alcançar 21
print('Jogo de Cartas 21!')
pontos = 0
baralho = Fila()
baralho = geraBaralho(deck)
while (True):
    print('Opções:\n1-Puxar uma carta\n2-Parar\n3-Gerar novo baralho\n4-Sair\n')
    acao = int(input('O que deseja fazer: '))
    if ( acao == 1):
        if ( baralho.tamanho() > 0):
            cartaAtual = baralho.desenfileirar()
            print('Carta retirada:', cartaAtual, '\n')
            if ( cartaAtual[0:1] == 'A'):
                pontos += 1
            elif ( cartaAtual[0:1] in ['K', 'J', 'Q'] or cartaAtual[0:2] == '10'):
                pontos += 10
            else:
                pontos += int(cartaAtual[0:1])
        else:
            print('Sem cartas disponíveis! Tente gerar outro baralho...\n')
        if ( pontos == 21):
            print('Você ganhou!!! Atingiu 21 :)\n')
            pontos = 0
        elif ( pontos > 21):
            print('Você perdeu! Atingiu {} pontos...\n'.format(pontos))
            pontos = 0
    elif ( acao == 2):
        print('Você desistiu e atingiu uma pontuação de {} pontos!\n'.format(pontos))
        pontos = 0
    elif ( acao == 3):
        print('Gerando novo baralho...\n')
        baralho = geraBaralho(deck)
    elif ( acao == 4):
        print('Volte sempre...\n')
        break
    else:
        print('Comando inválido!!!\n')
        
    

