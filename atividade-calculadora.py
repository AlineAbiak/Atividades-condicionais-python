import os

os.system('cls')

print("   |CALCULADORA|   ", "\n")

n = float(input("  Selecione o primeiro número da operação: "))

operador = input("  Selecione a operção matemática desejada (+, -, / ou x.): ")

n2 = float(input("  Selecione o segundo número da operação: "))

if(operador == "/"):
    print("   |O resultado é: ", n / n2)

elif(operador == "+"):
    print("   |O resultado é: ", n + n2)

elif(operador == "-"):
    print("   |O resultado é: ", n - n2)

elif(operador == "x" or operador == "*"):
    print("   |O resultado é: ", n * n2)

else:
    print("   |Operação inválida.")



