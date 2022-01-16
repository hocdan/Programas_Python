import re #biblioteca responsavel pelas expressoes regulares

#criando um objeto de expressoes regulares
#para poder encontrar numeros de telefone no formato: XX 9XXXX-XXXX
#OBS: passando uma string bruta (para nao ter que usar \\)
numeroTelRegex = re.compile(r"\d{2} 9\d{4}-\d{4}")

rodando = True
while rodando:
    print("\nIDENTIFICADOR DE NUMEROS 1.0\n")
    print("[1] Fornecer texto")
    print("[2] Editar padrao de busca")
    print("[3] Sair")
    opcao = input("----> ")

    if (opcao == '1'):
        numTelefone = input("\nTexto: ")
        identificador = numeroTelRegex.search(numTelefone)
        if ( identificador != None):
            print(f"Telefone(s) encontrado(s): {identificador.group()}")
        else:
            print(f"Nao ha numeros de telefone no texto acima...")
    elif (opcao == '2'):
        novoRegex = input("Nova expressao regular: ")
        novoRegex.encode('unicode_escape') #transformando string em string bruta
        numeroTelRegex = re.compile(novoRegex) #criando novo objeto de expressoes regulares
        print(f"Nova expressa regular ( {novoRegex} ) gravada no identificador!")
    elif (opcao == '3'):
        rodando = False
    else:
        print("\nOpcao invalida!!! Tente novamente...")
print("\nEncerrando programa...")
