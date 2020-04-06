import time
inicio = time.time()

n = int(input("Digite um número inteiro: "))
soma = 0

while (n > 0):
    resto = n % 10
    n = n // 10
    soma = soma + resto
fim = time.time()
print("A soma dos números é: ", soma)
print(fim - inicio)

'''r = 999%10
a = 999//10
print(a)
print(r)
 // Armazena o valor inteiro que sobra no exemplo acima a divisão de 999 por 10 acarreta no RESTO de 
um número inteiro o 9. Já na operação 999%9 ele retorna o valor do QUOCIENTE no caso 99'''
