num = 0

somatorio = 1
contador = -1

while (num != -1):
    num = int(input("Insira um número (-1 para terminar): "))
    somatorio = somatorio + num
    contador = contador + 1

media = somatorio / contador
print("Média:", media)
