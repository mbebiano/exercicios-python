# Leia 10 números reais e mostre os na ordem inversa
c=0
a=[]
while c<10:
    a.append(float(input('Digite o número real da posição %.f : '%c)))
    c+=1
c=9
while c>=0:
    print(a[c])
    c-=1
