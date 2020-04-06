# Verificar se uma palavra é palindrome
z=0
while z==0:
    x = input('Digite a palavra: ')
    y = x[::-1]
    if x == y:
        print('É palíndrome')
    else:
        print('Não é palíndrome')
    z = int(input('Digite 0 para continuar : \n'))
