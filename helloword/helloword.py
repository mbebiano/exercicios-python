# Tabuada de 1 a 10
"""c = 0

while c < 10:
    a = 1
    c += 1
    while a <= 10:
        print('Tabuada %d x %d = %d' %(a, c, a*c))
        a += 1"""
# Fibonacci Sequência
a = 1
b = 1
x=int(input('Digite a posição da sequência de Fibonnaci que deseja: '))
y=x
if x==1:
    print('Posição F(%d) = %d'%(x,a))
elif x==2:
    print('Posição F(%d) = %d'%(x,b))
else:
    x = x-2;
    while x>0:
        c = a+b
        b = a
        a = c
        x-=1
    print('Posição F(%d) = %d'%(y,c))

