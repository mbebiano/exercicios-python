#Verificacao parcial de Strings
'''arquivo = 'pRog.py'
x = arquivo.startswith('p')
y = arquivo.endswith('py')
print(x)
print(y)
x = arquivo.lower()
y = arquivo.upper()
print(x)
print(y)'''
# Find And Replace
s = 'um tigre, dois tigre, três tigres'
x = s.find('tigre')
print(x)
# retorna três, a posição onde está o tigre, da pra pesquisar a partir de um indice com s.find('tigre', 4) 4 é o indice
# Replace:
y = s.replace('tigre','gato')
print(y)
# replace faz uma cópia a string 's' continua contendo o tigre. No caso do meu exemplo foi para a variavel y
#Split e Join:

txt = 'batatinha quando nasce'
x = txt.split()
print(x)
data = '21/02/2011'
x = data.split ('/')
print(x)
times = ['Palmeiras','Santos','São Paulo','Corinthians']
x = '/'.join(times)
print(x)