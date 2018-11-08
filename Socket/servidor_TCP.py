#criação de um servirdor TCP em python
import socket
from datetime import datetime
#definindo porta e ip.
port1 = 5002
adress = '127.0.0.1'


#criando o socket servidor
socket_servidor_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#definindo de onde vamos escutar
destiny1 = (adress, port1)
#link do socket ao destiny
socket_servidor_tcp.bind(destiny1)

#o servidor vai ficar escutando o socket aqui:
socket_servidor_tcp.listen()
while True:
    #accept() retorna uma tupla cliente é o endereço da conexão e socket_conect é um novo socket, por onde serão trocadas informações.
    socket_conect, client = socket_servidor_tcp.accept()
    print('Conecção no endereço ', client)
    #mensagem escutada no socket_conect. tem que decodificar em utf-8 
    mensagem = socket_conect.recv(2000).decode('utf-8')
    print("Mensagem recebida no socket: %s" %mensagem)
    #uma resposta genérica pelo socket_conect
    socket_conect.send(('tambem mando mensagens').encode('utf-8'))
    #não esquece de fechar o socket
socket_conect.close()
