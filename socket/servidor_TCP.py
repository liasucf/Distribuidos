#criação de um servirdor TCP em python
import socket
from datetime import datetime
import threading
import json


#definindo porta e ip.
port1 = 5002
adress = '127.0.0.1'
#criando o socket servidor
socket_servidor_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#definindo de onde vamos escutar
destiny1 = (adress, port1)

#link do socket ao destiny
socket_servidor_tcp.bind(destiny1)

global vol, temp

vol = 30
temp = 30

def novo_cliente(clientsocket, addr, conexao):
  global vol, temp

  status_lampada = "desligada"
  #while True:
  mensagem = clientsocket.recv(2000).decode('utf-8')
  #do some checks and if msg == someWeirdSignal: break:
  if mensagem == "LAMPADA LIGADA":
    print("comando recebido lampada")
    status_lampada = "ligada"
    print("status da lampada:",status_lampada)
    conexao['lampada'].send('LAMPADA LIGADA'.encode())
  elif mensagem == "LAMPADA DESLIGADA":
    print("comando recebido lampada")
    status_lampada = "desligada"
    print("status da lampada:",status_lampada)
    conexao['lampada'].send('LAMPADA DESLIGADA'.encode())
# parte do portao
  elif mensagem == "Portão aberto":
    print("comando recebido portão")
    status_portao = "abrir"
    print("status do portao:",status_portao)
    conexao['portao'].send('portao abrindo'.encode())
  elif mensagem == "Portão fechado":
    print("comando recebido portão")
    status_portao = "fechando"
    print("status do portao:",status_portao)
    conexao['portao'].send('portao fechando'.encode())
# Parte do alarme
  elif mensagem == "Alarme ativado":
    print("comando recebido alarme")
    status_alarme = "Ativado"
    print("status do portao:",status_alarme)
    conexao['alarme'].send('ativando alarme'.encode())
  elif mensagem == "Alarme desativado":
    print("comando recebido alarme")
    status_alarme = "Desativado"
    print("status do portao:",status_alarme)
    conexao['alarme'].send('desativando alarme'.encode())
# Parte do som
  elif mensagem == "aumentar som":
    vol = vol + 1
    print("comando recebido som")
    print("volume:",vol)
    conexao['som'].send(str(vol).encode())
  elif mensagem == "diminuir som":
    vol = vol - 1
    print("comando recebido som")
    print("volume:",vol)
    conexao['som'].send(str(vol).encode())
# Parte da temperatura
  elif mensagem == "aumentar temperatura":
    for x in range(0,6):
      temp = temp + 1
    mensagem = str(temp)
    socket_cliente(mensagem)
    #Apos 3 segundos aumenta a temperatura
    for contagem in range(0,3):
      sleep(1)
    
    print("comando recebido temperatura")
    print("temperatura: ",mensagem)
    conexao['temperatura'].send(str(vol).encode())
  elif mensagem == "diminuir temperatura":
    for x in range(0,6):
      temp = temp - 1
    mensagem = str(temp)
    socket_cliente(mensagem)
    #Apos 3 segundos aumenta a temperatura
    for contagem in range(0,3):
      sleep(1)
    
    print("comando recebido temperatura")
    print("temperatura: ",mensagem)
    conexao['temperatura'].send(str(vol).encode())
  print ('conectado com ', addr)
  print (addr, ' >> ', mensagem)


#    mensagem = input('SERVER >> ')
  #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
  
  clientsocket.close()




#o servidor vai ficar escutando o socket aqui:
socket_servidor_tcp.listen()
print ('Servidor iniciado!')
print ('esperando clientes...')

conexao = {}

try:
	while True:
	   c, addr = socket_servidor_tcp.accept()     # Establish connection with client.
	   #thread.start_new_thread(novo_cliente,(c,addr))

	   ID = c.recv(2000).decode('utf-8')
	   if ID != 'ignore-me':
	      conexao[ID] = c

	   thread=threading.Thread(target=novo_cliente,args=(c, addr, conexao))
	   thread.daemon = True
	   thread.start()
	   #Note it's (addr,) not (addr) because second parameter is a tuple
	   #Edit: (c,addr)
	   #that's how you pass arguments to functions when creating new threads using thread module.
except Exception as e:
	socket_servidor_tcp.close()
	print(e)
finally:
	socket_servidor_tcp.close()
	
#while True:
    #accept() retorna uma tupla cliente é o endereço da conexão e socket_conect é um novo socket, por onde serão trocadas informações.
 #   socket_conect, client = socket_servidor_tcp.accept()
  #  print('Conecção no endereço ', client)
   # #mensagem escutada no socket_conect. tem que decodificar em utf-8 
   # mensagem = socket_conect.recv(2000).decode('utf-8')
   # print("Mensagem recebida no socket: %s" %mensagem)
    #uma resposta genérica pelo socket_conect
   # socket_conect.send(('tambem mando mensagens').encode('utf-8'))
    #não esquece de fechar o socket
#socket_conect.close()
