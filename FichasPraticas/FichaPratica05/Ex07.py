lista = []

for i in range(10):
    print(f"Insira um número na lista[{i}]: ")
    numInserido = int(input())
    lista.append(numInserido)

maiorPar = -1

# Encontrar o maior elemento
for i in range(10):
    if (lista[i] % 2 == 0):

        if (maiorPar % 2 != 0):
            maiorPar = lista[i]

        if (lista[i] > maiorPar):
            maiorPar = lista[i]


if (maiorPar % 2 == 0):
    print("Maior Par:", maiorPar)
else:
    print("Não há pares")
