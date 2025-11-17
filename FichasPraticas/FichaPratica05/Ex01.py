lista = []

for i in range(0, 10):
    # print("Insira um número na lista[", i, "]: ")
    print(f"Insira um número na lista[{i}]: ")
    numInserido = int(input())
    lista.append(numInserido)

print(lista)