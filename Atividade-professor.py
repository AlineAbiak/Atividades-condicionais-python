import os

os.system('cls')

print("    |ESCOLA APRENDER|    ", "\n")

nivel = int(input("|Selecione o nível: "))

aulas = int(input("|Quantidade de aulas lecionadas por semana: "))

if(nivel == 1):
    salario = (12.00 * aulas) * 4 
    print("|O salário final é: ", salario)

elif(nivel == 2):
    salario = (17.00 * aulas) * 4
    print("|O salário final é: ", salario)

elif(nivel == 3):
    salario = (25.00 * aulas) * 4
    print("|O salário final é: ", salario)

else:
    print("|Digite um nível válido!")

