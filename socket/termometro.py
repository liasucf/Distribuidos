import socket
import datetime
import json
import tkinter
import threading
from tkinter import ttk

#definindo porta e ip.
port1 = 5002
adress = '127.0.0.1'
destiny1 = (adress, port1)
#criando o socket servidor
socket_servidor_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#definindo de onde vamos escutar
destiny1 = (adress, port1)
#socket_servidor_tcp.close()
#link do socket ao destiny
socket_servidor_tcp.connect(destiny1)


#o servidor vai ficar escutando o socket aqui:
#socket_servidor_tcp.listen()

socket_servidor_tcp.send('lampada'.encode())

#while True:
#	#recebendo a variavel do servidor por json 
#	#status_lampada=json.loads(socket_cliente_lampada_tcp.recv(2048).decode('utf-8'))
#	status = socket_servidor_tcp.recv(2000).decode('utf-8')
#	print ("status da lampada: ", status)


class Temperatura():
    def __init__(self, socket_servidor_tcp):

        self.socket_servidor_tcp = socket_servidor_tcp
        self.status = 'off'
        
        root = tkinter.Tk()
        root.title("tcp interface")

        self.threading()

        #### self.frame1 1 #####        
        
        self.frame11 = ttk.Frame(root, padding=10)
        self.frame11.grid(row=0, column=0)
        
        self.frame1_1_label = ttk.Label(self.frame11, text='Temperatura')
        self.frame1_1_label.grid(row=0, column = 0)
        
    #    lampada_1_on = ttk.Button(self.frame11,text='On')
    #    lampada_1_on['command'] = lambda: lampStatus(status,self.frame11)
    #    lampada_1_on.grid(row=1, column=0)
        
        
        root.mainloop()
        print('Fim do loop')

    def update_gui(self):
        if self.status == 'LAMPADA LIGADA':
            text = 'on'
        else:
            text = 'off'

        print(self.status)

        self.frame1_lig = ttk.Label(self.frame11,text = text)
        self.frame1_lig.grid(row=2, column=0)


    def threading(self):
        self.t = threading.Thread(target=self.recieve_from_server)
        self.t.daemon = True
        self.t.start()

    def recieve_from_server(self):
        while True:
            status = self.socket_servidor_tcp.recv(2000).decode('utf-8')
            if status != '':
                self.status = status
            print ("status da lampada: ", self.status)

            self.update_gui()


#def lampStatus(status, self.frame11):
#    if status == 'LAMPADA LIGADA':
#        self.frame1_lig = ttk.Label(self.frame11,text = 'On')
#        self.frame1_lig.grid(row=2, column=0)
#    else:
#        self.frame1_off = ttk.Label(self.frame11,text = 'Off')
#        self.frame1_off.grid(row=2, column=0)
    
    
Temperatura(socket_servidor_tcp)  
#temos que fechar o socket
socket_servidor_tcp.close()
