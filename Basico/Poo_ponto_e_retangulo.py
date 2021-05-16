'''
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
O valor do centro do objeto deve ser mostrado na tela
Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
'''
#Classe ponto
class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
#Classe retangulo
class Retangulo:

    def __init__(self, Ponto, largura, altura):
        self.x = Ponto.x
        self.y = Ponto.y
        self.largura = largura
        self.altura = altura
        
#Funcao que imprime atributos de ponto
def imprimirPonto(Ponto):
    print("Posicao (x, y) do ponto: ({}, {})".format(Ponto.x, Ponto.y))

#Funcao que encontra o centro de um retangulo
def centroRetangulo(Ret):
    posX = Ret.x + (Ret.largura / 2)
    posY = Ret.y + (Ret.altura / 2)

    return (posX, posY)
#Programa em si

ponto1 = Ponto(0, 0)
ponto2 = Ponto(-1, 2)
ponto3 = Ponto(4, 5)

ret1 = Retangulo(ponto1, 2, 3)
ret2 = Retangulo(ponto2, 1, 5)
ret3 = Retangulo(ponto3, 3, 2)

retangulos = [ret1, ret2, ret3]

while (1):
    
    print("\n1- Ver retangulos")
    print("2- Ver centro do retangulo")
    print("3- Alterar retangulo")
    print("4- Sair")
    
    opcao = input("--> ")

    if (opcao == '1'):
        print("\nLISTA DE RETANGULOS")
        for retangulo in retangulos:
            print("Retangulo = [ ({}, {}), {}, {} ]".format(retangulo.x, retangulo.y, retangulo.largura, retangulo.altura))
    elif (opcao == '2'):
        index = (int)(input("\nInforme o index do retangulo: "))
        temp = centroRetangulo(retangulos[index]) #armazenando ponto
        ponto = Ponto(temp[0], temp[1]) #criando ponto 
        imprimirPonto(ponto) #imprimindo posicao do ponto
    elif (opcao == '3'):
        index = (int)(input("\nInforme o index do retangulo: "))
        retangulos.pop(index) #removendo elemento retangulo da lista
        posX = (float)(input("Nova posicao X do retangulo: "))
        posY = (float)(input("Nova posicao Y do retangulo: "))
        largura = (float)(input("Nova largura do retangulo: "))
        altura = (float)(input("Nova altura do retangulo: "))
        ponto = Ponto(posX, posY) #criando ponto inicial do novo retangulo
        ret = Retangulo(ponto, largura, altura) #criando novo retangulo
        retangulos.insert(index, ret) #armazenando novo retangulo
    elif (opcao == '4'):
        print("\nEncerrando programa...")
        break
    else:
        print("\nOpcao invalida!!!")
