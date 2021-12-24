#criando um dicionario
d1 = {"Nome" : "Daniel SG", "Idade" : 22, "Hobbies" : ["Livros", "Animes", "Jogos"] }
d2 = {} #um dicionario vazio
lista = [("Nome", "Gabriel SG"), ("Idade", 19), ("Hobbies", ["Jogos", "YouTube"])]
d3 = dict(lista) #dicionario a partir de uma lista de tuplas

print("\nDicionario 1 -> {}".format(d1))
print("Dicionario 2 -> {}".format(d2))
print(f"Dicionario 3 -> {d3}")

#alterando valores dos dicionarios
d1["Nome"] = "Daniel S Goncalves"
d2["Telefone"] = "********"
d2["Casa"] = 16
d2["Endereco"] = "Rua Bacanga"
d2.update( [("Moradora", "Fatima"), ("Condominio", "Ed.Omega")] )
del d3["Hobbies"][0]
item = d1.popitem()
item2 = d2.pop("Telefone")
print("\nDicionario 1 -> {}".format(d1))
print("DIcionario 2 -> {}".format(d2))
print(f"Dicionario 3 -> {d3}")
print(f"Item removido do dicionario 1: {item}")
print(f"Item removido do dicionario 2: {item2}")

#resgatando apenas as chaves e apenas os valores dos dicionarios
print(f"\nChaves do dicionario 1: {d1.keys()}")
print(f"Chaves do dicionario 2: {d2.keys()}")
print(f"Chaves do dicionario 3: {d3.keys()}")
print(f"Valores do dicionario 1: {d1.values()}")
print(f"Valores do dicionario 2: {d2.values()}")
print(f"Valores do dicionario 3: {d3.values()}")

#resgatando os pares (key, value) dos dicionarios
print(f"\nItens do dicionario 1: {d1.items()}")
print(f"Itens do dicionario 2: {d2.items()}")
print(f"Itens do dicionario 3: {d3.items()}")

#verificando se chaves e valores estao no dicionario
chave = "Nome"
valor = 16
print(f"\nA key {chave} esta no dicionario 1? {chave in d1.keys()}")
print(f"O value {valor} esta no dicionario 1? {valor in d1.values()}")
print(f"\nA key {chave} esta no dicionario 2? {chave in d2.keys()}")
print(f"O value {valor} esta no dicionario 2? {valor in d2.values()}")

