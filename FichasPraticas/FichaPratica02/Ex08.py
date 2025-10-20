# Ler valores
nota1 = int(input("Insira o 1º nota: "))
nota2 = int(input("Insira o 2º nota: "))
nota3 = int(input("Insira o 3º nota: "))

# Média Ponderada
mediaPonderada = (nota1 * 0.25) + (nota2 * 0.35) + (nota3 * 0.4)
print("Média Ponderada:", mediaPonderada)

if (mediaPonderada >= 9.5):
    print("Aprovado")
else:
    print("Reprovado")
