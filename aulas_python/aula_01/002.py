# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Digite a 1ª do Bimestre nota: "))
nota2 = float(input("Digite a 2ª do Bimestre nota: "))
nota3 = float(input("Digite a 3ª do Bimestre nota: "))
nota4 = float(input("Digite a 4ª do Bimestre nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4 

# print("A media e: " + str(media))

print(f"A media das notas e: {media:.2f}")

if  media < 7: 
  print(f"Reprovado")
else:
  print(f"Aprovado")