# Solicita dois números inteiros ao utilizador
base = int(input("Primeiro número: "))
expoente = int(input("Segundo número: "))

# Inicializa o resultado
resultado = 1

# Caso o expoente seja positivo
for i in range(expoente):
    resultado *= base

print(f"Resultado ({base} elevado a {expoente}): {resultado}")
