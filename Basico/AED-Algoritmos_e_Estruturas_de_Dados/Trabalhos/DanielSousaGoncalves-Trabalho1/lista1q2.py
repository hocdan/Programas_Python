#2a) Escreva uma função calcula_minimo_2 que receba como entrada uma lista de números inteiros
#(tamanho mínimo da lista de 3 elementos) e retorna soma dos dois menores valores na lista.
#Por exemplo, calcula_minimo([4,3,6,1,2]) deve retornar 3 (1+2).

def calcula_minimo_2(lista):
    lista.sort()
    soma = lista[0] + lista[1]
    return soma

L = [4, 3, 6, 1, 2]

print('Soma dos dois menores valores de L:', calcula_minimo_2(L))