'''
PROBLEM 4: LONGEST COMMOM PREFIX

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''

def longest_CP(lista) -> str:
    lista2 = [] #segunda lista contendo todas as permutacoes das strings da primeira lista

    #acessando cada string da lista, gerando suas permutacoes e armazenando na segunda lista
    for palavra in lista:
        for x in range(len(palavra)):
            if (x == 0):
                lista2.append(palavra[x])
            elif (palavra[0]+palavra[1:x+1] not in lista2):
                lista2.append(palavra[0]+palavra[1:x+1])
    print(lista2)
    '''
        #com esse metodo nao pegamos apenas prefixos mas tambem sub-cadeias de caracteres
        for x in range(len(palavra)):
            if (palavra[x] not in lista2):
                lista2.append(palavra[x])
            for y in range(x+1, len(palavra)):
                if (palavra[x]+palavra[x+1:y+1] not in lista2):
                    lista2.append(palavra[x]+palavra[x+1:y+1])
        '''

    #verificando qual o prefixo de maior tamanho e se eh comum de todas as palavras
    maiorPrefixComum = ""
    for prefix in lista2:
        comum = True #flag para saber se o prefixo existe dentro das palavras
        for palavra in lista:
            if prefix != palavra[:len(prefix)]:
                comum = False
        #se o prefixo for comum a todas as palavras, tiver tamanho maior que o MPC atual e maior
        if comum and len(prefix) > len(maiorPrefixComum):
            maiorPrefixComum = prefix

    return maiorPrefixComum

lista = ["reflower", "flow", "flight"]
lista2 = ["abca", "aba", "aaab"]
print(longest_CP(lista2))