def soma(z, d):
    aux = z
    z = d
    d = aux
    print('Dentro da funcao valor de z -a- = ', z)
    print('Dentro da funcao valor de d -b- = ', d)
    return z+d

z = 4
d = -5

print('Fora da função z = ', z)
print('Fora da função d = ',d)
print('Valor da função = ', soma(z, d))
print('Fora da função 2 z = ', z)
print('Fora da função 2 d = ',d)
