class Number:

    def __init__(self, number):

        self.number = number

    def getNumber(self):
        return self.number

    def __repr__(self):
        return "Número:%s" % (self.number)


numbers = []
count = 0

lista_opcoes = ["\nOpções: ",
                "1 - Cadastrar Produto",
                "2 - Ordenar",
                "3 - Mostrar Menor",
                "4 - Mostrar Maior", ]


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
            num = float(input("Digite o número que deseja salvar: "))
            number = Number(number=num)
            numbers.append(number)

            controle_insert = input(
                """Deseja cadastrar mais pessoas? (Digite 'n' ou 'N' para sair 
                e Enter para continuar)""")
            if len(controle_insert) == 1:
                if controle_insert == "n" or controle_insert == "N":
                    if controle_insert.upper() == "N":
                        print("Saindo do cadastro de pessoas")
                        break

    elif opcao_selecionada == 2:
        numeros_ordenados = sorted(
            numbers, key=Number.getNumber)
    elif opcao_selecionada == 3:
        print(numeros_ordenados[0])
    elif opcao_selecionada == 4:
        print(numeros_ordenados[-1])
