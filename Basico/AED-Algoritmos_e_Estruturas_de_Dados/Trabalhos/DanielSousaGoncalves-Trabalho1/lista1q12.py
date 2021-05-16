#12a) Escreva uma função quantidade_negativos que receba uma lista de números inteiros e
#retorne a quantidade de números negativos na lista. Por exemplo, quantidade_negativos([-1,-2,3,4,-5,-6])
#deve retornar 4.

def quantidade_negativos(lista):
    total = 0
    for item in lista:
        if ( item < 0):
            total += 1
    return total

L = [-1, -2, 3, 4, -5, -6]

print('Quantidade de números negativos em L:', quantidade_negativos(L))