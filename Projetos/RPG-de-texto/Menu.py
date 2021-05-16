'''
    Arquivo que simula o menu do jogo RPG de texto: ??????
'''
import os
from time import sleep

#funcao para limpar a tela
def limpar():
    #para sistemas linux e mac
    if os.name == 'posix':
        _ = os.system('clear')
    #para sistemas windows
    else:
        _ = os.system('cls')

#funcao que irá chamar o menu do jogo
def run():
    #aplicacao do menu
    while True:
        print("> Bem vindo ao RPG de texto!\n")
        print("\n########## MENU ##########")
        print("1- Iniciar jogo")
        print("2- Creditos")
        print("3- Sair")
        print("##########################\n")
        
        opcao = int(input("-> "))
        #realizando cada uma das opcoes
        if opcao == 1:
            sleep(2) #dando um delay de 2 segundos antes de limpar
            limpar()
            print("\nCarregando jogo...\n")
            #codigo para carregar primeira fase e iniciar jogador vai aqui
        elif opcao == 2:
            sleep(2) #dando um delay de 2 segundos antes de limpar
            limpar()
            print("\n\nFeito por: Daniel Sousa Gonçalves\n\n")
        elif opcao == 3:
            sleep(2) #dando um delay de 2 segundos antes de limpar
            limpar()
            print("\nEncerrando jogo...\n")
        else:
            print("\nSinto muito! Opcao invalida!\n")
        

#executando menu
if __name__ == '__main__':
    run()

