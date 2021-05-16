#7a) Escreva uma função radical que receba um radical e uma lista de palavras e retorne o
#número de palavras na lista que tenham o radical fornecido.
#Por exemplo, radical(‘part’, [‘partiu’,‘parceiro’,‘mesa’,‘partida’,‘parente’]) deve retornar 2.

def radical(rad, lista):
    tam = len(rad)
    total = 0
    for item in lista:
        for i in range(0, len(item)):
            if ( item[i:i+tam] == rad):
                total += 1
    return total

L = ['partiu', 'em particular', 'parceiro', 'temos essa participaçao', 'mesa', 'partida', 'parente']

print('Número de ocorrências do radical "part" em L:', radical('part', L))
