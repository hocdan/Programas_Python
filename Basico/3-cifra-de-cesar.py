"""
Caesar Cipher (caesar.py)

A Caesar cipher is a simple substitution cipher in which each letter of the
plain text is substituted with a letter found by moving n places down the
alphabet. For example, assume the input plain text is the following:

abcd xyz

If the shift value, n, is 4, then the encrypted text would be the following:

efgh bcd

You are to write a function that accepts two arguments, a plain-text message and
a number of letters to shift in the cipher. The function will return an
encrypted string with all letters transformed and all punctuation and
whitespace remaining unchanged.
"""

def cifra(texto, chave):
    #lista com as letras para futura referencia
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #inicializando variaveis
    textoCifrado = ""
    #percorrendo texto um caractere de cada vez
    for i in range(len(texto)):
        #apenas verificando as letras, ignorando os espacos e pontuacoes
        letra = texto[i]
        if letra in alfabeto:
            posicao = alfabeto.index(letra) #descobrindo posicao da letra no alfabeto
            #calculando nova posicao da letra conforme a chave informada
            if posicao+chave > len(alfabeto):
                novaPosicao = (posicao+chave)-len(alfabeto)
            else:
                novaPosicao = posicao+chave
            #com a nova posicao, verificar qual sera a nova letra e entao substituir
            novaLetra = alfabeto[novaPosicao]
            textoCifrado += novaLetra
        else:
            textoCifrado += letra
    #devolvendo o texto cifrado
    return textoCifrado

#Iniciando programa
while True:
    print("CIFRA DE CESAR 1.0")
    opcao = int(input("1- Cifrar texto\n2-Sair\n-> "))
    #abrindo menu e realizando as funcoes do programa
    if opcao == 1:
        texto = input("Insira o texto a ser cifrado: ")
        chave = int(input("Informe a chave da cifra: "))
        texto = cifra(texto, chave)
        #imprimindo resultado
        print("Seu texto na cifra de Cesar: {}\n".format(texto))
    elif opcao == 2:
        print("Encerrando programa...\n")
        break
    else:
        print("Opcao invalida! Tente novamente...\n")
    

