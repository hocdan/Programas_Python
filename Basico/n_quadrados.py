#algoritmo que cria uma lista com n quadrados

exp = (int)(input("Informe o expoente: "))
inicio = (int)(input("Menor elemento: "))
fim = (int)(input("Maior elemento: "))

lista = [ x ** exp for x in range(inicio, fim+1)]

print("Sua lista: {}".format(lista))
