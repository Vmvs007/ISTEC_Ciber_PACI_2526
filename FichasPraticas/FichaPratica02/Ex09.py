# Ler valores
num1 = int(input("Insira o 1º valor: "))
num2 = int(input("Insira o 2º valor: "))
num3 = int(input("Insira o 3º valor: "))

if (num1 < num2 and num1 < num3):
    print("Menor:", num1)

if (num2 < num1 and num2 < num3):
    print("Menor:", num2)

if (num3 < num1 and num3 < num2):
    print("Menor:", num3)
