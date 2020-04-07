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
    lista.sort()
    return lista
