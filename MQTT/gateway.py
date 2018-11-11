import ssl
import sys
import paho.mqtt.client as mqtt
import paho.mqtt.publish
import tkinter
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import os

broker = "localhost"
broker="mosquitto.org"
port = 1883

root = tkinter.Tk()
global volume; volume = IntVar()
global temperatura; temperatura = IntVar()
termometro_mensagem = '°C'
volume.set(20)
temperatura.set(30)
from  time import sleep 


def on_connect(client, userdata, flags, rc):
    print("Connectado with result code "+str(rc))

    mqttc.subscribe("termometro")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print (msg.topic+" "+str(msg.payload))
    global termometro_mensagem 
    termometro_mensagem = msg.payload

def lampadaOn():
    mqttc.publish("lampada", "Ligada")
    print('Liga')
    
    
def lampadaOff():
    mqttc.publish("lampada", "Desligada")
    print('Desliga')

    
def locked():
    mqttc.publish("tranca", "Fechado")
    print('Fecha')
    
    
def unlocked():
    mqttc.publish("tranca", "Aberto")
    print('Abre')

    
def ativado():
    mqttc.publish("alarme", "Ativado")
    print('Trava')
    
    
def desativado():
    mqttc.publish("alarme", "Desativado")
    print('Destrava')



def somAumentar():
    global volume
    vol = volume.get() + 1
    mqttc.publish("som", str(vol))
    volume.set(vol)

def somDiminuir():
    global volume
    vol = volume.get() - 1
    mqttc.publish("som", str(vol))
    volume.set(vol)

def VolumeSom():
    global volume
    volume = volume.get()
    mqttc.publish("som", str(volume))

mqttc = mqtt.Client("gateway")
mqttc.connect(broker,port)
mqttc.on_connect = on_connect
mqttc.on_message = on_message




def main():    
    
    root.title("MQTT interface")

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
    frame2 = ttk.Frame(root, padding=10)
    frame2.grid(row=0, column=1)
    
    frame_2_label = ttk.Label(frame2, text='Alarme')
    frame_2_label.grid(row=0, column = 0)
    
    
    image = Image.open('shield.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    shield = ImageTk.PhotoImage(image,master = root) 
    alarmOn = ttk.Button(frame2,image = shield)
    alarmOn['command'] = lambda: ativado()
    alarmOn.grid(row=1, column=0)
    
    image = Image.open('security-off.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    shieldOff = ImageTk.PhotoImage(image,master = root) 
    alarmOff = ttk.Button(frame2,image=shieldOff)
    alarmOff['command'] = lambda: desativado()
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
    aumentarSom_button['command'] = lambda: somAumentar()
    aumentarSom_button.grid(row=1, column=0)
    
    
    image = Image.open('volumeMinus.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    botaoMinus = ImageTk.PhotoImage(image ,master = root)
    aumentarSom_button = ttk.Button(frame3,image= botaoMinus)
    aumentarSom_button['command'] = lambda: somDiminuir()
    aumentarSom_button.grid(row=1, column=1)
    ######## Fim do Frame 3 ######
    
        #### Frame 4 #####
    frame4 = ttk.Frame(root, padding=10)
    frame4.grid(row=1, column=1)

    frame_4_label = ttk.Label(frame4, text='Temperatura')
    frame_4_label.grid(row=0, column = 0)

    image_tablet = Image.open('tablet.png')
    image_tablet = image_tablet.resize((120, 150), Image.ANTIALIAS)
    leitor_tablet = ImageTk.PhotoImage(image_tablet,master = root)    
    tempValor = ttk.Label(frame4,text='',image = leitor_tablet, compound='center')
    tempValor.grid(row=1, column=0)
      
    ######## Fim do Frame 4 ######
    
            #### Frame 5 #####
    #### Frame 5 #####
    frame5 = ttk.Frame(root, padding=10)
    frame5.grid(row=2, column=0)
    
    frame_5_label = ttk.Label(frame5, text='Portão')
    frame_5_label.grid(row=0, column = 0)
    
    image = Image.open('unlocked.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    cadAberto = ImageTk.PhotoImage(image,master = root) 
    lock = ttk.Button(frame5,image=cadAberto)
    lock['command'] = lambda: unlocked()
    lock.grid(row=1, column=0)
    
    image = Image.open('locked.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    cadFechado = ImageTk.PhotoImage(image,master = root) 
    unlock = ttk.Button(frame5,image=cadFechado)
    unlock['command'] = lambda: locked()
    unlock.grid(row=1, column=1)
    ######## Fim do Frame 5 ######
    ######## Fim do Frame 5 ######
    
    while True:
        root.update()
        mqttc.loop(.1)

        
        tempValor["text"] = termometro_mensagem
        
        

if __name__ == '__main__':
    main()
    sys.exit(0)
        

    



main() 




