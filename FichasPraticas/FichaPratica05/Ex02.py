lista = []

# Leitura da lista
for i in range(12):
    print(f"Insira um número na lista[{i}]: ")
    numInserido = float(input())
    lista.append(numInserido)

soma = 0

for i in range(12):
    soma = soma + lista[i]

print("Soma:", soma)
