tradutor = {
    "dog": "cão",
    "cat": "gato",
    "house": "casa",
    "computer": "computador",
    "car": "carro"
}

pesquisa = input("Palavra a traduzir EN -> PT: ")

if pesquisa not in tradutor:
    print("Tradução não encontrada")
else:
    print(tradutor[pesquisa])
