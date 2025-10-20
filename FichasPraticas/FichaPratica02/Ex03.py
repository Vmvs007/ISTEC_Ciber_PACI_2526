salario = float(input("Salário Anual: "))

if (salario <= 15000):
    impostos = salario * 0.2
    print("Taxas de 20%:", impostos)

if (salario > 15000 and salario <= 20000):
    impostos = salario * 0.3
    print("Taxas de 30%:", impostos)

if (salario > 20000 and salario <= 25000):
    impostos = salario * 0.35
    print("Taxas de 35%:", impostos)

if (salario > 25000):
    impostos = salario * 0.4
    print("Taxas de 40%:", impostos)
