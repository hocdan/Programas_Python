"""
    Contexto: um programa para verificar a media dos alunos de varias classes,
    onde serao dadas 4 informacoes (ID, Marks, Class, Name) em formato de coluna
    
    INPUT:
    Primeira linha: um numero inteiro N, sendo o total de estudantes;
    Segunda linha: nome das colunas (ID, MARKS, NAME, CLASS) em qualquer ordem;
    Proximas N linhas: contem os valores das respectivas colunas em uma unica
    string;

    OUTPUT:
    Um numero decimal mostrando a media das notas dos estudantes

    OBS: Tentar resolver em 4 linhas ou menos
    
"""
#coletando informacoes
N = int(input())
colunas = [coluna for coluna in input().split(" ") if coluna != ""]
#verificando coluna dos valores de nota e realizando media
media = 0
for i in range(N):
    valores = [valor for valor in input().split(" ") if valor != ""]
    print(valores)
    media += float(valores[colunas.index("MARKS")])
print(media/N)

