
# Calculadora simples em Python

# Variaveis para armazenar os números

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


# Operações matemáticas

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2 if numero2 != 0 else "Indefinido (divisão por zero)"
exponenciacao = numero1 ** numero2
raiz_quadrada_numero1 = numero1 ** 0.5
raiz_quadrada_numero2 = numero2 ** 0.5

# print

print(f"resultado: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Exponenciação: {exponenciacao}")
print(f"Raiz quadrada do primeiro número: {raiz_quadrada_numero1}")
print(f"Raiz quadrada do segundo número: {raiz_quadrada_numero2}")

