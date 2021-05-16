'''ITEM escolhido: Livros(Codigo, nome, editora, ano, valorpago)
Funcionalidades implementadas:
• Ao executar o sistema deve mostrar um menu para o usuário digitar quais operação deseja realizar.
• Cadastrar ITEM
• Alterar ITEM
• Excluir ITEM fornecendo o Código
• Localizar um ITEM pelo Código
• Listagem geral dos ITEMS (apresentando a quantidade geral, e o somatório / media dos valores numéricos).
Recomendações:
• Cumprir as Funcionalidades
• Armazenas os dados em listas do Python
• Ter pelo menos dois arquivo .py (um com as funções que executam as funcionalidades) e outro com o arquivo que importa e faz uso das funções.
'''
from Funcoes import *

Livros = {}

print('''Digite a funcionalidade desejada:
[1] CADASTRAR novo livro
[2] ALTERAR um livro existente
[3] EXCLUIR um livro existente
[4] LOCALIZAR um livro pelo código
[5] LISTAGEM de todos os livros cadastrados
[6] SAIR do programa''')

while (True):
    acao = int(input('\nOpção:'))
    if ( acao == 1):
        cadastrar(Livros)
    elif ( acao == 2):
        codigo = input('Informe o código do livro desejado:')
        alterar(Livros, codigo)
    elif ( acao == 3):
        codigo = input('Informe o código do livro desejado:')
        excluir(Livros, codigo)
    elif ( acao == 4):
        codigo = input('Informe o código do livro desejado:')
        localizar(Livros, codigo)
    elif ( acao == 5):
        listarGeral(Livros)
    elif ( acao == 6):
        print('Volte sempre!!!')
        break
    else:
        print('Comando inválido! Tente novamente...')
        
        
