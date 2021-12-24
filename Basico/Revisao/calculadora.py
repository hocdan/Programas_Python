#Uma simples calculadora usando os conceitos basicos de Python!!!
import math

#inicio do programa
rodando = True
historico = []
while rodando:
    print("\nCALCULADORA 1.0\n")
    print("1- Calcular")
    print("2- Historico")
    print("3- Sair")
    #testando se entrada fornecida eh valida
    try:
        opcao = int(input("---> "))
    except (TypeError, ValueError):
        print("\nEntrada invalida!!! Tente novamente...")
    else:
        #executando opcoes do menu
        if (opcao == 1):
            #abrindo submenu com as opcoes de calculo
            try:
                num1 = float(input("\nValor 1 = "))
                operacao = input("Operacao (+, -, *, /, ^)= ")
                num2 = float(input("\nValor 2 = "))
            except (TypeError, ValueError):
                print("\nEntrada invalida!!! Tente novamente...")
            else:
                #verificando se operador eh valido e realizando calculo
                if (operacao in ["+", "-", "*", "/", "^"]):
                    if (operacao == "+"):
                        resultado = num1 + num2
                    elif (operacao == "-"):
                        resultado = num1 - num2
                    elif (operacao == "*"):
                        resultado = num1 * num2
                    elif (operacao == "/"):
                        resultado = num1 / num2
                    else:
                        resultado = num1 ** num2
                    print(f"Resultado = {resultado}")
                    historico.append( str(num1) + " " + operacao + " " + str(num2) + " = " + str(resultado))
                else:
                    print("Operacao fornecida eh invalida!!! Tente novamente...")
        elif (opcao == 2):
            #imprimindo historico de calculos
            print("\nHistorico da Calculadora:\n")
            for index, calculo in enumerate(historico):
                print(f"{index+1}. {calculo}")
        elif (opcao == 3):
            #saindo do loop principal
            rodando = False
        else:
            print("\nOpcao invalida!!! Tente novamente...")
print("\nEncerrando programa...\n")

