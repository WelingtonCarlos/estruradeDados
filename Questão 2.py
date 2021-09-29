
# Importando classe pessoas
""" from typing import List """
from Pessoas import Pessoas

# Criando lista de opções para o usuário
lista_opcoes = ["\nOpções: ",
                "1 - Cadastrar pessoas ",
                "2- Cadastrar café"]

# Criando lista pessoas
lista_pessoas = []

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
            nome_pessoa = input("Insira o nome: ")
            salario = int(input("Insira o salario: "))
            pessoa = Pessoas(nome=nome_pessoa, salario=salario)
            lista_pessoas.append(pessoa)
            print("Foi realizado o cadastro de {nome_pessoa}")

            controle_insert = input(
                "Deseja cadastrar mais pessoas? (Digite 'n' ou 'N' para sair)")
            if len(controle_insert) == 1:
                if controle_insert == "n" or controle_insert == "N":
                    if controle_insert.upper() == "N":
                        print("Saindo do cadastro de pessoas")
                        break
