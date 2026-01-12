carro={
    "marca":"Toyota",
    "modelo":"Corolla",
    "ano":2020
}

if "cor" not in carro: # Avaliar se a chave "cor" não existe
    carro["cor"]="Azul"

print(carro)