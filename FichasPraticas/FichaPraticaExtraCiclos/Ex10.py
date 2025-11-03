numero = int(input("Introduza um número inteiro: "))

revertido = 0

num_temp = numero

# Enquanto ainda houver dígitos
while num_temp > 0:
    digito = num_temp % 10               # Último dígito
    revertido = revertido * 10 + digito  # Adiciona o dígito ao número invertido
    num_temp //= 10                      # Remove o último dígito

print(f"Número: {numero} | Resultado: {revertido}")
