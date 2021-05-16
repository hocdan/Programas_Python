#Uma pizzaria oferece aos seus clientes pizzas customizadas, onde cada cliente escolhe no menu todos os itens
#que serão colocados na sua pizza (queijo, presunto, ovo, orégano, cebola, tomate, rúcula, azeitona, ...).
#E então, armazena cada pedido em um dicionário de pedidos, onde a chave do dicionário é a mesa que fez o pedido
#e o valor é a lista de ingredientes escolhidos. Porém, o pizzaiolo veriﬁcou que não tem azeitona e nem palmito
#suﬁcientes e precisa informar os clientes que escolheram estes itens. Faça uma função em Python chamada listar_mesas
#que receba como entrada o dicionário de pedidos e os ingredientes que estão em falta e retorne as mesas que precisam
#ser notiﬁcadas. Adicionalmente, escreva um código que chame essa função.

D = {'1':'ovo, azeitona, cebola', '2':'ovo, calabresa, cebola', '3':'queijo, azeitona, oregano', '4':'palmito, presunto, ovo', '5':'queijo, carne, palmito, azeitona'}

def listar_mesas(D):
    mesas = []
    for k,v in D.items():
        if ( 'palmito' in v or 'azeitona' in v):
                mesas.append(k)
    print(mesas)

listar_mesas(D)
