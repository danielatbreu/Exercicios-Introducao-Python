print("\n====== Funções ======")
primeiro_numero = int(input("Insira o primeiro número: "))
segundo_numero = int(input("Insira o segundo número: "))

print("\nSelecione qual operação você deseja realizar de acordo com as opções abaixo:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Potência")
operacao = (input(""))

def soma (primeiro_numero,segundo_numero):
    soma = primeiro_numero + segundo_numero
    return (soma)

def subtracao (primeiro_numero,segundo_numero):
    subtracao = primeiro_numero - segundo_numero
    return (subtracao)

def multiplicacao(primeiro_numero, segundo_numero):
    resultado = 0
    sinal = 1

    if segundo_numero < 0:
        segundo_numero = -segundo_numero
        sinal = -1

    for _ in range(segundo_numero):
        resultado = resultado + primeiro_numero

    if sinal == -1:
        resultado = -resultado
    return resultado

def potencia(primeiro_numero, segundo_numero):
    if segundo_numero == 0:
        return 1

    resultado = primeiro_numero
    contador = 1

    while contador < segundo_numero:
        resultado = multiplicacao(resultado, primeiro_numero)
        contador = contador + 1
    return resultado

if operacao == "1":
    print("O resultado é: ", soma(primeiro_numero,segundo_numero))

elif operacao == "2":
    print("O resultado é: ", subtracao(primeiro_numero,segundo_numero))

elif operacao == "3":
    print("O resultado é: ", multiplicacao(primeiro_numero,segundo_numero))

elif operacao == "4":
    print("O resultado é: ", potencia(primeiro_numero, segundo_numero))











