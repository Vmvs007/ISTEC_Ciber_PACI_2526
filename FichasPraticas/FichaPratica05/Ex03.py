lista = []

for i in range(10):
    # print("Insira um número na lista[", i, "]: ")
    print(f"Insira um número na lista[{i}]: ")
    numInserido = int(input())
    lista.append(numInserido)

maior = lista[0]

# Encontrar o maior elemento
for i in range(10):
    if (lista[i] > maior):
        maior = lista[i]

print("Maior:", maior)
