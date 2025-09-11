# importe a biblioteca 

from math import sqrt

#variavel dos catetos
ct1 = float(input("Digite o valor do cateto 1: "))
ct2 = float(input("Digite o valor do cateto 2: "))

#calculo da hipotenusa

hipotenusa = sqrt(pow(ct1,2) + (pow(ct2,2)))

#print

print(f"O valor da hipotenusa e: {hipotenusa:.2f}")