'''
    Um pequeno projeto para estudo baseado em um tutorial do YouTube

    -> Programa que irá solicitar um nome de usuario no GitHub para entao "resgatar" a sua
    foto de perfil.

    OBS: utiliza as bibliotecas externas requests e bs4.
'''

import requests
from bs4 import BeautifulSoup as bs #abreviando a parte interna de bs4 para facilidade de uso

#coletando nome de usuario do GitHub e fazendo uma request da pagina web do seu GitHub
github_user = input("Nome do usuario: ")
url = "https://github.com/" + github_user
r = requests.get(url)

#armazenando a pagina em formato html com os elementos ja separados e listados
soup = bs(r.content, "html.parser")
#retirando a imagem de usuario desse arquivo html, somente onde se encontra a imagem de perfil
profile_image = soup.find("img", {"alt" : "Avatar"})["src"] #tipo IMG, de atributo ALT na porcao SRC
print(profile_image) #mostrando link para o item desejado (imagem de perfil)
