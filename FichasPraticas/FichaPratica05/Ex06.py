lista = []

for i in range(10):
    print(f"Insira um número na lista[{i}]: ")
    numInserido = int(input())
    lista.append(numInserido)

crescente = True

for i in range(1, 10):
    if (lista[i] <= lista[i - 1]):
        crescente = False


if (crescente): # crescente == True
    print("Crescente")
else:
    print("Não crescente")
