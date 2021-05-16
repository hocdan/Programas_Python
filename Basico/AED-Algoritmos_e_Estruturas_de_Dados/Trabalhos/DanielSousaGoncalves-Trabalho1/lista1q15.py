#15a) Calcule o valor de π usando a série inﬁnita:
# pi = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...
#Construa um dicionário que guarde a quantidade de termos da série e o valor de π correspondente.
#Por exemplo: 1:4, 2: 2.666666666666667, 3: 3.466666666666667 , ....
#Quantos termos da série são necessários para obter 3,14? 3,141? 3,1415? 3,14159?
#OBS: Colocando 140000 termos obtemos todos os valores de pi pedidos
dicionario = {}

vezes = int(input('Quantidade de termos da serie:'))
pi = 4
j = 3
p1, p2, p3, p4 = 0, 0, 0, 0
for i in range(vezes):
    dicionario[i+1] = pi
    if (pi >= 3.14 and pi <= 3.15 and p1 == 0):
        p1 = i
    elif (pi >= 3.141 and pi < 3.142 and p2 == 0):
        p2 = i
    elif (pi >= 3.1415 and pi < 3.1416 and p3 == 0):
        p3 = i
    elif (pi >= 3.14159 and pi <= 3.14160 and p4 == 0):
        p4 = i
    if ( i%2 == 0):
        pi -= (4/j)
    else:
        pi += (4/j)
    j += 2
print(dicionario)
print('Foram precisos {} termos para gerar pi = 3.14'.format(p1))
print('Foram precisos {} termos para gerar pi = 3.141'.format(p2))
print('Foram precisos {} termos para gerar pi = 3.1415'.format(p3))
print('Foram precisos {} termos para gerar pi = 3.14159'.format(p4))
