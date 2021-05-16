"""
    Contexto: programa que diz quantas vezes e em quais posicoes as palavras de um
    grupo B aparecem/ocorrem em um grupo A

    INPUT:
    Primeira linha: uma string no formato "N M", com N e M referentes ao numero de
    palavras dos grupos A e B, respectivamente;
    Proximas N linhas: contem as palavras do grupo A;
    Proximas M linhas: contem as palavras do grupo B;
    
    OUTPUT:
    Devolva M linhas contendo uma string do tipo "Xi Yi ... Zi" onde as letras sao
    as posicoes da palavra i do grupo B no grupo A, caso nao haja ocorrencia apenas
    imprima -1 na linha;
    
"""
#pegando dimensoes e as convertendo
tamanhos = input().split(" ")
n = int(tamanhos[0])
m = int(tamanhos[1])
#input das N linhas com as palavras do grupo A
grupoA = []
for i in range(n):
    palavraA = input()
    grupoA.append(palavraA)
#input das M linhas com as palavras do grupo B
grupoB = []
for i in range(m):
    palavraB = input()
    grupoB.append(palavraB)
#verificando ocorrencias de B em A e imprimindo resultados
for i in range(m):
    if grupoB[i] in grupoA:
        #percorrendo grupoA e vendo as posicoes das palavras
        for j in range(n):
            if grupoB[i] == grupoA[j]:
                print("{} ".format(j+1), end="")
        print() #quebra de linha
    else:
        print("-1")
    
