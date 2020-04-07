def soma_elementos(lista):
    count=0
    acumulador=0
    while count<len(lista):
        acumulador = lista[count] + acumulador
        count+=1
    return acumulador

