class Pilha:
    def __init__(self):
        self.items = []
    def empilhar(self, valor):
        self.items.append(valor)
    def desempilhar(self):
        self.items.pop()
    def vazia(self):
        return (self.tamanho() == 0)
    def topo(self):
        if ( self.vazia() ):
            return None
        return self.items[-1]
    def tamanho(self):
        return len(self.items)

p1 = Pilha()
notacao = ''

print('''Comandos válidos:\nE-Empilhar\nD-Desempilhar
V-Verificar se está vazia\nT-Devolve topo da pilha(se existir)
L-Devolve tamanho da pilha\nO-Olhar situação da pilha\nS-Sair do programa\n\nOperações válidas: + - / *\n''')

while (True):
    r = input('Próxima ação: ')
    if ( r == 'E' or r == 'e' ):
        valor = int(input('Digite um valor:'))
        notacao += ' ' + str(valor)
        p1.empilhar(valor)
    elif ( r == 'D' or r == 'd' ):
        p1.desempilhar()
    elif ( r == 'V' or r == 'v' ):
        p1.vazia()
    elif ( r == 'T' or r == 't' ):
        p1.topo()
    elif ( r == 'L' or r == 'l' ):
        p1.tamanho()
    elif ( r == 'O' or r == 'o' ):
        print(p1.items)
    elif ( r == '+' ):
        if ( p1.topo() == None):
            print('Operação inválida!')
        else:
            notacao += ' +'
            op1 = p1.topo()
            p1.desempilhar()
            op2 = p1.topo()
            p1.desempilhar()
            valor = op1 + op2
            p1.empilhar(valor)
    elif ( r == '-' ):
        if ( p1.topo() == None):
            print('Operação inválida!')
        else:
            notacao += ' -'
            op1 = p1.topo()
            p1.desempilhar()
            op2 = p1.topo()
            p1.desempilhar()
            valor = op2 - op1
            p1.empilhar(valor)
    elif ( r == '*' ):
        if ( p1.topo() == None):
            print('Operação inválida!')
        else:
            notacao += ' *'
            op1 = p1.topo()
            p1.desempilhar()
            op2 = p1.topo()
            p1.desempilhar()
            valor = op1 * op2
            p1.empilhar(valor)
    elif ( r == '/' ):
        if ( p1.topo() == None):
            print('Operação inválida!')
        else:
            notacao += ' /'
            op1 = p1.topo()
            p1.desempilhar()
            op2 = p1.topo()
            p1.desempilhar()
            valor = op2/op1
            p1.empilhar(valor)
    elif ( r == 'S' or r == 's' ):
        print('Encerrando programa...')
        print('Notação Polonesa inversa:', notacao)
        break
    else:
        print('Comando inválido!!!Tente novamente...')

'''OBS: EXERCICIO --> Escreva uma função que receba uma string que representa um expressão aritmética em notação RPN e devolva o valor da expressão.
Suponha que os operandos e operadores são separados por espaços em branco. Suponha que cada operando pode ter um número arbitrário de caracteres. Por exemplo,
55.5 33.3 + 22 * 44 66.66 - /'''
        
