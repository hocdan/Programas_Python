#algoritmo para gerenciar uma lista qualquer

lista = []

while (True):
    print("\n=========== MENU ===========")
    print("1- Inserir elemento na lista")
    print("2- Inserir no final da lista")
    print("3- Retirar elemento da lista")
    print("4- Limpar elementos da lista")
    print("5- Ordenar lista")
    print("6- Inverter elementos na lista")
    print("7- Visualizar lista")
    print("8- Visualizar fatia da lista")
    print("9- Sair")
    print("============================")
    
    opcao = input("--> ")

    if (opcao == '1'):
        elemento = input("\nInforme o elemento: ")
        i = (int)(input("Posicao na lista? "))
        lista.insert(i, elemento)
    elif (opcao == '2'):
        elemento = input("\nInforme o elemento: ")
        lista.append(elemento)
    elif (opcao == '3'):
        i = (int)(input("\nPosicao na lista? "))
        lista.pop(i)
    elif (opcao == '4'):
        print("\nLimpando lista...")
        lista.clear()
    elif (opcao == '5'):
        print("\nOrdenando lista...")
        lista.sort()
    elif (opcao == '6'):
        print("\nInvertendo lista...")
        lista.reverse()
    elif (opcao == '7'):
        print("\nTamanho da lista: {}".format( len(lista)))
        print("Lista: {}".format(lista))
    elif (opcao == '8'):
        inicio = (int)(input("\nInicio da fatia: "))
        fim = (int)(input("Final da fatia: "))
        print("Lista[{}:{}]: {}".format(inicio, fim, lista[inicio:fim+1]))
    elif (opcao == '9'):
        print("\nEncerrando programa...")
        break
    else:
        print("Opcao invalida!!!")
    
