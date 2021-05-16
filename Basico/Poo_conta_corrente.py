'''
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do
correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos
são obrigatórios.
'''

class Conta:

    def __init__(self, identificacao, dono, saldo = 0):
        self.saldo = saldo
        self.identificacao = identificacao
        self.dono = dono

    def alterarNome(self, nome):
        print("\nNome da conta alterado de '{}' para '{}'".format(self.dono, nome))
        self.dono = nome

    def deposito(self, valor):
        self.saldo += valor
        print("\nR$ {} foram depositados na conta {}!".format(valor, self.identificacao))

    def saque(self, valor):
        if ( self.saldo - valor >= 0):
            self.saldo -= valor
            print("\nSaldo aprovado! Retirando R$ {}".format(valor))
        else:
            print("\nSinto muito! Saldo insuficiente...")
    #Metodo bonus...
    def mostrarConta(self):
        print("\n===========================================")
        print("ID da conta: {}".format(self.identificacao))
        print("Proprietario da conta: {}".format(self.dono))
        print("Saldo disponivel: R$ {}".format(self.saldo))
        print("===========================================")

cliente = Conta("01020409", "Daniel")
#realizando operacoes...
cliente.mostrarConta()
cliente.alterarNome("Daniel Sousa Goncalves")
cliente.saque(10)
cliente.deposito(60)
cliente.saque(30)
cliente.mostrarConta()

        
