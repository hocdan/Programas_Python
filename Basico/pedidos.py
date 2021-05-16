'''
Escreve um algoritmo que leia o codigo do item pedido, a quantidade e calcule
o valor a ser pafo por aquele lanche. So finaliza se o codigo informado por -999
'''

codigo = 0

while (codigo != -999):
    codigo = input("Informe o codigo do produto:")
    quantidade = (int)(input("Quantidade: "))
    valor = 0
    if ( codigo == "001"):
        valor = quantidade * 2.0
    elif ( codigo == "002"):
        valor = quantidade * 3.25
    elif ( codigo == "003"):
        valor = quantidade * 1.75
    elif ( codigo == "004"):
        valor = quantidade * 10.90
    elif ( codigo == "-999"):
        print("Encerrando programa...")
        break;
    else:
        print("Codigo invalido!!!")
        continue
    print("Valor total a ser pago: R$ {}".format(valor))
