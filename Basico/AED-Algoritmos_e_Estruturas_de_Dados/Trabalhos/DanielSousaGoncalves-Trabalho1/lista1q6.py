#6a) Escreva uma função quatidade_palavras_8 que receba uma lista de palavras e retorne o número de
#palavras na lista que tenham comprimento 8.
#Por exemplo: quantidade_palavras_8([‘planilha’,‘áreas’,‘dados’,‘Anaconda’,‘Cientista’]) deve retornar 2.

def quantidade_palavras_8(lista):
    total = 0
    for item in lista:
        if ( len(item) == 8):
            total += 1
    return total

L = ['planilha', 'áreas', 'dados', 'Anaconda', 'Cientista']

print('Quantidade de palavras de tamanho 8 na lista:', quantidade_palavras_8(L))