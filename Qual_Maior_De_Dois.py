# Maior de Dois

numero01 = int(input("Digite O Primeiro Numero: "))
numero02 = int(input("Digite O Segundo Numero: "))



if numero01 > numero02:
    print(f"O Numero {numero01} É Maior Que O {numero02}")
elif numero02 > numero01:
    print(f"O Numero {numero02} É Maior Que O {numero01}")
else:
    print(f"Os Numeros São Iguais, Número Digitado:{numero01}")