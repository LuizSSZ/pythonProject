'''
Exercício: Faça um programa que pergunte a idade,
o peso e a altura de uma pessoa e decide se ela está apta a ser do Exército
'''

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

if (sexo == "F" or sexo == "f"):
    if (idade >= 17 and idade <= 22):
        pts = 1
    else:
        pts = 0
    if (peso >= 50):
        pts += 1
    else:
        pts += 0
    if (altura >= 1.57):
        pts += 1
    else:
        pts += 0
    result = pts

elif (sexo == "M" or sexo == "m"):
    if (idade >= 17 and idade <= 22):
        pts = 1
    else:
        pts = 0
    if (peso >= 60):
        pts += 1
    else:
        pts += 0
    if (altura >= 1.7):
        pts += 1
    else:
        pts += 0
    result = pts
else:
    print("ENTRADA INVÁLIDA!")

print("----------------------------------------------------------")

if (result == 3):
    print("Parabéns, você está APTO a servir o Exército brasileiro!")
else:
    print("Infelizmente você está INAPTO a servir o Exército brasileiro!")
