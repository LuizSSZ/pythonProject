'''
Exercício: Faça um programa que leia a quantidade de pessoas que serão convidadas em uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados
e depois irá imprimir todos os nomes da lista
'''
print("------------------------------------------------\n")
print("QUANTAS PESSOAS VOCÊ IRÁ CONVIDAR PARA A FESTA?\n")
print("------------------------------------------------\n")

num_convidados = int(input("Digite a quantidade de pessoas que você quer convidar para a festa: "))

lista_convidados = []

i = 0

while (i < num_convidados):
    print(f"Convidado N°{i + 1}")
    nome_convidado = input("NOME: ")
    lista_convidados.append(nome_convidado)
    i += 1

print(" - " * 10)
print("CONVIDADOS".center(30))
print(" - " * 10)

print("-" * 30)

for j in range(len(lista_convidados)):
    print(f"{lista_convidados[j]} - convidado n° {j + 1}")
    print("-" * 30)
