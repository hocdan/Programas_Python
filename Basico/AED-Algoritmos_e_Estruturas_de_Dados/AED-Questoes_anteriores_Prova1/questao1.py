#Dada uma lista L de entrada contendo números inteiros, escreva uma função, em Python,
#chamada remover_repeticoes que retorne uma lista P contendo somente os números inteiros
#que não se repetem na lista L.
#Por exemplo, remover_repeticoes([9,8,8,2,4,2,8,1,2]) deverá retornar [9,4,1].

L = [9, 8, 8, 2, 4, 2, 8, 1, 2]

def remover_repeticoes(L):
    lista = L.copy()
    P = []
    for item in lista:
        achou = 0
        for  item2 in L:
            if (item == item2):
                achou += 1
        if ( achou <= 1):
            P.append(item)
    return P

print(remover_repeticoes(L))
    
        
                         
