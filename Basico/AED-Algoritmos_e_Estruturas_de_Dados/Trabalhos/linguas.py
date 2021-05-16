D = {'a':'!', 'b':'@', 'c':'#', 'd':'$', 'e':'%', 'f':'^', 'g':'*', 'h':'&',
     'i':']', 'j':'[', 'k':'~', 'l':';', 'm':'|', 'n':'/', 'o':'0', 'p':'+',
     'q':'£', 'r':'¢', 's':'¬', 't':'}', 'u':'-', 'v':'°', 'w':'\\', 'x':'?',
     'y':'<', 'z':'>', ' ':'_', '0':'o', '1':'m', '2':'u', '3':'b', '4':'t',
     '5':'c', '6':'e', '7':'z', '8':'q', '9':'ç', 'ç':'9', 'á':'1', 'ã':'2',
     'â':'3', 'é':'4', 'ê':'5', 'í':'6', 'ó':'7', 'ô':'8', 'ú':'9'}

def codificador(texto, D):
    texto = texto.lower()
    textoC = []
    for c in texto:
        c == D[c]
        textoC.append(c)
    
    return ''.join(textoC)

def descodificador(texto, D):
    texto2 = []
    for c in texto:
        for k in D.keys():
            if (D[k] == c):
                texto2.append(k)
    return ''.join(texto2)

while (True):
    texto = input('Informe um texto:')
    if ( texto == '.' ):
        print('Volte sempre...')
        break
    texto2 = codificador(texto, D)
    print(texto2)
    resposta = input('Deseja traduzir o texto acima(s/n)?')
    if ( resposta == 's' or resposta == 'S'):
        print(descodificador(texto2, D))
    else:
        print('Volte sempre...')
        break
