"""

    Contexto: salvar o conjunto de pares (i, j, k) que estejam nos intervalos
    0 <= i <= x, 0 <= j <= y e 0 <= k <= z e suas componentes nao somem igual a
    N, esse conjunto de pares deve fazer parte das permutacoes de i, j e k;

    INPUT:
    Primeira linha: o valor de x;
    Segunda luinha: o valor de y;
    Terceira linha: o valor de z;
    Quarta linha: o valor de n;

    OUTPUT:
    Deve mostrar a lista com os pares que obedecem as restricoes dadas do inicio;

"""
x = int(input())
y = int(input())
z = int(input())
n = int(input())

pares = []
for i in range(x+1):
    par = []
    par.append(i)
    for j in range(y+1):
        par.append(j)
        for k in range(z+1):
            par.append(k)
            print(par)
            #testando condicoes
            if (par[0]+par[1]+par[2] != n and par not in pares):
                pares.append(par.copy())
                print(pares)
            par.pop()
        par.pop()
print(pares)
