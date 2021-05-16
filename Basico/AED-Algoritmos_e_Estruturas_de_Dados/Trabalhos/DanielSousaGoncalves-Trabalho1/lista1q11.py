#11a) Escreva uma função soma_impares que receba uma lista de números inteiros e retorne
#a soma dos números ímpares na lista. Por exemplo, soma_impares([11,20,36,41,55,6]) deve retornar 107.

def soma_impares(lista):
    soma = 0
    for item in lista:
        if (item%2 != 0):
            soma += item
    return soma

L = [11, 20, 36, 41, 55, 6]

print('Soma dos números ímpares em L:', soma_impares(L))