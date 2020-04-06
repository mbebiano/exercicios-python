# Verificar se um número é divisível por 3 E por 5

Cond = int(input('Digite o número a ser verificado: '))

if (Cond%3 == 0)  and (Cond%5 == 0):
    print('FizzBuzz')

else:
    print(Cond)