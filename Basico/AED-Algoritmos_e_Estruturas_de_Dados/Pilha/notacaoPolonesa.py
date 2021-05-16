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
    if ( p1.topo() not in ['+', '-', '*', '/'] and p1.tamanho() >= 2):
        op2 = p1.topo()
        p1.desempilhar()
        if ( p1.topo() not in ['+', '-', '*', '/'] ):
            op1 = p1.topo()
            for i in p1.items[::-1]:
                p1.desempilhar()
                if ( i == '+' ):
                    valor = op1 + op2
                    p1.empilhar(valor)
                    break
                elif ( i == '-' ):
                    valor = op1 - op2
                    p1.empilhar(valor)
                    break
                elif ( i == '*' ):
                    valor = op1 * op2
                    p1.empilhar(valor)
                    break
                elif ( i == '/' ):
                    valor = op1 / op2
                    p1.empilhar(valor)
                    break
        else:
            p1.empilhar(op2)
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
        p1.empilhar(r)
        notacao += ' +'
    elif ( r == '-' ):
       p1.empilhar(r)
       notacao += ' -'
    elif ( r == '*' ):
       p1.empilhar(r)
       notacao += ' *'
    elif ( r == '/' ):
       p1.empilhar(r)
       notacao += ' /'
    elif ( r == 'S' or r == 's' ):
        print('Encerrando programa...')
        print('Notação Polonesa:', notacao)
        break
    else:
        print('Comando inválido!!!Tente novamente...')
