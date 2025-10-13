produto1 = float(input("Insira o preço do 1º produto: "))
produto2 = float(input("Insira o preço do 2º produto: "))
produto3 = float(input("Insira o preço do 3º produto: "))

total = produto1 + produto2 + produto3
totalComDesconto = total * 0.9

print("Valor com 10% de desconto:", totalComDesconto, "€")
