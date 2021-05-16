#10a) Escreva uma função troca que receba três strings str1, velho e novo e troca em str1 todas as
#ocorrências de velho por novo. Por exemplo, troca(‘Um alunos, dois alunos, tres alunos.’,‘aluno’,‘estudante’)
#deve retornar a string ‘Um estudante, dois estudante, tres estudantes.’.
#Observação: existe a função replace que faz isso, mas você não deve usá-la. (Dica: use os métodos split e join).

def troca(string, velho, novo):
    string2 = string.split(velho)
    return novo.join(string2)

print(troca('Um alunos, dois alunos, tres alunos', 'alunos', 'estudantes'))