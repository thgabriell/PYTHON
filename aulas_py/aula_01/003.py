# Tendo como dado de entrada a altura(h) de uma pessoa e seu sexo, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

# .strip() usado para remover espaços em branco no início e no final de uma string.
# .upper() transformar todas as letras de uma string em maiúsculas.  <!-- -->

altura = float(input(f"Qual a sua altura: " ))
sexo = input(f"Qual o seu sexo (M para masculino F para feminino):").strip().upper()

if sexo == "M":
    peso_ideal = (72.7*altura) - 58
    print(f"Peso recomendado para Homens {peso_ideal:.2f} kg")
elif sexo == "F":
    peso_ideal = (62.1*altura) - 44.7
    print(f"Peso recomendado para Mulheres {peso_ideal:.2f} kg")
else:
    print(f"Esse sexo nao existi. ")