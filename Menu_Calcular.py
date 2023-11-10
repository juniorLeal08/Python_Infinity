# Menu De Calculadora

numero01 = float(input("Digite O Primeiro Numero: "))
numero02 = float(input("Digite O Segundo Numero: "))

while True:

    resultado = 0

    escolha = int(input("""
          Escolha Uma Operação:
          1 - Somar
          2 - Subtrair
          3 - Multiplicar
          4 - Dividir
          0 - Sair       
    """))
    match escolha:
        case 1:
            resultado = numero01 + numero02
            print(f"O Resultado Da Soma É {resultado}")
        case 2:
            resultado = numero01 - numero02
            print(f"O Resultado Da Subtração É {resultado}")
        case 3:
            resultado = numero01 * numero02
            print(f"O Resultado Da Multiplicação É {resultado}")
        case 4:
            if numero02 != 0:
                resultado = numero01 / numero02
                print(f"O Resultado Da Divisão É {resultado}")
            else:
                print("Erro Divisão Por Zero.")

        case 0:
            print("Programa Encerrado.....")
            break
        case _:
            print("Opção Invalida.Por Favor, Escolha Uma Opção Valida.")
            print(f"O Resultado É:{resultado}")

