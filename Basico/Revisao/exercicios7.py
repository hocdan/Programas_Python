#treinando funcoes
def func1(n1, n2, n3):
    maior = n1
    if ( n2 > maior and n2 > n3):
        maior = n2
    elif ( n3 > maior):
        maior = n3
    return maior

def func2_e_3(numeros, operacao='+'):
    #setando valor inicial do acumulador para uso da operacao
    if (operacao == '+'):
        total = 0
    elif (operacao == '*'):
        total = 1
    #realizando operacoes sobre o conjunto de numeros repassados
    for numero in numeros:
        if (operacao == '+'):
            total += numero
        elif (operacao == '*'):
            total *= numero
    return total

def func4(string):
    return string[-1::-1]

def func5(n):
    if (n == 1 or n == 0):
        return 1 #0! = 1 e 1! = 1
    elif (n > 0):
        total = 1
        for i in range(n, 1, -1):
            total *= i
        return total
    else:
        return 0 #fatorial invalido

def func6(num, limMin, limMax):
    pertence = False
    if (num >= limMin and num <= limMax):
        pertence = True
    return pertence

def func7(string):
    numLower, numUpper = 0, 0
    for char in string:
        if ( char.isalpha()): #checando se o charactere pertence ao alfabeto
            if (char.isupper()): #verificando se o char esta em caixa alta
                numUpper += 1
            else:
                numLower += 1
    return (numLower, numUpper)

def func8(lista):
    novaLista = []
    #verificando lista antiga e apenas adicionando itens unicos na nova lista
    for item in lista:
        if (item not in novaLista):
            novaLista.append(item)
    return novaLista

def func9(num):
    ehPrimo = True
    if (num >= 2):
        #verificando possiveis divisoes do numero
        for i in range(2, int((num/2))+1):
            if ( num%i == 0 and i != num):
                ehPrimo = False
                break #numero nao eh primo, busca encerrada
    else:
        ehPrimo = False
    return ehPrimo

def func10(lista):
    novaLista = []
    for item in lista:
        if (item%2 == 0):
            novaLista.append(item)
    return novaLista

#menu principal para testar funcoes
rodando = True
while rodando:
    print("\nTESTANDO FUNCOES 1.0")
    print("[1] Maior dos numeros!")
    print("[2] Somando todos os numeros")
    print("[3] Multiplicando todos os numeros")
    print("[4] Invertendo uma string!")
    print("[5] Calculando o fatorial de N")
    print("[6] Checando se um numero pertence aos limites!")
    print("[7] Verificando letras!")
    print("[8] Criando uma lista unica!")
    print("[9] Encontrando um primo!")
    print("[10] Apenas os pares!")
    print("[0] Sair")
    opcao = input("-----> ")

    if (opcao == '1'):
        #1. Write a Python function to find the Max of three numbers.
        print("\n1. Maior dos numeros!")
        n1 = float(input("Informe o numero 1: "))
        n2 = float(input("Informe o numero 2: "))
        n3 = float(input("Informe o numero 3: "))
        print(f"Maior dos numeros = {func1(n1, n2, n3)}")
    elif (opcao == '2'):
        #2. Write a Python function to sum all the numbers in a list.
        print("\n2. Somando todos os numeros")
        n = int(input("Quantidade de numeros: "))
        lista = []
        for i in range(n):
            lista.append(int(input(f"Informe o numero {i} da lista: ")))
        print(f"Somatorio dos numeros = {func2_e_3(lista, '+')}")
    elif (opcao == '3'):
        #3. Write a Python function to multiply all the numbers in a list.
        print("\n3. Multiplicando todos os numeros")
        n = int(input("Quantidade de numeros: "))
        lista = []
        for i in range(n):
            lista.append(int(input(f"Informe o numero {i} da lista: ")))
        print(f"Produtorio dos numeros = {func2_e_3(lista, '*')}")
    elif (opcao == '4'):
        #4. Write a Python program to reverse a string.
        print("\n4. Invertendo uma string!")
        string = input("Informe uma string qualquer: ")
        print(f"Sua string invertida: {func4(string)}")
    elif (opcao == '5'):
        #5. Write a Python function to calculate the factorial of a number (a non-negative integer). 
        #The function accepts the number as an argument.
        print("\n5. Calculando o fatorial de N")
        n = int(input("Valor de N: "))
        print(f"{n}! = {func5(n)}")
    elif (opcao == '6'):
        #6. Write a Python function to check whether a number falls in a given range.
        print("\n6. Checando se um numero pertence aos limites!")
        num = float(input("Informe um numero qualquer: "))
        min = float(input("Limite minimo do intervalo: "))
        max = float(input("Limite maximo do intervalor: "))
        pertence = func6(num, min, max)
        print("O numero {} pertence ao limite [{}, {}]? {}".format(num, min, max, pertence))
    elif (opcao == '7'):
        """
        7. Write a Python function that accepts a string and calculate the number of upper case letters 
        and lower case letters.
        Sample String : 'The quick Brow Fox'
        Expected Output :
        No. of Upper case characters : 3
        No. of Lower case Characters : 12
        """
        print("\n7. Verificando letras!")
        string = input("Informe uma frase: ")
        print(f"Numero de letras minusculas: {func7(string)[0]}")
        print(f"Numero de letras maiusculas: {func7(string)[1]}")
    elif (opcao == '8'):
        #8. Write a Python function that takes a list and returns a new list with unique elements 
        #of the first list
        print("\n8. Criando uma lista unica!")
        n = int(input("Quantidade de items: "))
        lista = []
        for i in range(n):
            lista.append(input(f"Informe o item {i} da lista: "))
        print(f"Lista dos items unicos: {func8(lista)}")
    elif (opcao == '9'):
        """
        9. Write a Python function that takes a number as a parameter and check the number is prime or not. 
        Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive 
        divisors other than 1 and itself.
        """
        print("\n9. Encontrando um primo!")
        num = int(input("Informe um numero qualquer: "))
        print(f"O numero {num} eh primo? {func9(num)}")
    elif (opcao == '10'):
        """
        10. Write a Python program to print the even numbers from a given list. Go to the editor
        Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
        Expected Result : [2, 4, 6, 8]
        """
        print("\n10. Apenas os pares!")
        n = int(input("Quantidade de numeros: "))
        lista = []
        for i in range(n):
            lista.append(float(input(f"Informe o numero {i} da lista: ")))
        print(f"Lista dos numeros pares: {func10(lista)}")
    elif (opcao == '0'):
        rodando = False
    else:
        print("\nOPCAO INVALIDA!!! Tente novamente...")
print("Encerrando programa...")