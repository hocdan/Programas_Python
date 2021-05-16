#Escreva a função em Python chamada exclusivos, que receba duas strings como entrada e
#retorne uma nova string contendo os caracteres das mesmas que não pertencem
#simultaneamente as duas strings. Por exemplo, exclusivos(‘aluno’,‘novato’)
#deve retornar ‘luvt’. Adicionalmente, escreva um código que solicite as duas strings
#ao usuário e chame a função passando as strings obtidas como parâmetro.

def exclusivos(str1, str2):
    str3 = [x for x in str2 if (x not in str1)]
    str4 = [x for x in str1 if (x not in str2)]
    return ''.join(str3+str4)

print(exclusivos('daniel', 'kaio'))


    
    
