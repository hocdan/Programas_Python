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
        
