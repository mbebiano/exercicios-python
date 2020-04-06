# Imprimir Fatorial

Number = int(input("Digite o valor de n: "))
Count = Number - 1
if Number == 0:
    print(1)

else:
    while Count >= 1:
        Number = Number * Count
        Count= Count-1

    print(Number)
