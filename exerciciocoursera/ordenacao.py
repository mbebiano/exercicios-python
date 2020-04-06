# Verificar se está em ordem crescente

Primeiro = int(input('Digite o primeiro número: '))
Segundo = int(input('Digite o segundo número: '))
Terceiro = int(input('Digite o terceiro número: '))

if Primeiro<Segundo and Segundo<Terceiro:
    print('crescente')

else:
    print('não está em ordem crescente')