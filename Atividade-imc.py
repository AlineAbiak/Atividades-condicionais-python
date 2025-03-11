import os

os.system('cls')

print("    |CÁLCULO DE IMC|    ", "\n")

peso = float(input("Qual é o seu peso?: "))

altura = float(input("Qual é a sua altura?: "))

imc = peso / (altura * altura)

os.system('cls')

print("|Seu IMC é: ", imc)

if(imc <= 16.9):
    print("|Muito abaixo do peso.")

elif(imc >= 17 and imc <= 18.4):
    print("|Abaixo do peso.")

elif(imc >= 18.5 and imc <= 24.9):
    print("|Peso normal.")

elif(imc >= 25 and imc <= 29.9):
    print("|Acima do peso.")

elif(imc >= 30 and imc <= 34.9):
    print("|Obesidade grau |.")

elif(imc >= 35 and imc <= 40):
    print("|Obesidade grau")

else:
    print("|Obesidade grau |||.")