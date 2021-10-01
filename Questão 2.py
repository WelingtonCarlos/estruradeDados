
# Importando classe pessoas
""" from typing import List """


class Funcionario:

    def __init__(self, nome, salario):

        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def __repr__(self):
        return "Nome:%s salário:%s" % (self.nome, self.salario)


funcionarios = []

# Criando lista de opções para o usuário
lista_opcoes = ["\nOpções: ",
                "1 - Cadastrar funcionário",
                "2- Listar Funcionários em ordem Alfabética",
                "3- Listar Funcionários em ordem crescente de salário",
                "4- Listar Funcionários em ordem decrescente de salário"]

# Criando lista pessoas

# Iniciando interação com o usuário
print("Sistema de cadastro treinamento")
nome_usuario = input("\n Ola! Digite seu nome: ")

# Loop para funcionamento do programa
while True:
    # Mostra as opções e solicita que o usuário selecione uma
    print(f"{nome_usuario} escolha uma opção: ")
    for opcao in lista_opcoes:
        print(opcao)
    opcao_selecionada = int(input("Insira a opção desejada: "))
    # controle de navegação do sistema
    if opcao_selecionada == 1:  # Cadastrando pessoas
        while True:
            nome_funcionario = input("Insira o nome: ")
            salario = float(input("Insira o salario: "))
            funcionario = Funcionario(nome=nome_funcionario, salario=salario)
            funcionarios.append(funcionario)
            print("Foi realizado o cadastro de {nome_funcionario}")

            controle_insert = input(
                "Deseja cadastrar mais pessoas? (Digite 'n' ou 'N' para sair)")
            if len(controle_insert) == 1:
                if controle_insert == "n" or controle_insert == "N":
                    if controle_insert.upper() == "N":
                        print("Saindo do cadastro de pessoas")
                        break

    elif opcao_selecionada == 2:
        funcionarios_ordem_alfabetica = sorted(
            funcionarios, key=Funcionario.getNome)
        print(funcionarios_ordem_alfabetica)

    elif opcao_selecionada == 3:
        funcionarios_ordem_crescente_salario = sorted(
            funcionarios, key=Funcionario.getSalario)
        print(funcionarios_ordem_crescente_salario)

    elif opcao_selecionada == 4:
        funcionarios_ordem_decrescente_salario = sorted(
            funcionarios, key=Funcionario.getSalario, reverse=True)
        print(funcionarios_ordem_decrescente_salario)

    else:
        print("opção inválida")
