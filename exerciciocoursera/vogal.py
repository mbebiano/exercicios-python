def vogal(vogal1):
    if vogal1 in 'aeiouAEIOU':
        a = True
    else:
        a = False
    return a

vogal1 = input('Digite um caractere para verificar: ')
print(vogal(vogal1))
