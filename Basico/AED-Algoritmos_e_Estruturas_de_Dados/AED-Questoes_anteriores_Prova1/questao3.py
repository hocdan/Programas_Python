#Um dicionário Português-Inglês é útil para orientar um estudante brasileiro a se expressar nos Estados Unidos
#ou em outro país de língua inglesa. Já um dicionário Inglês-Português, por sua vez, é útil para orientar um
#estudante que fale inglês a se expressar no Brasil. Escreva a função em Python chamada converter, que receba
#como entrada um dicionário Português-Inglês e retorne o dicionário Inglês-Português correspondente.
#Por exemplo, converter({‘Casa’:‘House’ , ‘Artigo’:‘Paper’,‘Papel’:‘Paper’, ‘Telefone’:‘Phone’}) deverá retornar
#o dicionário {‘House’: ‘Casa’, ‘Paper’: ‘Artigo, Papel’, ‘Phone’: ‘Telefone’ }*. * ﬁque atento para as palavras
#que possuem mais de um signiﬁcado (ex: Paper).

D = {'Casa':'House','Artigo':'Paper', 'Papel':'Paper', 'Telefone':'Phone'}

def converter(D):
    DN = {}
    for v in D.values():
        if ( v in DN.values()):
            continue
        DN[v] = ''
    for k in D.keys():
        i = D[k]
        if ( i in DN.keys() and DN[i] != ''):
            DN[i] += ', ' + k
            continue
        DN[i] += k
    print(DN)

converter(D)
