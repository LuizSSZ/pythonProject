print("---------------------")
print("\nCalculadora-Simples\n")
print("---------------------")

number1 = int(input(": "))
number2 = int(input(": "))

operator = input("Escolha o operador: \n[+]\n[-]\n[*]\n[/]\n")

if (operator == "+"):
    result = number1 + number2
elif (operator == "-"):
    result = number1 - number2
elif (operator == "*"):
    result = number1 * number2
elif (operator == "/"):
    if (number2 != 0):
        result = number1 / number2
    else:
        print("Erro: Divisão por Zero!")
else:
    print("Operador inválido! Por favor tente novamente")

print(f"Resultado Final: {result}")