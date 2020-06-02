from rest_sms_gateway import SMSGatewayClient
import time
import random
def tempoAleatorio():
    num = round(random.uniform(19, 22), 2)
    return num;
def mensagemRandomizada():
    arquivo = open('mensagensEnvio.txt', 'r')
    lista = arquivo.readlines()  # readlinesssssss
    arquivo.close()
    mensagemAleatoria=random.choice(lista)
    return mensagemAleatoria;
def lerListaTelefones():
    arquivo = open('sms.txt', 'r')
    listaNumeros = arquivo.readlines()  # readlinesssssss
    arquivo.close()
    print("Quantidade De Números Cadastrados:", len(listaNumeros))
    return listaNumeros
def envioEmMassa(listaNumeros):
    i = 0
    contadorSucesso = 0
    contadorNaoEnviadas = 0
    while i < len(listaNumeros):
        sender = client.send_sms(listaNumeros[i], mensagemRandomizada())
        if sender['ok']:
            contadorSucesso += 1
        else:
            contadorNaoEnviadas += 1
        print("Ainda Em Envio. Sucessos:", contadorSucesso, "Não enviadas:", contadorNaoEnviadas);
        i += 1
        time.sleep(tempoAleatorio())

    print("Envio Finalizado Sucesso:", contadorSucesso, "Não enviadas:", contadorNaoEnviadas)


client = SMSGatewayClient('http://192.168.1.101:8080')
listaNumeros=lerListaTelefones()
envioEmMassa(listaNumeros)





