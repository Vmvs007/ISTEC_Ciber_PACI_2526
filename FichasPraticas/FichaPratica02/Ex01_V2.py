# Ler números
num1 = int(input("Insira o 1º número: "))
num2 = int(input("Insira o 2º número: "))

# Apresentar o maior

if (num1 == num2):
    print("São iguais")
else:
    if (num1 > num2):
        print("Maior:", num1)
    else:
        print("Maior:", num2)
