'''
Diversos programas para treinar os conceitos de Dicionario

D = {}

D.items() -> retorna uma lista detupla contendo todas as chaves e valores do dicio
nario D

D.keys() -> retorna uma lista com todas as chaves do dicionario D

D.values() -> retorna uma lista com todos os valores do dicionario D

D.clear() -> limpa todo o dicionario D

del D -> remove o dicionario D

len(D) -> retornar o tamanho de D (numero de pares de chaves e valores)

D1.update(D2) -> adiciona os itens do dicionario D2 ao dicionario D1

'''

'''
1) Um programa de agenda telefonica com tamanho definido inicialmente pelo usuario
e que entao devera ser preenchido totalmente para posterior consulta, a qual ira
retornar o numero telefonico de acordo com o nome dado (chave)

agenda = {}
tam = (int)(input("Informe o tamanho da agenda: "))

for i in range(0, tam):
    nome = input("Nome do contato {}: ".format(i+1))
    telefone = input("Telefone do contato {}: ".format(i+1))
    agenda[nome] = telefone #salvando dados na agenda

while (1):
    print("\n====== Agenda ======")
    print("1- Ver contato")
    print("2- Adicionar contato")
    print("3- Excluir contato")
    print("4- Ver agenda")
    print("5- Sair")
    print("====================")

    opcao = input("\n--> ")

    if (opcao == '1'):
        index = input("\nInforme o nome do contato: ")
        print("Telefone de {}: {}".format(index, agenda[index]))
    elif (opcao == '2'):
        nome = input("\nNome do contato: ")
        telefone = input("Telefone do contato: ")
        agenda[nome] = telefone #salvando dados na agenda
    elif (opcao == '3'):
        index = input("\nInforme o nome do contato: ")
        del agenda[index]
        print("Contato de {} excluido com sucesso!".format(index))
    elif (opcao == '4'):
        print("\n====== Agenda ======")
        for (nome, telefone) in agenda.items():
              print("{}: {}".format(nome, telefone))
        print("====================")
    elif (opcao == '5'):
        print("\nEncerrando programa...")
        break
    else:
        print("\nOpcao invalida!!!")
'''

'''
2) Programa que pede que o usuario digite uma frase em portugues e imprima a tra
ducao da frase para a lingua dos piratas

Vocabulario:
senhor = matey  / hotel = fleabag inn/ estudante = swabbie / garoto = matey
madame = proud beaty / professor = foul blaggart / restaurante = galley 
seu = yer / com licenca = arr / estudantes = swabbies / sao = be / e = be
advogado = foul blaggart / o = th' / banheiro = head / meu = me / oi = avast
homem = matey



dicionario = { "matey" : ["senhor", "garoto", "homem"], "fleabag inn" : "hotel",
               "swabbie" : "estudante", "proud beaty" : "madame", "foul blaggart":
               ["professor", "advogado"], "galley" : "restaurante", "yer" : "seu",
               "arr" : "com licenca", "be" : ["sao", "e"], "th'" : "o", "head" :
               "banheiro", "me" : "meu", "avast" : "oi" }

frase = input("Informe uma frase (em portugues): ")
frase = frase.lower()
print(frase.split(' '))

frase2 = ""
juntar = False

for palavra in frase.split(' '):
    traduziu = False
    
    if (juntar):
        palavra = temp + " " + palavra
        juntar = False
    for lista in dicionario.values():
        if ( palavra in lista and type(lista) == list):
            for traducao in dicionario.keys():
                if ( dicionario[traducao] == lista):
                    frase2 = frase2 + " " + traducao
                    traduziu = True
                    break
        elif ( palavra == lista):
            for traducao in dicionario.keys():
                if ( dicionario[traducao] == lista):
                    frase2 = frase2 + " " + traducao
                    traduziu = True
                    break
    if (not traduziu):
            temp = palavra
            juntar = True
        
print("Traducao para o pirata: {}!".format(frase2))
'''

'''
3)Escreva um programa que leia uma string do teclado e retorne uma tabela com a
frequencia com que cada letra aparece na string. Ignore se as letras sao maiscu
las ou minusculas

Exemplo:
Sabendo o que sei e sabendo o que sabes e o que não e o que não sabemos, ambos
saberemos se somos sábios, sabidos ou simplesmente saberemos se somos sabedores.


frase = input("Informe uma frase: ")
frase = frase.lower()

registro = {}

for char in frase:
    if ( char not in registro.keys()):
        registro[char] = 1 #registrando novo char e contabilizando 1
    else:
        for index in registro.keys():
            if ( char == index):
                registro[index] += 1

print("Ocorrencias:\n {}".format(registro))
'''

'''
4)Suponha um dicionario D de estudantes, como definida no exemplo abaixo, onde
cada par consiste do nome do estudante e das notas do mesmo. Escreva uma funcao
chamada "aprovados" que receba como entrada o dicionario D e imprima o nome dos
alunos aprovados. Um aluno eh aprovado quando todas as suas notas sao maiores
que 7



def aprovados( D ):

    for (aluno, notas) in D.items():
        if ( notas[0] > 7 and notas[1] > 7 and notas[2] > 7):
            print(aluno)

    return


dicionario = {"Alano" : (7.5, 8.0, 6.5), "Denise" : (9.0, 8.5, 9.5), "Ana Paula" : (3.5, 1.0, 6.0)}

aprovados(dicionario)
'''
