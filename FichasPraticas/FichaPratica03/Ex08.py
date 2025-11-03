num = int(input("Insira um número: "))

antecessor = num - 5
sucessor = num + 5

while (antecessor < num):
    print(antecessor)
    antecessor = antecessor + 1

print()

num = num + 1

while (num <= sucessor):
    print(num)
    num = num + 1
