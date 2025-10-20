# Ler valores
a = int(input("Insira o 1º valor: "))
b = int(input("Insira o 2º valor: "))
c = int(input("Insira o 3º valor: "))

if (a < b and a < c):  # A ... ...
    if (b < c):  # ABC
        print(a, "|", b, "|", c)
    else:  # ACB
        print(a, "|", c, "|", b)

if (b < a and b < c):  # B ... ...
    if (a < c):  # BAC
        print(b, "|", a, "|", c)
    else:  # BCA
        print(b, "|", c, "|", a)

if (c < a and c < b):  # C ... ...
    if (a < b):  # CAB
        print(c, "|", a, "|", b)
    else:  # CBA
        print(c, "|", b, "|", a)
