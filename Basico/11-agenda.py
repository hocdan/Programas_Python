n = int(input())
contatos = {}
for i in range(n):
    dados = input().split(" ")
    contatos[dados[0]] = dados[1]
nomes = []
while True:
    try:
        nome = input()
        if nome == "":
            break
        else:
            nomes.append(nome)
    except EOFError:
        break
for i in range(len(nomes)):
    if nomes[i] in contatos.keys():
        print("{}={}".format(nomes[i], contatos[nomes[i]]))
    else:
        print("Not found")
