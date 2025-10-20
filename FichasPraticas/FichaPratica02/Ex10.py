num1 = float(input("1º número: "))
num2 = float(input("2º número: "))

operacao = input("Operação ( + - * / ): ")

match (operacao):
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:  # Default option - caso nenhum dos anteriores se verifique
        print("Operação não reconhecida:", operacao)
