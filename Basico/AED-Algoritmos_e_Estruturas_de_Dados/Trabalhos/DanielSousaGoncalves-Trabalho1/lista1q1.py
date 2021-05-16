#1a) Crie uma lista chamada minha_lista com os seguintes itens: “Iron”, 200, “ola”, False, [], -1, 150.
# Para esta lista, escreva os seguintes comandos:

minha_lista = ['Iron', 200, 'ola', False, [], -1, 150]

#A) Inserir “almoço” e 200 no ﬁnal da lista.
minha_lista.append('almoço')
minha_lista.append(200)
print('a)', minha_lista)

#B)  Inserir “unicornio” na posição de índice 2.
minha_lista.insert(2, 'unicornio')
print('b)', minha_lista)

#C)  Inserir 2018 no início da lista.
minha_lista.insert(0, 2018)
print('c)', minha_lista)

#D) Encontrar o índice de “olá”
print('d) Seria impossível encontrar pois a lista não contem a string "olá"')

#E)  Contar o número de ocorrências de 200 na lista.
ocorre = 0
for item in minha_lista:
    if (item == 200):
        ocorre += 1
print('e) O item 200 ocorre {} vezes na lista'.format(ocorre))

#F)  Remover a primeira ocorrência do numero 200 da lista.
for index, item in enumerate(minha_lista):
    if (item == 200):
        del minha_lista[index]
        break
print('f)', minha_lista)
