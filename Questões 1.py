def main():
    seq1 = [54, 2, 11, 4, 17, 7, 21, 1, 5, 37, 42, 13, 29]
    seq2 = [54, 2, 55, 11, 21, 1, 5, 37, 42, 13, 29]
    seq3 = [54, 2, 11, 4, 17, 7, 21, 1, 99, 55, 67, 9, 71, 79, 89]
    seq4 = [721, 345, 901, 101, 21, 67, 7, 9, 4, 79]
    seq5 = [871, 888, 564, 764, 990, 76, 3, 1, 2, 5, 45, 89]

    print(seq1)
    print(seq2)
    print(seq3)
    print(seq4)
    print(seq5)
    print("\n")

    insercao(seq1)
    print("Ordenação por inserção: ", seq1)

    selecao(seq2)
    print("Ordenação por seleção: ", seq2)

    bolha(seq3)
    print("Ordenação por troca: ", seq3)

    merge_sort(seq4)
    print("Ordenação por intercalação: ", seq4)

    quicksort(seq5)
    print("Ordenação Rápida: ", seq5)


# Ordenação pro Inserção
def insercao(seq):
    x = len(seq)
    for p in range(1, x):
        current_element = seq[p]  # posição atual
        index = p - 1  # índice sendo uma posição a menos que o p
        while index >= 0 and seq[index] > current_element:
            seq[index + 1] = seq[index]
            index = index - 1

        seq[index + 1] = current_element

# Ordenação por Seleção


def selecao(seq):
    x = len(seq)
    for index in range(x-1):
        min_index = index  # o menor índice da lista é na posição que o index estiver

        for right in range(index, x):
            if seq[right] < seq[min_index]:  # se o elemento seguinte ao index for menor
                # eles invertem de posição
                seq[right], seq[min_index] = seq[min_index], seq[right]

# Ordenação por Troca


def bolha(seq):
    x = len(seq)
    # verifica se a lista tem tamanho pra fazer a ordenação
    for final in range(x - 1):

        # inicia do primeiro elemento da lista até o penúltimo
        for current in range(x - 1):
            # se o valor que está na posição atual é maior que o seguinte
            if seq[current] > seq[current + 1]:
                # inverte a posição
                seq[current + 1], seq[current] = seq[current], seq[current + 1]


# Ordenação por Intercalação


def merge_sort(seq):
    mergesort(seq, 0, end=None)


def mergesort(seq, start, end):
    if end is None:
        end = len(seq)
    if(end - start > 1):
        meio = (end + start)//2
        mergesort(seq, start, meio)
        mergesort(seq, meio, end)
        merge(seq, start, meio, end)


def merge(seq, start, meio, end):
    left = seq[start:meio]
    right = seq[meio:end]
    init_left, init_right = 0, 0
    for k in range(start, end):
        if init_left >= len(left):
            seq[k] = right[init_right]
            init_right = init_right + 1
        elif init_right >= len(right):
            seq[k] = left[init_left]
            init_left = init_left + 1
        elif left[init_left] < right[init_right]:
            seq[k] = left[init_left]
            init_left = init_left + 1
        else:
            seq[k] = right[init_right]
            init_right = init_right + 1


# Ordenação Rápida

def quicksort(seq):
    quick(seq, 0, end=None)


# start é 0 pra começar do início, e end é None pois não tem como passar a list
def quick(seq, start, end):

    # se o fim for vazio, o fim então é o tamanho da lista -1.
    if end is None:
        end = len(seq) - 1
    # Se o início da nossa lista for menor que o fim:
    if start < end:
        p = partition(seq, start, end)          # calculamos a posição do pivô
        # chamo a função principal com o fim sendo o pivô -1
        quick(seq, start, p - 1)
        # chamando a unção com o início sendo o pivô +1
        quick(seq, p + 1, end)


def partition(seq, start, end):
    # nosso pivô é o último elemento
    pivot = seq[end]
    i = start                                   # Nosso index inicia no começo
    # a variável J inicia em start e termina no imediato antes do end
    for j in range(start, end):
        # se o J for menor do que o pivô:
        if seq[j] <= pivot:
            # seus valores são imediatamente invertidos
            seq[j], seq[i] = seq[i], seq[j]
            i = i + 1                           # o index avança uma casa.
    # e por último troca os valores do index com o J
    seq[i], seq[end] = seq[end], seq[i]
    return i


def busca(lista, elem):
    """Retorna o índice elem se ele estiver na lista ou None, caso contrário"""
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None


lista_estranha = [8, "5", 32, 0, "python", 11]
print(lista_estranha)
print("digite um elemento pra ser buscado: ")
elemento = input()
indice = busca(lista_estranha, elemento)
if indice is not None:
    print("O índice do elemento {} é {}".format(elemento, indice))
else:
    print("O elemento {} não se encontra na lista".format(elemento))


main()
