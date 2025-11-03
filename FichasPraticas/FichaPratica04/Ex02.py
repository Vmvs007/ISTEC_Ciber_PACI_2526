soma = 0

for i in range(11, 52):  # vai de 11 até 51
    if i % 2 != 0:       # verifica se é ímpar
        print(i)
        soma += i         # acumula a soma

print("Somatório dos números ímpares:", soma)
