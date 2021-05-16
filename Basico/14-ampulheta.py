"""
    Contexto: um programa que descubra a ampulheta em uma matrix 6x6 que tenha
    o maior somatorio de seus elementos. Uma ampulheta eh o conjunto de elementos
    dispostos na matriz da seguinte forma:
                                             
                    a b c    --> linha i; colunas x, x+1, x+2 
                      d      --> linha i+1; coluna x+1
                    e f g    --> linha i+2; colunas x, x+1, x+2
    
    Somatorio = a+b+c+d+e+f+g

    OBS: Fazer isso para todas as ampulhetas possiveis dentro da matriz 6x6 dada
    linha por linha com espacamento entre seus elementos
    OBS2: os valores dos elementos da matriz podem variar de -9 ate +9
"""

#lendo matriz de dados uma linha de cada vez
matriz = []
for i in range(6):
    linha = input().split(" ")
    #adicionando linha a matriz
    matriz.append(linha)
#verificando possiveis ampulhetas na matriz
maior = -64 #valor inicial para comparacao
for i in range(4):
    for j in range(4):
        cima = matriz[i][j:j+3]
        meio = matriz[i+1][j+1:j+2]
        baixo = matriz[i+2][j:j+3]
        #somando valores da ampulheta e vendo se eh o novo maior
        valor = 0
        for num in cima:
            valor += int(num)
        for num in meio:
            valor += int(num)
        for num in baixo:
            valor += int(num)
        print(valor)
        if valor > maior:
            maior = valor
#imprimindo matriz
print("Matriz = {")
for i in range(6):
    for j in range(6):
        print(matriz[i][j], end="")
    print("")
print("}")
print("\nMaior valor de ampulheta: ", maior)
