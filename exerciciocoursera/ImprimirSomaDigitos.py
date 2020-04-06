#Imprimir soma dos digitos de um número.


n = input('Digite um número inteiro: ')
count = 0
acumulador = 0

while count < len(n):
    acumulador = int(n[count]) + acumulador
    count+=1

print(acumulador)
