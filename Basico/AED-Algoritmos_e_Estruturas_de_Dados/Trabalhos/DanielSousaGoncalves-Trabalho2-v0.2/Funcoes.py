# coding=utf-8
#funcao que cadastra um livro
from terminaltables import SingleTable

def cadastrar(dic):
    L = []
    
    codigo = input('Codigo do livro:')
    nome = input('Nome:')
    L.append(nome)
    editora = input('Editora:')
    L.append(editora)
    ano = input('Ano:')
    L.append(ano)
    while (True):
        try:
            valor = float(input('Valor pago: R$'))
            ok = True
            break
        except ValueError:
            ok = False
            print ('\nValor inválido!!!\n')
    if ( ok ):
        L.append(valor)
    dic[codigo] = L

#função que altera um livro
def alterar(dic, cod):
    print('Acessando livro...')
    if (cod not in dic.keys()):
        print('Código inválido!')
    else:
        L = []
        nome = input('Novo nome:')
        L.append(nome)
        editora = input('Nova editora:')
        L.append(editora)
        ano = input('Novo ano:')
        L.append(ano)
        valor = float(input('Novo valor pago: R$'))
        L.append(valor)

        dic[cod] = L

#função que exclui um livro
def excluir(dic, cod):
    print('Excluindo livro de código', cod, '...')
    if ( len(dic.keys()) == 0):
        print('''=============================
|   SEM LIVROS CADASTRADOS! |
=============================
              ''')
    elif ( cod not in dic.keys()):
        print('''=============================
|      CÓDIGO INVÁLIDO!     |
=============================
              ''')
    else:
        del dic[cod]
        print('''======================================
|      LIVRO EXCLUÍDO COM SUCESSO    |
======================================
              ''')

#função que localiza um livro
def localizar(dic, cod):
    dados2 = []
    dados2.append(['CÓDIGO', 'TÍTULO', 'EDITORA', 'ANO', 'VALOR PAGO'])
    print('Procurando pelo livro de código', cod, '...')
    if ( len(dic.keys()) == 0):
        print('''=============================
|   SEM LIVROS CADASTRADOS! |
=============================
              ''')
    elif ( cod not in dic.keys()):
        print('''=============================
|      CÓDIGO INVÁLIDO!     |
=============================
              ''')
    else:
        info = dic[cod]
        print('''=====================================
|      INFORMAÇÕES ENCONTRADAS      |
=====================================
''')
        dados2.append([cod, info[0], info[1], info[2], info[3]])
        table = SingleTable(dados2)
        print(table.table)
#função que lista todos os livros cadastrados
def listarGeral(dic):
    dados = []
    dados.append(['CÓDIGO', 'TÍTULO', 'EDITORA', 'ANO', 'VALOR PAGO'])
    print('Acessando dados...\n')
    soma = 0
    if ( len(dic.keys()) == 0):
        print('''=============================
|   SEM LIVROS CADASTRADOS! |
=============================
              ''')
    else:
        print('''==================================
|       LIVROS ENCONTRADOS       |
==================================\n
          ''')
        for k, v in dic.items():
            dados.append([k, v[0], v[1], v[2], v[3]])
            soma += v[3]
        table = SingleTable(dados)
        dados.append(['TOTAL:',len(dic.keys()), '', '', soma])
        table.inner_footing_row_border = True
        print(table.table)