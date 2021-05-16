'''
Escreva um programa que escolha aleatoriamente um numero entre 0 e 10, ao qual o
usuario deve tentar adivinhar. O jogo acaba quando o usuario acerta ou quando ele
desiste
'''
import random

alet = random.randint(0, 10)
num = -2

while (num != alet):
    num = (int)(input("Informe um numero: "))
    if ( num != alet):
        print("Sinto muito. {} nao eh o numero aleatorio...".format(num))
    else:
        print("Parabens!!! O numero aleatorio eh {}".format(num))
        
