num = int(input("Insira um número: "))

antecessor = num - 5
sucessor = num + 5

while (antecessor <= sucessor):
    if(antecessor!=num):
        print(antecessor)

    antecessor = antecessor + 1

