def retangulo2(coluna, linha):
    i = 1 #linha
    j = 1 #coluna
    tab = ''

    while i <= linha:
        if i==1 or i==linha:
            j = 1
            tab = ''
            while j <= coluna:
                tab = tab + '#'
                j += 1
            print(tab)

        else:
            j=1
            tab = ''
            while j <= coluna:
                if j==1 or j==coluna:
                    tab = tab + '#'
                else:
                    tab = tab + ' '
                j+=1
            print(tab)
        i+=1



largura = int(input('Digite a largura: '))
altura = int(input('Digita a altura: '))

retangulo2(largura, altura)