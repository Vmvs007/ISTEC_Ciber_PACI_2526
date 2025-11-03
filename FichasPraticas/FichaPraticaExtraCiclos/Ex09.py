numero = int(input("Introduza um número inteiro: "))

num_temp = numero

soma = 0

# Enquanto ainda houver dígitos
while num_temp > 0:
    digito = num_temp % 10      # Obtém o último dígito
    soma += digito              # Soma o dígito
    num_temp //= 10             # Remove o último dígito

print(f"A soma dos dígitos de {numero} é: {soma}")
