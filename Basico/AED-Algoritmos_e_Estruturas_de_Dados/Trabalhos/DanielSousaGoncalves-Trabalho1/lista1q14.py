#14a) Escreva uma função nao_eh_ruim que receba como entrada uma string e encontre
#as primeiras ocorrências de ‘nao eh’ e de ‘ruim’. Se ‘nao’ vier antes de ‘ruim’,deve-se substituir a
#expressão ‘nao eh...ruim’ por ‘eh bom’, retornando a nova string.
#Por exemplo,nao_eh_ruim(‘Figado nao eh tao ruim’) deve retornar ‘Figado eh bom’.

def nao_eh_ruim(string):
    p1 = 'nao eh'
    p2 = 'eh bom'
    parar1, parar2 = 0, 0
    achou, achou2 = 0, 0
    string2 = string
    for i in range(len(string)):
        if ( string[i:i+6] == 'nao eh' and parar1 == 0):
            achou = i
            parar1 += 1
        if ( string[i:i+4] == 'ruim' and parar2 == 0):
            achou2 = i
            parar2 += 1
        if (achou2 < achou):
            parar2 = 0
    if ( achou < achou2):
        string2 = string[:achou]
        string2 += 'eh bom'
        string2 += string[achou2+4:]
    return string2

print('Frase "Figado nao eh tao ruim" editada:', nao_eh_ruim("Figado nao eh ruim"))
