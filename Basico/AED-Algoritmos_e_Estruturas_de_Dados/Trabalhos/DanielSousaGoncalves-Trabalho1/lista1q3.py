#3a) Escreva uma função soma_quadrados que receba uma lista de números e retorne a soma dos quadrados
#dos números na lista. Por exemplo, soma_dos_quadrados([2, 3, 4]) deve retorna 4+9+16 que é 29.

def soma_quadrados(lista):
    soma = 0
    for item in lista:
        soma += item**2
    return soma

L = [2, 3, 4]

print('Soma dos quadrados da lista igual a:', soma_quadrados(L))