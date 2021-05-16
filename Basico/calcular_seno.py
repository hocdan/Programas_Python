'''
Escreva um programa que calcule e mostre o seno dos angulos entre 0 e 360
Use a funcao sin do pacote math

math.sin(x) -> retorna o seno de x em radianos
math.radians(x) -> converte angulo x de graus para radianos
math.degrees(x) -> converte angulo x de radianos para graus

'''

import math

for i in range(0, 361):
    #calculando seno do angulo em graus (que foram convertidos para radianos)
    angulo = math.sin(math.radians(i))

    print("Seno do angulo {}°: {}".format(i, angulo))
