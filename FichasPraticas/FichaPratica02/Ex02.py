salario = float(input("Salário Anual: "))

if (salario <= 15000):
    impostos = salario * 0.2
    print("Taxas de 20%:", impostos)
else:
    impostos = salario * 0.3
    print("Taxas de 30%:", impostos)
