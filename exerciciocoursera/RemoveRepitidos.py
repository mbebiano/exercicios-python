def remove_repetidos(lista):
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[i] == lista[j]:
                lista.pop(j)
                j -= 1
            else:
                lista[i] = lista[i]
            j += 1
        i += 1

    return lista

listaz = [2, 4, 2, 2, 3, 3, 1]
listaz.sort()
print(remove_repetidos(listaz))

'''count=0
z = 1
listaz=[]
print(type(z))

while z != 0:
    listaz.append(int(input('Digite um número para adicionar a lista: ')))
    z = int(input('Digite 0 para parar e 1 para continuar'))


print(type(z))
print(listaz)'''

'''for n in lista:
    cont = 1
    while cont < len(lista):
        if n == lista[cont]:
            lista.pop(cont)
        else:
            a+=1
        cont+=1'''


'''while cont<len(lista):
    print(lista[cont])
    cont +=1'''