from time import sleep
from tkinter import *
import socket
import datetime
import tkinter
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import os
#__________________________________________________________________________________________________________________________
#definindo a porta e o IP de comunicação como uma variavel global
adress = '127.0.0.1'
port = 5002

#__________________________________________________________________________________________________________________________
#definindo volume como uma variavel global
root = tkinter.Tk()
global volume; volume = IntVar()
volume.set(20)
#__________________________________________________________________________________________________________________________

#definição do destino como uma variavel global
destiny = (adress, port)

#__________________________________________________________________________________________________________________________

#definindo o socket para passar por   parametro
def socket_cliente(mensagem):
	#criando o socket TCP.
	socket_cliente_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#link do socket com o endereço de destino
	socket_cliente_tcp.connect(destiny)
	#o socket envia a mensagem para o servidor tcp codificado com UTF-8
	sleep(0.01)
	socket_cliente_tcp.send(mensagem.encode('utf-8'))
	#O método recv lê os bytes recebidos, retornando-os em uma string, até o limite 2000. não esqueça de decodificar 	de UTF-8
#	mensagem_recebida = socket_cliente_tcp.recv(2000).decode('utf-8')
#	print(mensagem_recebida)
#	print("Mensagem recebida: %s" %mensagem_recebida)
	#temos que fechar o socket
	socket_cliente_tcp.close()

#__________________________________________________________________________________________________________________________
#definindo função de ligar lampada que vai ser usada pelo botão
def lampadaOn():
	#mensagem a ser enviada
	mensagem = 'LAMPADA LIGADA'	
	socket_cliente(mensagem)
	

#__________________________________________________________________________________________________________________________
#definindo função de desligar lampada que vai ser usada pelo botão
def lampadaOff():
	#mensagem a ser enviada
	mensagem = 'LAMPADA DESLIGADA'	
	socket_cliente(mensagem)

#__________________________________________________________________________________________________________________________
#definindo função de abrir portao que vai ser usada pelo botão
def portaoAbrir():
	#mensagem a ser enviada
	mensagem = 'Portão aberto'	
	socket_cliente(mensagem)
	

#__________________________________________________________________________________________________________________________
#definindo função de fechar portão que vai ser usada pelo botão
def portaoFechar():
	#mensagem a ser enviada
	mensagem = 'Portão fechado'	

	socket_cliente(mensagem)

#__________________________________________________________________________________________________________________________
#definindo função de ligar alarme que vai ser usada pelo botão
def alarme_ativar():
	#mensagem a ser enviada
	mensagem = 'Alarme ativado'	
	socket_cliente(mensagem)
	

#__________________________________________________________________________________________________________________________
#definindo função de desligar alarme que vai ser usada pelo botão
def alarme_desativar():
	#mensagem a ser enviada
	mensagem = 'Alarme desativado'	
	socket_cliente(mensagem)

#__________________________________________________________________________________________________________________________
#definindo função de aumentar temperatura
def aumenta_temp():
	mensagem = 'aumentar temperatura'	
	socket_cliente(mensagem)
	
	


#__________________________________________________________________________________________________________________________
#definindo função diminuir temperatura
def diminui_temp():
	mensagem = 'diminuir temperatura'	
	socket_cliente(mensagem)
	


#__________________________________________________________________________________________________________________________


#definindo função de aumentar volume
def aumenta_som():
	mensagem = 'aumentar som'	
	socket_cliente(mensagem)		


#__________________________________________________________________________________________________________________________
#definindo função diminuir volume
def diminui_som():
	mensagem ='diminuir som'	
	socket_cliente(mensagem)
	
	

#__________________________________________________________________________________________________________________________
#definindo função volume
def VolumeSom():
	global volume
	volume = volume.get()
	socket_cliente(str(volume))



#__________________________________________________________________________________________________________________________

global som


