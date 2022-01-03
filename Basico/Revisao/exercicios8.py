#treinando OOP

#definição da classe Funcionário
class Funcionario():
    """
        Uma classe que modela o comportamento de um funcionário em uma empresa.

        Atributos:
        -> nomeEmpresa (string)
        -> idEmpresa (string)
        -> Nome (string)
        -> Idade (int)
        -> CPF (string)
        -> Cargo (string)
        -> Salário (float)

        Métodos:
        -> mostrarDados()
        -> alterarIdade()
        -> alterarCargo()
        -> alterarSalario()
        -> mostrarFuncao()
    """

    def __init__(self, empresa, nome, idade, CPF, cargo, salario):
        self.empresa = empresa.upper()
        self.idEmpresa = empresa[0:2].lower()+CPF
        self.nome = nome
        self.idade = idade
        self.cpf = CPF
        self.cargo = cargo
        self.salario = salario

    def mostrarDados(self):
        print(f"\n\nFuncionário da empresa {self.empresa}")
        print(f"ID: {self.idEmpresa}")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"CPF: {self.cpf}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R$ {self.salario}")
        print(f"{self.mostrarFuncao()}")

    def alterarNome(self, novoNome):
        self.nome = novoNome
        print("\nNome atualizado com sucesso!")

    def alterarIdade(self, novaIdade):
        #verificando se idade é válida
        if (novaIdade >= 18):
            self.idade = novaIdade
            print(f"\nIdade atualizada com sucesso!")
        else:
            print("\nErro ao atualizar idade!")

    def alterarCargo(self, novoCargo):
        novoCargo = novoCargo.lower() #tratando string para futura comparação
        #verificando se o cargo é válido
        alterar = False
        if (self.empresa == "MATEUS" and novoCargo in ["caixa", "empacotador", "administrativo", "carregador", "motorista", "chefe"]):
            alterar = True
        elif (self.empresa == "BURGUER KING" and novoCargo in ["atendente", "caixa", "cozinheiro", "ajudante de cozinheiro", "administrativo", "chefe"]):
            alterar = True
        elif (self.empresa == "NIKE" and novoCargo in ["atendente", "caixa", "administrativo", "chefe"]):
            alterar = True
        #alterando ou nao o cargo
        if (alterar):
            self.cargo = novoCargo
            print(f"\nCargo alterado com sucesso!")
        else:
            print(f"\nErro ao alterar cargo! A empresa {self.empresa} não tem o cargo {novoCargo}")

    def alterarSalario(self, novoSalario):
        #verificando se o salário é mínimo
        if (novoSalario >= 1100):
            self.salario = novoSalario
            print(f"\nSalário atualizado com sucesso!")
        else:
            print("\nErro ao atualizar salário! Valor inválido (abaixo do mínimo)...")

    def mostrarFuncao(self):
        #imprimindo informações acerca do cargo atual do funcionário em questao
        if (self.cargo == "atendente"):
            print(f"\nSou atendente da empresa {self.empresa} e tenho a função de receber e auxiliar os clientes.")
        elif (self.cargo == "caixa"):
            print(f"\nSou o caixa da empresa {self.empresa} e tenho a função de processar as compras e vendas dos produtos.")
        elif(self.cargo == "empacotador"):
            print(f"\nSou o empacotador da empresa {self.empresa} e tenho a função de empacotar e guardar os produtos.")
        elif (self.cargo == "administrativo"):
            print(f"\nSou do administrativo da empresa {self.empresa} e tenho a função de administrar os recursos.")
        elif (self.cargo == "carregador"):
            print(f"\nSou o carregador da empresa {self.empresa} e tenho a função de carregar, descarregar e armazenar produtos.")
        elif (self.cargo == "motorista"):
            print(f"\nSou o motorista da empresa {self.empresa} e tenho a função de buscar e entregar diversos produtos.")
        elif (self.cargo == "cozinheiro"):
            print(f"\nSou o cozinheiro da empresa {self.empresa} e tenho a função de cozinhar os pratos do cardápio.")
        elif (self.cargo == "ajudante de cozinheiro"):
            print(f"\nSou o ajudante de cozinheiro da empresa {self.empresa} e tenho a função de auxiliar o cozinheiro em suas tarefas.")
        elif (self.cargo == "chefe"):
            print(f"\nSou o chefe da empresa {self.empresa} e tenho a função de monitorar e tomar decisões importantes para o bem de todos.")
        else:
            print("\nErro ao falar sobre o cargo! Cargo inválido/não cadastrado...")

#programa principal

