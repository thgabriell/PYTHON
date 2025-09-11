# IMC = peso / (altura * altura)
#
# 18.50 - 24.99 = Peso normal.
# 25.00 - 29.99 = pré-obesidade.
# 30.00 - 34.99 = Obesidade grau I.
# 35.00 - 39.99 = Obesidade grau II.
# >40.00: Obesidade grau III.


# variavel

peso = float(input("Digite o seu peso em  kg: "))
altura = float(input("Digite a sua altura em metros:"))

# cálculo e print 

imc = peso / (altura * altura)

if imc < 18.5:
    print("Magro demais") 
elif  imc >= 18.5 and imc < 25:
    print("peso normal")
elif imc >= 25 and imc < 30:
    print("pré-obesidade")
elif imc >= 30 and imc < 35:
    print("obesidade grau I")
elif imc >= 35 and imc < 40:
    print("obesidade grau II")
else:
    print("obesidade grau III")
print(f"Seu IMC é {imc:.2f}")