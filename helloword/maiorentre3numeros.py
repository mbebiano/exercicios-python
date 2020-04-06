# Saber o maior entre 3 números
a = int(input('Digite o valor do primeiro numero: '))
b = int(input('Digite o valor do segundo numero: '))
c = int(input('Digite o valor do terceiro numero: '))

if a > b :
    if a > c:
        print('O maior número é = %d' % (a))
    else :
        print('O maior número é = %d' % (c))
elif b > a:
    if b > c:
        print('O maior número é = %d' % (b))
    else :
        print('O maior número é = %d' % (c))
else:
    if c > a:
        print('O maior número é = %d' % (c))
    else :
        print('O maior número é = %d' % (a))