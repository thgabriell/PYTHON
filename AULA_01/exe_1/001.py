#crie um script que imprime os números de 1 a 10 e indica se são pares ou ímpares

for numero in range(1, 11):
    if  numero % 2 == 0 :
        print(f"{numero} é Par")
    else: 
        print(f"{numero} é Ímpar")   