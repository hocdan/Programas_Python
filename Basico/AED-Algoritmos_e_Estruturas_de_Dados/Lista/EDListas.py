class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
    def setValor(self, novo_valor):
        self.valor = novo_valor
        
    def getValor(self):
        return self.valor
    
    def setProximo(self, proximo):
        self.proximo = proximo
        
    def getProximo(self):
        return self.proximo

class ListaNaoOrdenada:
    def __init__(self):
        self.inicio = None
        
    def vazia(self):
        return self.inicio == None
    
    def inserir(self, item):
        temp = No(item)
        temp.setProximo(self.inicio)
        self.inicio = temp

    def buscar(self, item):
        atual = self.inicio
        encontrado = False
        while atual != None and not encontrado:
            if ( atual.getValor() == item):
                encontrado = True
            else:
                atual = atual.getProximo()
        return encontrado

    def tamanho(self):
        atual = self.inicio
        tam = 0
        while atual != None:
            tam += 1
            atual = atual.getProximo()
        return tam

    def imprimir(self):
        atual = self.inicio
        while atual != None:
            print(atual.getValor())
            atual = atual.getProximo()

    def remover(self, item):
        if ( self.inicio.getValor() == item):
            self.inicio = self.inicio.getProximo()
        else:
            previo = self.inicio
            atual = previo.getProximo()
            while ( atual != None):
                if ( atual.getValor() == item ):
                    previo.setProximo(atual.getProximo())
                    break
                else:
                    previo = atual
                    atual = atual.getProximo()

class ListaOrdenada(ListaNaoOrdenada):

    def inserir(self, item):
        atual = self.inicio
        previo = None
        parar = False
        while ( atual != None and not parar):
            if ( atual.getValor() > item):
                parar = True
            else:
                previo = atual
                atual = atual.getProximo()
        temp = No(item)

        if ( previo == None): # é o primeiro
            temp.setProximo(self.inicio)
            self.inicio = temp
        else:
            temp.setProximo(atual)
            previo.setProximo(temp)
            
    def buscar(self, item):
        atual = self.inicio
        encontrou = False
        parar = False
        while (atual != None and not encontrou and not parar):
            if ( atual.getValor() == item):
                encontrou = True
            else:
                if ( atual.getValor() > item):
                    parar = True
                else:
                    atual = atual.getProximo()
        return encontrou
    
