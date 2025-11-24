lista = []

for i in range(10):
    # print("Insira um número na lista[", i, "]: ")
    print(f"Insira um número na lista[{i}]: ")
    numInserido = int(input())
    lista.append(numInserido)

menor = lista[0]

# Encontrar o menor elemento
for i in range(10):
    if (lista[i] < menor):
        menor = lista[i]

print("Menor:", menor)
