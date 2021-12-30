#programa que responde frases simples
respostas = { ("qual", "seu", "nome", "como", "chama") : "Olá, me chamo David.", 
("idade", "qual", "anos", "quantos", "tempo") : "Não tenho idade, sou uma I.A que acabou de ser criada...", 
("seu", "trabalho", "funcao", "habilidade", "qual") : "Sirvo apenas para responder e entreter os humanos.",
("como", "clima", "previsão", "tempo", "temperatura") : "Para mim o clima está sempre ensolarado, 38 graus.",
("como", "está", "humor", "seu", "triste") : "Sou uma I.A simples e portanto não sinto nada." }

rodando = True
while rodando:
    #coletando pergunta
    pergunta = input("[David] Me pergunte algo: ")
    #processando pergunta
    pergunta.lower()
    pergunta = pergunta.replace('?', "")
    palavras = pergunta.split()
    #realizando comparacoes
    contador = [0, 0, 0, 0, 0]
    for palavra in palavras:
        index = 0
        for dados in respostas.keys():
            for i in range(5):
                if (palavra == dados[i]):
                    contador[index] += 1
            index += 1
    #respondendo de acordo com a melhor combinacao
    maior = contador.index(max(contador)) #encontra index do maior valor na lista
    if (maior == 0):
        print(respostas[("qual", "seu", "nome", "como", "chama")])
    elif (maior == 1):
        print(respostas[("idade", "qual", "anos", "quantos", "tempo")])
    elif (maior == 2):
        print(respostas[("seu", "trabalho", "funcao", "habilidade", "qual")])
    elif (maior == 3):
        print(respostas[("como", "clima", "previsão", "tempo", "temperatura")])
    elif (maior == 4):
        print(respostas[("como", "está", "humor", "seu", "triste")])
    else:
        print("Não entendi a sua pergunta...")
    #sair ou continuar
    sair = input("Finalizar sessão (S/N)? ")
    if (sair == 'S' or sair == 's'):
        rodando = False
print("[David]  Adeus, amigo!")
print("Encerrando...")