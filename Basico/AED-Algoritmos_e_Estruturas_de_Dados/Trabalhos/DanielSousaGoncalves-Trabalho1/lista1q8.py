#8a) Escreva uma função palavras_inicio_ﬁm_iguais que receba como entrada uma lista de palavras e retorne
#a quantidade de palavras da lista que possuem 2 ou mais caracteres e cujos primeiro e últimos caracteres
#sejam iguais. Por exemplo, palavras_inicio_ﬁm_iguais([‘aba’, ‘xyz’, ‘aa’, ‘x’, ‘bbb’]) retorna 3.

def palavras_inicio_fim_iguais(lista):
    total = 0
    for item in lista:
        if (len(item) >= 2 and item[0] == item[-1]):
            total += 1
    return total

L = ['aba', 'xyz', 'aa', 'x', 'bbb']

print('Número de palavras com inicio e fim iguais em L:', palavras_inicio_fim_iguais(L))
