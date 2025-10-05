numeros_originais = []
print("Por favor, digite 10 números inteiros:")

for i in range(10):
    while True:
        try:
            num = int(input(f"Digite o {i+1}º número: "))
            numeros_originais.append(num)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

numeros_alterados = numeros_originais.copy()

for i in range(len(numeros_alterados)):
    if numeros_alterados[i] < 0:
        numeros_alterados[i] = 0

print("\n--- Resultado ---")
print(f"Lista original: {numeros_originais}")
print(f"Lista com negativos substituídos por zero: {numeros_alterados}")