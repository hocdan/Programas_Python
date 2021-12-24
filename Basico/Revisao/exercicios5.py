#criando conjuntos
set1 = {1, 3, 2, 3, 2, 4, 5, 1, 1, 6, 7, 8}
set2 = set([0, 2, 4, 8, 16, 32])
set3 = set1.union(set2)

print(f"\nConjunto 1: {set1}")
print(f"\nConjunto 2: {set2}")
print(f"\nConjunto 3: {set3}")

#checando se um elemento se encontra no conjunto
print(f"\nO elemmento 8 se encontra no conjunto 2? {8 in set2}")

#adicionando elementos nos conjuntos
set1.update([-4, -3, -2, -2, -1, 0])
set2.add(64)
print(f"\nConjunto 1: {set1}")
print(f"\nConjunto 2: {set2}")

#itens em comum entre os conjuntos
set4 = set1.intersection(set2)
print(f"\nConjunto interseccao do 1 com o 2: {set4}")
