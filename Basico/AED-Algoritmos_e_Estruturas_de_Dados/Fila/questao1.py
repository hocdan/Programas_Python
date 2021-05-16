from pilha import *
'''Escreva o método Inverte, da classe Fila, que inverta os elementos da fila, tal que os
elementos iniciais passem a ser finais e vice-versa. Para fazer a inversão, utilize uma Pilha.'''

class Fila:
    def __init__(self):
        self.items = []
    def enfileirar(self, valor):
        self.items.insert(0, valor)
    def desenfileirar(self):
        return self.items.pop()
    def tamanho(self):
        return len(self.items)
    def vazia(self):
        return (len(items) == 0)
    def frente(self):
        return self.items[-1]
    def inverter(self):
        p1 = Pilha()
        while (self.items != []):
             item = self.frente()
             p1.empilhar(item)
             self.desenfileirar()
        while (not p1.vazia()):
            item = p1.topo()
            self.enfileirar(item)
            p1.desempilhar()
        return self.items
    def verificar(self):
        print(self.items)

f1 = Fila()

f1.enfileirar(1)
f1.enfileirar(2)
f1.enfileirar(3)
f1.enfileirar(4)
f1.enfileirar(5)
f1.verificar()
f1.desenfileirar()
f1.verificar()
f1.inverter()
f1.verificar()

    
