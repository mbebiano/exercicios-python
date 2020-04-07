def retangulo(linha, coluna):
    i = 1  # linha
    j = 1  # coluna
    tab = ''
    while j <= altura:
        while i <= largura:
            tab = tab + '#'
            i += 1
        print(tab, end='\n')
        j += 1

largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura : '))

retangulo(altura, largura)