def maior_primo(num):
    count = 1
    acum = 0
    a = 0
    b = False

    while b==False:
        while count <= num:
            if num % count == 0:
                acum += 1
            else:
                a += 1

            count += 1
        if acum == 2:
            b = True
        else:
            num = num - 1
            acum = 0
            count= 1
    return num



num_primo = int(input('Digite nº primo maior ou igual a 2: '))

while num_primo < 2 :
    num_primo = int(input('Digite nº primo maior ou igual a 2: '))

print(maior_primo(num_primo))



