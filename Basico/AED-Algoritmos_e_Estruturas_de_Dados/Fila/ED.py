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
    def visualizar(self):
        print(self.items)
