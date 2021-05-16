'''
1)Crie uma classe que modele uma pessoa:
*Atributos: nome, idade, peso e altura
*Metodos: envelhecer, engordar, emagrecer e crescer
OBS: por padrao, a cada ano que nossa pessoa envelhece, sendo a idade dela menor
que 21 anos, ela deve crescer 0.5 cm
'''
class Pessoa:
    #Construtor da classe (inicializador de atributos)
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        for i in range(anos):
            if (self.idade < 21):
                self.crescer() #chamando metodo proprio da classe, atravez do self.
            self.idade += 1

    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kg):
        self.peso -= kg

    def crescer(self):
        self.altura += 0.05

#Testando classe

alguem = Pessoa("Daniel", 15, 62, 1.69)

print("Nome da pessoa: {}".format(alguem.nome))
print("Idade da pessoa: {}".format(alguem.idade))
print("Peso da pessoa: {}".format(alguem.peso))
print("Altura da pessoa: {}".format(alguem.altura))

alguem.envelhecer(7) #fazendo a pessoa envelhecer 5 anos
alguem.engordar(12) #fazendo a pessoa engordar 12 kg
alguem.emagrecer(6.5) #fazendo a pessoa emagrecer 6.5 kg

print("\nNome da pessoa: {}".format(alguem.nome))
print("Idade da pessoa: {}".format(alguem.idade))
print("Peso da pessoa: {}".format(alguem.peso))
print("Altura da pessoa: {}".format(alguem.altura))
        
    
