#crie uma lista
lista1 = []
print("Lista vazia: {}".format(lista1))
lista2 = [1, 2, "meu ovo", [2, 4, 8, 16], 3.14]
print(f"Lista aninhada: {lista2}")
lista3 = list("daniel")
print("Lista a partir de uma string: {}".format(lista3))

#adicionado itens nas listas
lista1.append("dad")
lista2.insert(0, "inicio")
lista3.extend(["israel", "gabriel"])
print("Lista 1: {}\nLista 2: {}\nLista 3: {}\n".format(lista1,lista2, lista3))

#removendo itens de uma lista
lista3.pop()
print("Lista 3 atualizada: ", lista3)
lista2.remove(2)
del lista2[3][1]
print("Lista 2 atualizada: ", lista2)
lista3.clear()
print("Lista 3 totalmente limpa: ", lista3)

#use list slicing para apenas pegar os 3 itens do meio da lista
lista3 = [4, 10, 2, 1, 23]
print(lista3[1:4])
