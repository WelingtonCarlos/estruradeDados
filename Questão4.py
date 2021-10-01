def buscasequencial(lista, elem):
    count = 0
    for i in range(len(lista)):
        count = count + 1
        if lista[i] == elem:
            print(count, "comparações")
            return elem

    return "Não encontrado"


def buscabinaria(seq, elem):

    start = 0
    end = len(seq)-1
    count = 0
    while start <= end:
        middle = (start + end)//2

        if seq[middle] < elem:
            start = middle + 1
        elif seq[middle] > elem:
            end = middle - 1
        else:
            count = count + 1
            print(count, "comparações")
            return elem

        count = count + 1

    return 'Elemento não encontrado'


def quicksort(seq):
    quick(seq, 0, end=None)


def quick(seq, start, end):

    if end is None:
        end = len(seq) - 1
    if start < end:
        p = partition(seq, start, end)
        quick(seq, start, p - 1)
        quick(seq, p + 1, end)


def partition(seq, start, end):
    pivot = seq[end]
    i = start
    for j in range(start, end):
        if seq[j] <= pivot:
            seq[j], seq[i] = seq[i], seq[j]
            i = i + 1
    seq[i], seq[end] = seq[end], seq[i]
    return i


class Produto:

    def __init__(self, codigo1, nome1, preco1):

        self.cogido1 = codigo1
        self.nome1 = nome1
        self.preco1 = preco1

    def getCodigo(self):
        return self.codigo1

    def getNome(self):
        return self.nome1

    def getPreco(self):
        return self.preco1

    def __repr__(self):
        return "produto:%s preço:%s" % (self.nome1,
                                        self.preco1)


class Codigo:

    def __init__(self, codigo):

        self.codigo = codigo

    def getCodigo(self):
        return self.codigo

    def __repr__(self):
        return "Código:%s" % (self.codigo)


class Descricao:

    def __init__(self, nome):

        self.nome = nome

    def getNome(self):
        return self.nome

    def __repr__(self):
        return "Produto:%s" % (self.nome)


class Preco:

    def __init__(self, preco):

        self.preco = preco

    def getPreco(self):
        return self.preco

    def __repr__(self):
        return "Preço:%s" % (self.preco)


produtos = []
codigos = []
descricaos = []
precos = []


# Criando lista de opções para o usuário
lista_opcoes = ["\nOpções: ",
                "1 - Cadastrar Produto",
                "2 - Listar Produtos em ordem Alfabética",
                "3 - Listar Produtos do menor para o maior preço",
                "4 - Listar Produtos maior para o menor preço",
                "5 - Listar Produtos por ordem crescente de código"]

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
            codigo_produto = int(input("Insira o código do produto: "))
            nome_descricao = input("Insira o nome do produto: ")
            preco_produto = float(input("Insira o preço do produto: "))
            codigo = Codigo(codigo=codigo_produto)
            codigos.append(codigo)
            descricao = Descricao(nome=nome_descricao)
            descricaos.append(descricao)
            preco = Preco(preco=preco_produto)
            precos.append(preco)
            produto = Produto(codigo1=codigo_produto,
                              nome1=nome_descricao, preco1=preco_produto)
            produtos.append(produto)
            print("Cadastro do produto realizado com sucesso}")

            controle_insert = input(
                "Deseja cadastrar mais pessoas? (Digite 'n' ou 'N' para sair)")
            if len(controle_insert) == 1:
                if controle_insert == "n" or controle_insert == "N":
                    if controle_insert.upper() == "N":
                        print("Saindo do cadastro de pessoas")
                        break

    elif opcao_selecionada == 2:
        produto_ordem_alfabetica = sorted(
            produtos, key=Produto.getNome)
        print(produto_ordem_alfabetica)

    elif opcao_selecionada == 3:
        produto_ordem_crescente_preco = sorted(
            produtos, key=Produto.getPreco)
        print(produto_ordem_crescente_preco)

    elif opcao_selecionada == 4:
        produto_ordem_descrescente_preco = sorted(
            produtos, key=Produto.getPreco, reverse=True)
        print(produto_ordem_descrescente_preco)

    elif opcao_selecionada == 5:
        produto_ordem_crescente_codigo = sorted(
            produtos, key=Produto.getCodigo)
        print(produto_ordem_crescente_codigo)

    else:
        print("opção inválida")

    """ elif opcao_selecionada == 2:
        print(codigos)
        print(descricaos)
        print(precos, "Reais") """

""" quicksort(teste)

print(teste)

print(buscasequencial((teste), 10))

print(buscabinaria((teste), 10)) """
