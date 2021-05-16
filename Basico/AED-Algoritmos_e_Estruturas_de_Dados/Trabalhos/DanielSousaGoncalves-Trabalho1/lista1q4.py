#4a) Crie uma função seleciona_alunos, que recebe uma lista de alunos e um valor inteiro correspondente
#a sua nota (Ex: [[‘Pedro’, 8], [‘Maria’, 9.5 ], ... ]), e retira todos os alunos da lista que possuem
#nota menor que 7.

def seleciona_alunos(lista):
    for i in range(len(lista)-1):
        if (lista[i][1] < 7):
            del lista[i]
    return lista

L = [ ['Pedro', 8], ['Maria', 9.5], ['Joao', 6.5], ['Antonio', 7], ['Paulo', 5.4]]

print('Lista atualizada com alunos de média >= 7:', seleciona_alunos(L))