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
'''
p1 = Pilha()
print('A pilha não tem elementos?', p1.vazia())
print('Qual o elemento do topo?', p1.topo())
print('Qual o tamanho da pilha?', p1.tamanho())
print(p1.items)
for i in range(10):
    p1.empilhar(i)
    print(p1.items)
print('A pilha não tem elementos?', p1.vazia())
print('Qual o elemento do topo?', p1.topo())
print('Qual o tamanho da pilha?', p1.tamanho())
print('Desempilhando...')
for i in range(p1.tamanho()):
    print(p1.items)
    p1.desempilhar()
print(p1.items)
'''
    
