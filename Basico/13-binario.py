import math

n = int(input())
#realizando divisoes para tornar o numero de base 10 em um de base 2
numero = ""
while n > 0:
    resto = n%2
    n = math.floor(n/2)
    
    if resto == 1:
        numero += "1"
    else:
        numero += "0"
print("O numero {} eh igual a {} em binario!".format(n, numero[-1::-1]))
#verificando cadeia de 0s e 1s do numero N na base 2
maior, temp = 0, 0
for digito in numero:
    if digito == "1":
        temp += 1
    else:
        temp = 0
    #vendo se existe nova sequencia maior de 1s
    if temp > maior:
        maior = temp
print("Maior cadeia de 1s igual a: {}!".format(maior))
