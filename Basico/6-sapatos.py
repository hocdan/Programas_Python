"""
Contexto: fazer um programa que compute as vendas de sapatos com base nos pedi-
dos dos clientes e se o sapato esta disponivel em estoque

INPUT:
Primeira linha: numero X de sapatos
Segunda linha: uma string com os sapatos de tamanho Y disponiveis separados por
espaco
As proximas N linhas: uma string que representa o sapato que o cliente quer e
quanto ele ira pagar, no formato de "Y X"
Ultima linha: imprimir o valor total ganho na venda de sapatos

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
numSapatos = int(input())
sapatos = input()
#tratando string de sapatos para jogar seus valores em uma lista
lista = sapatos.split(" ")
print(lista)
numClientes = int(input())
#pedido de cada cliente
ganho = 0
for i in range(numClientes):
    pedido = input()
    pedido = pedido.split(" ")
    print("Sapato: {}, valendo R${}".format(pedido[0], pedido[1]))
    #verificando se pedido pode ser atendido e calculando ganho
    if pedido[0] in lista:
        lista.remove(pedido[0])
        ganho += int(pedido[1])
print(ganho)
