lista = []

for i in range(0, 10):
    # print("Insira um número na lista[", i, "]: ")
    print(f"Insira um número na lista[{i}]: ")
    numInserido = int(input())
    lista.append(numInserido)

print(lista)

# Somar todos os elementos - sum( )
somaElementos = sum(lista)
print("Soma:", somaElementos)

# Maior elemento - max( )
maior = max(lista)
print("Maior:", maior)

# Menor elemento - min( )
menor = min(lista)
print("Menor:", menor)

# Tamanho da lista - len( )
tamanhoLista = len(lista)
print("Tamanho (quantidade de elementos):", tamanhoLista)
