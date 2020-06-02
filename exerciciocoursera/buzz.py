#Verificar se um número é Divisível por 5
import random

def mensagemRandomizada():
    arquivo = open('mensagensEnvio.txt', 'r')
    lista = arquivo.readlines()  # readlinesssssss
    arquivo.close()
    mensagemAleatoria=random.choice(lista)
    return mensagemAleatoria;


i=0;

while(i<10):
    print(tempoAleatorio())
    i+=1;