'''
    O comando with toma conta de erros e fechamento do arquivo,
    alem de suporta o modo em que se irá manipular o arquivo co-
    mo:

    'r'/reading
    'w'/writing(overwriting)
    'rb'/'wb'(binary mode para ler ou escrever)
    'a'/appending(acrescentar dados sem dar overwriting)

    E a opção '+' que quando combinada com as outras extende suas funções

    OBS: alguns metodos uteis na manipulacao de arquivos
    1) os.rename(nome_antigo_do_arquivo, nome_novo_do_arquivo)
    2) os.remove(nome_do_arquivo_a_ser_excluido)
    3) os.mkdir(nome_do_diretorio_a_ser_criado)
    4) os.chdir(caminho_para_o_diretorio_de_destino)
    5) os.getcwd() #retorna o diretorio atual
    6) os.rmdir(nome_do_diretorio_a_ser_excluido) #deve estar vazio
'''

nome = input("Nome do arquivo a ser criado: ")
with open(nome+'.txt', 'w') as arquivo:
    #processando arquivo no modo de escrita
    print("Informe o caractere $ para finalizar a escrita!\n")
    dados = ''
    while True:
        dados = input('>')
        if dados != "$":
            arquivo.write(dados+'\n')
        else:
            break

with open(nome+'.txt', 'r') as arquivo:
    #processando arquivo no modo de leitura
    print("\nAbrindo arquivo...\n\n" + arquivo.read()) #imprime todo o arquivo
    '''
        Outras maneira de ler todas as linhas do arquivo:
        1)
        for linha in arquivo:
            print(linha, end='')
        2)
        lista = list(arquivo) #vai armazenar as linhas como elementos de lista
        print("Formato de lista: ", lista)
    '''
print("Finalizando programa...")