def main():

    standard_temp = 23
    temp = standard_temp
    
    root.title("TCP interface")
    
        
    #### Frame 1 #####        
    
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid(row=0, column=0)
    
    frame_1_label = ttk.Label(frame1, text='Lampada')
    frame_1_label.grid(row=0, column = 0)
    
    image = Image.open('lightOn.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    lightOn = ImageTk.PhotoImage(image,master = root)
    
    lampada_1_on = ttk.Button(frame1,image= lightOn)
    lampada_1_on['command'] = lambda: lampadaOn()
    lampada_1_on.grid(row=1, column=0)
    
    image = Image.open('light-bulb(2).png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    lightOff = ImageTk.PhotoImage(image,master = root)    
    
    lampada_1_off = ttk.Button(frame1,image=lightOff)
    lampada_1_off['command'] = lambda: lampadaOff()
    lampada_1_off.grid(row=1, column=1)
    

        
    ##### Fim do Frame 1 #######    
    
            #### Frame 2 #####
    frame4 = ttk.Frame(root, padding=10)
    frame4.grid(row=0, column=1)
    
    frame_4_label = ttk.Label(frame4, text='Alarme')
    frame_4_label.grid(row=0, column = 0)
    
    
    image = Image.open('shield.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    shield = ImageTk.PhotoImage(image,master = root) 
    alarmOn = ttk.Button(frame4,image = shield)
    alarmOn['command'] = lambda: alarme_ativar()
    alarmOn.grid(row=1, column=0)
    
    image = Image.open('security-off.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    shieldOff = ImageTk.PhotoImage(image,master = root) 
    alarmOff = ttk.Button(frame4,image=shieldOff)
    alarmOff['command'] = lambda: alarme_desativar()
    alarmOff.grid(row=1, column=1)
    ######## Fim do Frame 2 ######
    
        #### Frame 3 #####
    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=1, column=0)
    
    frame_3_label = ttk.Label(frame3, text='Som')
    frame_3_label.grid(row=0, column = 0)    
    
    
    image = Image.open('volumePlus.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    botaoPos = ImageTk.PhotoImage(image ,master = root)
    aumentarSom_button = ttk.Button(frame3,image=botaoPos)
    aumentarSom_button['command'] = lambda: aumenta_som()
    aumentarSom_button.grid(row=1, column=0)
    
    
    image = Image.open('volumeMinus.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    botaoMinus = ImageTk.PhotoImage(image ,master = root)
    aumentarSom_button = ttk.Button(frame3,image= botaoMinus)
    aumentarSom_button['command'] = lambda: diminui_som()
    aumentarSom_button.grid(row=1, column=1)
    
    image = Image.open('tablet.png')
    image = image.resize((120, 150), Image.ANTIALIAS)
    leitor = ImageTk.PhotoImage(image,master = root)    
    abaixarSom_button = ttk.Label(frame3,text='Valor do Volume',image = leitor, compound='center')
    #abaixarSom_button['command'] = lambda: VolumeSom()
    abaixarSom_button.grid(row=1, column=2)
    ######## Fim do Frame 3 ######
    
        #### Frame 4 #####
    frame4 = ttk.Frame(root, padding=10)
    frame4.grid(row=1, column=1)
    
    frame_4_label = ttk.Label(frame4, text='Temperatura')
    frame_4_label.grid(row=0, column = 0)
    
    image = Image.open('hot.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    hot = ImageTk.PhotoImage(image,master = root) 
    tempMais = ttk.Button(frame4,image = hot)
    tempMais['command'] = lambda: aumenta_temp()
    tempMais.grid(row=1, column=0)
    
    image = Image.open('cold.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    cold = ImageTk.PhotoImage(image,master = root) 
    tempMenos = ttk.Button(frame4,image = cold)
    tempMenos['command'] = lambda: diminui_temp()
    tempMenos.grid(row=1, column=1)
    ######## Fim do Frame 4 ######
    
           #### Frame 5 #####
    frame4 = ttk.Frame(root, padding=10)
    frame4.grid(row=2, column=0)

    frame_4_label = ttk.Label(frame4, text='Portão')
    frame_4_label.grid(row=0, column = 0)

    image = Image.open('unlocked.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    cadAberto = ImageTk.PhotoImage(image,master = root)
    lock = ttk.Button(frame4,image=cadAberto)
    lock['command'] = lambda: portaoAbrir()
    lock.grid(row=1, column=0)

    image = Image.open('locked.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    cadFechado = ImageTk.PhotoImage(image,master = root)
    unlock = ttk.Button(frame4,image=cadFechado)
    unlock['command'] = lambda: portaoFechar()
    unlock.grid(row=1, column=1)
         ######## Fim do Frame 5 ######
    
    
    root.mainloop()
    
    print('Fim do loop')
main()
def do_stuff():
    print('')


  

