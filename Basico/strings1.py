'''
Programa que le um nome completo e separa nome e sobrenome, alem de informar
o numero de caracteres e o total de vogais
'''

nome = input("Qual o seu nome? ")
vogais = 0

nome = nome.lower() #convertendo todos os caracteres para nao haver diferencas

for c in nome:
    if ( c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
        vogais += 1

print("\nO nome {} possui {} caracteres, sendo {} vogais!\n".format(nome, len(nome), vogais))

pos = nome.find(' ') #procurando primeira ocorrencia de espaco para separar

print("\nNome: {}\nSobrenome: {}\n".format(nome[:pos], nome[pos:]))

print("\nNome completo ao contrario: {}\n".format(nome[::-1]))

#imprimindo nome completo em forma de escada
print("Nome em formato de escada")
for i in range(0, len(nome)+1):
    print(nome[:i])

