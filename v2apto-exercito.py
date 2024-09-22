'''
Exercício: Faça um programa que pergunte a idade,
o peso e a altura de uma pessoa e decide se ela está apta a ser do Exército
'''
print("------------------------------------------------\n")

print("Você está apto a servir o Exército brasileiro?\n")

print("------------------------------------------------\n")

print("Digite os seguintes dados:")

print("------------------------------")
sexo = input("SEXO [M/F]:")
print("------------------------------")
idade = int(input("IDADE:"))
print("------------------------------")
peso = float(input("PESO:"))
print("------------------------------")
altura = float(input("ALTURA:"))
print("------------------------------")

print("\n-------------------------------------------------\n")

if (sexo == "f" or sexo == "F"):
    if (idade >= 17 and idade <= 22) and (peso >= 50) and (altura >= 1.57):
        print("Parabéns, você está APTA a servir o Exército brasileiro!")
    else:
        print("Infelizmente você está INAPTA para servir o Exército brasileiro!")
elif (sexo == "m" or sexo == "M"):
    if (idade >= 17 and idade <= 22) and (peso >= 60) and (altura >= 1.7):
        print("Parabéns, você está APTO a servir o Exército brasileiro!")
    else:
        print("Infelizmente você está INAPTO para servir o Exército brasileiro!")
else:
    print("Entrada inválida, por favor tente novamente!")

