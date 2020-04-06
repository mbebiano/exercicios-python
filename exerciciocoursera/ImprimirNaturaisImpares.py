# Receba uma valor e imprima os números naturais.

number = int(input("Digite o valor de n: "))
iteracao = 1

while number > 0:
    number -= 1
    print(iteracao)
    iteracao += 2
