#range( stop ) #primeira definição ou definição simplificada Padrão de step é 1 e start é 0
#range( [start], stop[, step] ) #segunda definição ou definição completa

nomes = ['Maria', 'Ricardo', 'Isabel', 'Taís', 'Laura']

contador = 0

for nome in nomes:
  if len(nome) > 4:
    contador += 1

print(contador)