rodando1 = True
#dicionario mapeando empresas e seus respectivos funcionarios
empresas = { "MATEUS" : [],
"BURGUER KING" : [],
"NIKE" : [] }
while rodando1:
    #menu principal
    print("\nGERENCIADOR DE FUNCIONÁRIOS 1.0\n")
    print("[1] Cadastrar funcionário")
    print("[2] Editar funcionário")
    print("[3] Visualizar funcionário")
    print("[4] Remover funcionário")
    print("[5] Ver todas os funcionários")
    print("[6] Sair")
    opcao1 = input("\n-----> ")
    #executando opcoes do menu
    if (opcao1 == '1'):
        #cadastrando novo funcionário
        print("\n----- CADASTRANDO NOVO FUNCIONÁRIO -----")
        empresa = input("\nInforme o nome da empresa: ").upper()
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        cpf = input("CPF (com pontos e traços): ")
        cargo = input("Cargo: ")
        salario = float(input("Salário: R$"))
        if (empresa in ["MATEUS", "BURGUER KING", "NIKE"]):
            novoFuncionario = Funcionario(empresa, nome, idade, cpf, cargo, salario)
            #adicionando novo funcionário à sua empresa
            empresas[empresa].append(novoFuncionario)
            print("\nFuncionário cadastrado com sucesso!")
        else:
            print("\nErro ao cadastrar funcionário! Dados inválidos...")
    elif (opcao1 == '2'):
        #editando funcionário existente
        print("\n----- EDITANDO FUNCIONÁRIO -----")
        nomeEmpresa = input("\nQual a empresa do funcionário? ").upper()
        id = input("\nID do funcionário: ")
        encontrou = False
        for (empresa, funcionarios) in empresas.items():
            #encontrando empresa
            if (empresa == nomeEmpresa):
                #encontrando funcionario da empresa
                for funcionario in funcionarios:
                    if (id == funcionario.idEmpresa):
                        #alterando dados desse funcionário
                        encontrou = True
                        rodando2 = True
                        while rodando2:
                            print("[1] Alterar nome")
                            print("[2] Alterar idade")
                            print("[3] Alterar cargo")
                            print("[4] Alterar salário")
                            print("[5] Sair")
                            opcao2 = input("\n-----> ")
                            #executando opções do submenu
                            if (opcao2 == '1'):
                                novoNome = input("Nome: ")
                                funcionario.alterarNome(novoNome)
                            elif (opcao2 == '2'):
                                novaIdade = int(input("Idade: "))
                                funcionario.alterarIdade(novaIdade)
                            elif (opcao2 == '3'):
                                novoCargo = input("Cargo: ")
                                funcionario.alterarCargo(novoCargo)
                            elif (opcao2 == '4'):
                                novoSalario = float(input("Salário: R$"))
                                funcionario.alterarSalario(novoSalario)
                            elif (opcao2 == '5'):
                                rodando2 = False
                            else:
                                print("\nopção inválida! Tente novamente...")
        if (not(encontrou)):
            print("\nFuncionário inexistente! Tente novamente...")
    elif (opcao1 == '3'):
        #visualizando informações de um funcionário existente
        print("\n----- VISUALIZANDO FUNCIONÁRIO -----")
        nomeEmpresa = input("\nQual a empresa do funcionário? ").upper()
        id = input("\nID do funcionário: ")
        encontrou = False
        for (empresa, funcionarios) in empresas.items():
            #encontrando empresa
            if (empresa == nomeEmpresa):
                #encontrando funcionario da empresa
                for funcionario in funcionarios:
                    if (id == funcionario.idEmpresa):
                        #imprimindo informações do funcionário
                        funcionario.mostrarDados()
                        encontrou = True
        if (not(encontrou)):
            print("\nFuncionário inexistente! Tente novamente...")
    elif (opcao1 == '4'):
        #removendo funcionário
        print("\n----- REMOVENDO FUNCIONÁRIO -----")
        nomeEmpresa = input("\nQual a empresa do funcionário? ").upper()
        id = input("\nID do funcionário: ")
        encontrou = False
        for (empresa, funcionarios) in empresas.items():
            #encontrando empresa
            if (empresa == nomeEmpresa):
                #encontrando funcionario da empresa
                for funcionario in funcionarios:
                    if (id == funcionario.idEmpresa):
                        funcionarios.remove(funcionario)
                        print("\nFuncionário removido com sucesso!")
                        encontrou = True
        if (not(encontrou)):
            print("\nFuncionário inexistente! Tente novamente...")
    elif (opcao1 == '5'):
        for (empresa, funcionarios) in empresas.items():
            print(f"\n----- LISTA DE FUNCIONÁRIOS DA EMPRESA [{empresa}]-----")
            for funcionario in funcionarios:
                print(f"{funcionario.mostrarDados()}")
            print("\n--------------------------------------------------------")
    elif (opcao1 == '6'):
        rodando1 = False
    else:
        print("\nOpção inválida! Tente novamente...")
print("\nEncerrando programa...\n")