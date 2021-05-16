from fila import *
'''Escreva o método Ordenado, da classe Fila, que verifica se os elementos da fila
estão ordenados de maneira crescente, a partir do início da fila.
O método deve retornar True se os elementos estiverem ordenados e False, caso contrário.'''
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
    def ordenado(self):
        ord = True
        for i in range(self.tamanho()-1):
            if ( self.items[i] < self.items[i+1]):
                ord = False
                break
        return ord

f1 = Fila()

f1.enfileirar(1)
f1.enfileirar(2)
f1.enfileirar(3)
print('Ordenado?', f1.ordenado())
f1.enfileirar(5)
print('Ordenado?', f1.ordenado())
f1.enfileirar(6)
print('Ordenado?', f1.ordenado())
f1.enfileirar(2)
print('Ordenado?', f1.ordenado())
