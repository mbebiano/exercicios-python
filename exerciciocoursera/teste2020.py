
"""sender = client.send_sms('+5532991495085', 'Your first message')
if sender['ok']: # or sender['status_code'] == 200
    print('Message sent!')
else:
    print("not send!")
    """
client = SMSGatewayClient('http://192.168.1.101:8080')
arquivo = open('sms.txt', 'r')
lista = arquivo.readlines() # readlinesssssss
arquivo.close()
a = len(lista)
print(a)
i = 0;
while i<a:
    print(lista[i]);
    i+=1;

