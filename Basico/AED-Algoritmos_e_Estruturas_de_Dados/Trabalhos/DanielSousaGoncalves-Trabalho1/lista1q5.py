#5a) Escreva uma função chamada espelho que recebe uma strings como parâmetro e anexa o conteúdo da string
#a si mesma em ordem inversa. Por exemplo: [a, b, c] -> [a, b, c, c, b, a].

def espelho(string):
    string2 = string[-1::-1]
    string += string2
    return string

print('Usando função espelho na string "espelho":', espelho('espelho'))