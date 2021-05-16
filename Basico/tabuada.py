#Programa que calcula e mostra a tabuada de 1 ate 10

for i in range(1, 11):
    print("=== TABUADA DO {} ===".format(i))
    for j in range(1, 11):
        print("{} X {} = {}".format(i, j, i*j))
