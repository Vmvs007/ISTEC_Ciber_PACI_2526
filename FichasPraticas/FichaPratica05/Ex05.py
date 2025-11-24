lista = []

numInserido = 1

while (numInserido >= 0):
    numInserido = int(input("Insira um número na lista (negativo para parar): "))

    lista.append(numInserido)

# len(vossaLista) dá o tamanho da lista (quantidade de elementos)
tamanhoLista = len(lista)

# remover o último elemento
lista.pop(tamanhoLista - 1)

# Calcular a media
somaElementos = sum(lista)
quantidadeElementos = len(lista)

media = somaElementos / quantidadeElementos

print("Média:", media)
