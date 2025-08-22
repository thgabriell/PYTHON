# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Digite a 1ª do Bimestre nota: "))
nota2 = float(input("Digite a 2ª do Bimestre nota: "))


media = (nota1 + nota2 ) / 2 

# print("A media e: " + str(media))

print(f"A media das notas e: {media:.2f}")

if  media > 7: 
  print(f"Aprovado")
else:
  print(f"Reprovado")