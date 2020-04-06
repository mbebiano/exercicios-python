# Strings em Python são imutaveis o que aumenta a perfomance, a solução seria a concatenação como no exemplo abaixo


frase = 'atoa'
x = len(frase)
c = 0
d = 1
while c < x:

    if frase[c] in 'aeiou':
        frase = frase[:c] + '*' + frase[d:x]
    else:
        frase=frase
    c+=1
    d+=1

print(frase)

'''
# Programa ler palavra e troque as vogais por '*'
palavra = input('Digite uma palavra: ')

for 'aeiou' in palavra'''
