#função que cadastra um livro
def cadastrar(dic):
    L = []
    
    codigo = input('Código do livro:')
    nome = input('Nome:')
    L.append(nome)
    editora = input('Editora:')
    L.append(editora)
    ano = input('Ano:')
    L.append(ano)
    valor = float(input('Valor pago: R$'))
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
|    NOME    | {}
=====================================
|   EDITORA  | {}
=====================================
|     ANO    | {}
=====================================
|    VALOR   | {}
=====================================
'''.format(info[0], info[1], info[2], info[3]))
#função que lista todos os livros cadastrados
def listarGeral(dic):
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
            print('''==================
|      LIVRO     | {}
==================
|      NOME      | {}
==================
|     EDITORA    | {}
==================
|       ANO      | {}
==================
|   VALOR PAGO   | {}
==================
              '''.format(k, v[0], v[1], v[2], v[3]))
            soma += v[3]
        print('''===================
| TOTAL DE LIVROS | {}
===================
|   VALOR TOTAL   | {}
===================
         '''.format( len(dic.keys()), soma))
        
