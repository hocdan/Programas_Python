import os

#Matrizes do jogo
solucao = [ [ " ", " ", "1", " ", " ", " ", " ", " ", "7", " "],
            [ "O", "D", "A", "L", "A", "C", "2", " ", "T", " "],
            [ " ", " ", "B", " ", "5", " ", "6", " ", "R", " "],
            [ " ", " ", "A", " ", "B", " ", "L", " ", "A", " "],
            [ " ", "3", "C", "A", "I", "X", "A", " ", "B", " "],
            [ " ", " ", "A", " ", "R", " ", "G", " ", "A", " "],
            [ " ", " ", "X", " ", "U", " ", "O", " ", "L", " "],
            [ "4", "N", "I", "E", "T", "Z", "S", "C", "H", "E"],
            [ " ", " ", " ", " ", "A", " ", "T", " ", "O", " "],
            [ " ", " ", " ", " ", "8", "M", "A", "S", "S", "A"] ]

cruzada = [ [ " ", " ", "1", " ", " ", " ", " ", " ", "7", " "],
            [ "?", "?", "?", "?", "?", "?", "2", " ", "?", " "],
            [ " ", " ", "?", " ", "5", " ", "6", " ", "?", " "],
            [ " ", " ", "?", " ", "?", " ", "?", " ", "?", " "],
            [ " ", "3", "?", "?", "?", "?", "?", " ", "?", " "],
            [ " ", " ", "?", " ", "?", " ", "?", " ", "?", " "],
            [ " ", " ", "?", " ", "?", " ", "?", " ", "?", " "],
            [ "4", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
            [ " ", " ", " ", " ", "?", " ", "?", " ", "?", " "],
            [ " ", " ", " ", " ", "8", "?", "?", "?", "?", "?"] ]

dicas = [ ["1- A casa do Bob Esponja"],
          ["2- Aquele que apenas escuta, pois esta ___!"],
          ["3- Muito util para guardar coisas"],
          ["4- Nome do filosofo reconhecido por seu bigode xD"],
          ["5- Aquele que nao raciona plenamente, inquieto..."],
          ["6- Crustaceo muito famoso em restaurantes"],
          ["7- Hercules executou 12 deles para ascender ao Olimpo"],
          ["8- Ingrediente comum em receitas italianas"] ]

#Constantes do jogo
n = 10

def mostrarCruzada(cruzada):
    print("\n             CRUZADAS 1.0\n")
    for i in range(n):
        print("===="*n) #barra grande o suficiente para toda a cruzada
        print("|", end="") #barra lateral 
        for j in range(n):
            print(" {} |".format(cruzada[i][j]), end="") #imprimindo sem quebrar a linha
        print("")
    print("===="*n) #barra grande o suficiente para toda a cruzada
    #Mostrando dicas
    for dica in dicas:
        print(dica)

def verificarCruzada(cruzada, solucao):
    errado = False
    for i in range(n):
        for j in range(n):
            if ( cruzada[i][j] != solucao[i][j]):
                errado = True
                break
        if (errado):
            print("\nSinto muito...cruzada errada! Tente novamente ;)\n")
            break
    if ( not errado):
        print("\nParabens! Voce resolveu toda a cruzada :)\n")

def preencherCruzada(cruzada, numero, direcao, palavra):
    palavra = palavra.upper() #convertendo para letra capitular
    #procurando numero na matriz
    for i in range(n):
        for j in range(n):
            if ( cruzada[i][j] == numero):
                if (direcao == 'w'):
                    i -= 1
                elif (direcao == 'a'):
                    j -= 1
                elif (direcao == 's'):
                    i += 1
                elif (direcao == 'd'):
                    j += 1
                pos = [i, j] #armazenando local da pergunta
    #preenchendo palavra no local da pergunta de acordo com o numero e direcao (se possivel)
    for char in palavra:
        if ( (pos[0] >= 0 and pos[0] < n) and (pos[1] >= 0 and pos[1] < n)):
            if (direcao == 'w' and (cruzada[pos[0]][pos[1]] != " " and cruzada[pos[0]][pos[1]] not in "12345678" )):
                cruzada[pos[0]][pos[1]] = char
                pos[0] -= 1 #atualizando local
            elif (direcao == 'a' and (cruzada[pos[0]][pos[1]] != " " and cruzada[pos[0]][pos[1]] not in "12345678" )):
                cruzada[pos[0]][pos[1]] = char
                pos[1] -= 1 #atualizando local
            elif (direcao == 's' and (cruzada[pos[0]][pos[1]] != " " and cruzada[pos[0]][pos[1]] not in "12345678" )):
                cruzada[pos[0]][pos[1]] = char
                pos[0] += 1 #atualizando local
            elif (direcao == 'd' and (cruzada[pos[0]][pos[1]] != " " and cruzada[pos[0]][pos[1]] not in "12345678" )):
                cruzada[pos[0]][pos[1]] = char
                pos[1] += 1 #atualizando local
    

#Menu do jogo
while (True):
    mostrarCruzada(cruzada)
    acao = input("Digite (1-Responder, 2-Verificar, 3-Sair): ")

    if (acao == '1'):
        numero = input("Numero da pergunta: ")
        direcao = input("Direcao do preenchimento (w,a,s,d): ")
        resposta = input("Resposta: ")
        preencherCruzada(cruzada, numero, direcao, resposta)
    elif (acao == '2'):
        verificarCruzada(cruzada, solucao)
    elif (acao == '3'):
        print("\nVolte sempre...\n")
        break
    else:
        print("\nOpcao invalida!!!\n")

    #os.system('cls' if os.name == 'nt' else 'clear') #limpando tela e console Python
    
    

n = input("\nFim de jogo:)\n")
        
