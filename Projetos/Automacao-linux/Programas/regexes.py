import re #biblioteca responsavel pelas expressoes regulares

#criando um objeto de expressoes regulares
#para poder encontrar numeros de telefone no formato: XX 9XXXX-XXXX
#OBS: passando uma string bruta (para nao ter que usar \\)
numeroTelRegex = re.compile(r"\d{2} 9\d{4}-\d{4}")

rodando = True
while rodando:
    print("\nIDENTIFICADOR DE PADROES 1.0\n")
    print("[1] Fornecer texto (telefone)")
    print("[2] Fornecer texto (nomes)")
    print("[3] Editar padrao de busca")
    print("[4] Sair")
    opcao = input("----> ")

    if (opcao == '1'):
        numTelefone = input("\nTexto: ")
        #utilizando o metodo search() para encontrar a primeira ocorrencia de uma regex
        identificador = numeroTelRegex.search(numTelefone)
        if ( identificador != None):
            print(f"Telefone encontrado: {identificador.group()}")
        else:
            print(f"Nao ha numero de telefone no texto acima...")
    elif (opcao == '2'):
        textoNomes = input("\nTexto: ")
        #utilizando metodo findall() para encontrar multiplas ocorrencias de uma regex
        identificador = numeroTelRegex.findall(textoNomes)
        if ( identificador != None):
            print(f"Nome(s) encontrado(s): {identificador}")
        else:
            print(f"Nao ha nome(s) no texto acima...")
    elif (opcao == '3'):
        novoRegex = input("Nova expressao regular: ")
        novoRegex.encode('unicode_escape') #transformando string em string bruta
        numeroTelRegex = re.compile(novoRegex) #criando novo objeto de expressoes regulares
        print(f"Nova expressa regular ( {novoRegex} ) gravada no identificador!")
    elif (opcao == '4'):
        rodando = False
    else:
        print("\nOpcao invalida!!! Tente novamente...")
print("\nEncerrando programa...")
