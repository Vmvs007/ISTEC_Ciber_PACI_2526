
# Pede um número ao utilizador
numero = int(input("Introduza um número: "))

print(f"Os divisores de {numero} são:")

# Percorre todos os números de 1 até ao próprio número
for i in range(1, numero + 1):
    if numero % i == 0:  # Se o resto da divisão for 0, é divisor
        print(i)
