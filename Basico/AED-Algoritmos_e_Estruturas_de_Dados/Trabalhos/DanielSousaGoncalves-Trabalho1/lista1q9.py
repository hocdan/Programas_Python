#9a) Um triângulo retângulo pode ter lados cujos comprimentos são todos inteiros.
#O conjunto de três valores inteiros para os comprimentos dos lados de um triângulo retângulo é chamado de
#Tripla de Pitágoras. Os comprimentos dos três lados devem obedecer à relação de que a soma dos quadrados de
#dois dos lados é igual ao quadrado da hipotenusa. Escreva um programa para identiﬁcar todas as triplas de
#Pitágoras para lado1, lado2 e hipotenusa, não maiores que 500. Utilize um método de força bruta, com um loop
#for triplamente aninhado que tenta todas as possibilidades.

total = 0
for i in range(1, 501):
    for j in range(1, 501):
        for k in range(1, 501):
            if ( (k*k == i*i + j*j) or (j*j == i*i + k*k) or (i*i == j*j + k*k)):
                print('Tripla de Pitágoras encontrada: {} {} {}'.format(i, j, k))
                total += 1
print('Total de possibilidades:', total)
