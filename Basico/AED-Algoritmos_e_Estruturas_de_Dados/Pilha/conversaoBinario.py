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
            return 'Sem elementos!'
        return self.items[-1]
    def tamanho(self):
        return len(self.items)

p1 = Pilha()

print('Conversor Binário 1.0\n')

numero = int(input('Informe um número:'))

#preenchendo pilha com o resto das divisões sucessivas
resto, n = 1, 1
while ( n != 0):
    n = int(numero / 2)
    resto = numero - (2*n)
    numero = n
    p1.empilhar(resto)
    
#desempilhando para obter a forma binária do número
binario = ''
while ( not p1.vazia() ):
    binario += str(p1.topo())
    p1.desempilhar()
    
print('Forma binária:', binario)
