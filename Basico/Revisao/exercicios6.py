#compreensao de listas, dicionarios e conjuntos
l1 = [x * 2 for x in range(1, 11)]
d1 = { chave : valor for chave, valor in enumerate("DANIEL")}
c1 = {letras for letras in "skdkjasdnjnasknd"}

print(f"\nLista={l1}")
print(f"Dicionario={d1}")
print(f"Conjunto={c1}")

#usando compreensao de listas para alterar items em uma matriz
m1 = [ [0, 1, 2], [3, 4, 5], [6, 7, 8] ]
print(f"\nMatriz={m1}")
m2 = [ [item * 2 for item in linha] for linha in m1]
print(f"Matriz duplicada={m2}")
