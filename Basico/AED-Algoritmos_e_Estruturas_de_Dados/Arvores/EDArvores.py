
class No:
    def __init__(self, valor):
        self.valor = valor
        self.dir = None
        self.esq = None

class ArvoreBB:
    def __init__(self):
        self.raiz = None

    def getRaiz(self):
        if ( self.raiz != None):
            return self.raiz.valor
        else:
            return "Arvore vazia..."

    def inserir(self, valor):
        if ( self.raiz == None):
            self.raiz = No(valor)
        else:
            self._inserir(valor, self.raiz)

    def _inserir(self, valor, nodo):
        if ( valor < nodo.valor): #se o valor for menor que o valor do nodo atual...
            if ( nodo.esq == None ): # seo nodo esquerdo estiver vazio...
                nodo.esq = No(valor)
            else: #se o nodo esquerdo estiver preenchido, entao continuar procurando...
                self._inserir(valor, nodo.esq)
        else: #se o valor for maior ou igual ao valor do nodo atual...
            if ( nodo.dir == None): # se o nodo direito estiver vazio...
                nodo.dir = No(valor)
            else: #se o nodo direito estiver preenchido, entao continuar procurando...
                self._inserir(valor, nodo.dir)
                
    def buscar(self, valor):
        if ( self.raiz != None):
            return self._buscar(valor, self.raiz)
        else:
            return None

    def _buscar(self, valor, nodo):
        if ( nodo.valor == valor):
            return True
        elif ( valor < nodo.valor and nodo.esq != None):
            return self._buscar(valor, nodo.esq)
        elif ( valor > nodo.valor and nodo.dir != None):
            return self._buscar(valor, nodo.dir)
        else:
            return False

    def imprimir(self, tipo):
        if (self.raiz != None):
            if ( tipo == 1):
                return self._imprimirPre(self.raiz)
            elif ( tipo == 2):
                return self._imprimirEm(self.raiz)
            elif ( tipo == 3):
                return self._imprimirPos(self.raiz)
        
    def _imprimirPre(self, nodo):
        if ( nodo != None):
            print("(" + str(nodo.valor) + ") ", end="")
            self._imprimirPre(nodo.esq)
            self._imprimirPre(nodo.dir)

    def _imprimirEm(self, nodo):
        if ( nodo != None):
            self._imprimirEm(nodo.esq)
            print("(" + str(nodo.valor) + ") ", end="")
            self._imprimirEm(nodo.dir)

    def _imprimirPos(self, nodo):
        if ( nodo != None):
            self._imprimirPos(nodo.esq)
            self._imprimirPos(nodo.dir)
            print("(" + str(nodo.valor) + ") ", end="")
                
