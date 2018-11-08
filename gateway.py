import ssl
import sys
import paho.mqtt.client as mqtt
import paho.mqtt.publish
import tkinter
from tkinter import ttk
from tkinter import *

broker = "localhost"
broker="mosquitto.org"
port = 1883

root = tkinter.Tk()
global volume; volume = IntVar()
global temperatura; temperatura = IntVar()
volume.set(20)
temperatura.set(30)
from  time import sleep 

mqttc = mqtt.Client("gateway")
mqttc.connect(broker,port)
mqttc.loop_start()



def main():    
    
    root.title("MQTT interface")

    #### Frame 1 #####        
    
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid(row=0, column=0)
    
    frame_1_label = ttk.Label(frame1, text='Lampada')
    frame_1_label.grid(row=0, column = 0)
    
    lampada_1_on = ttk.Button(frame1,text='On')
    lampada_1_on['command'] = lambda: lampadaOn()
    lampada_1_on.grid(row=1, column=0)
    
    lampada_1_off = ttk.Button(frame1,text='Off')
    lampada_1_off['command'] = lambda: lampadaOff()
    lampada_1_off.grid(row=1, column=1)
    

        
    ##### Fim do Frame 1 #######    
    
            #### Frame 2 #####
    frame4 = ttk.Frame(root, padding=10)
    frame4.grid(row=0, column=1)
    
    frame_4_label = ttk.Label(frame4, text='Alarme')
    frame_4_label.grid(row=0, column = 0)
       
    alarmOn = ttk.Button(frame4,text='Ligar')
    alarmOn['command'] = lambda: ativado()
    alarmOn.grid(row=1, column=0)
    
    alarmOff = ttk.Button(frame4,text='Desligar')
    alarmOff['command'] = lambda: desativado()
    alarmOff.grid(row=1, column=1)
    ######## Fim do Frame 2 ######
    
        #### Frame 3 #####
    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=1, column=0)
    
    frame_3_label = ttk.Label(frame3, text='Som')
    frame_3_label.grid(row=0, column = 0)    
    
    aumentarSom_button = ttk.Button(frame3,text='Aumentar Volume')
    aumentarSom_button['command'] = lambda: somAumentar()
    aumentarSom_button.grid(row=1, column=0)

    aumentarSom_button = ttk.Button(frame3,text='Abaixar Volume')
    aumentarSom_button['command'] = lambda: somDiminuir()
    aumentarSom_button.grid(row=1, column=1)
    
    abaixarSom_button = ttk.Button(frame3,text='Valor do Volume')
    abaixarSom_button['command'] = lambda: VolumeSom()
    abaixarSom_button.grid(row=1, column=2)
    ######## Fim do Frame 3 ######
    
        #### Frame 4 #####
    frame4 = ttk.Frame(root, padding=10)
    frame4.grid(row=1, column=1)
    
    frame_4_label = ttk.Label(frame4, text='Temperatura')
    frame_4_label.grid(row=0, column = 0)
       
    tempMais = ttk.Button(frame4,text='+')
    tempMais['command'] = lambda: termometroAumentar()
    tempMais.grid(row=1, column=0)
    
    tempMenos = ttk.Button(frame4,text='-')
    tempMenos['command'] = lambda: termometroDiminuir()
    tempMenos.grid(row=1, column=1)
    ######## Fim do Frame 4 ######
    
            #### Frame 5 #####
    frame4 = ttk.Frame(root, padding=10)
    frame4.grid(row=2, column=0)
    
    frame_4_label = ttk.Label(frame4, text='Portão')
    frame_4_label.grid(row=0, column = 0)
       
    lock = ttk.Button(frame4,text='Abrir')
    lock['command'] = lambda: unlocked()
    lock.grid(row=1, column=0)
    
    unlock = ttk.Button(frame4,text='Fechar')
    unlock['command'] = lambda: locked()
    unlock.grid(row=1, column=1)
    ######## Fim do Frame 5 ######
    
    
    root.mainloop()
    mqttc.disconnect() #disconnect
    mqttc.loop_stop() 

    
    print('Fim do loop')
        

    
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
    mqttc.publish("alarme", "Acionado")
    print('Trava')
    
    
def desativado():
    mqttc.publish("alarme", "Desativado")
    print('Destrava')
    
def termometroAumentar():
    
    global temperatura
    temp = temperatura.get()
    for x in range(0,6):
         print('Temperatura Ambiente')
         temp = temp + 1 
         print(temp)
         mqttc.publish("termometro", str(temp))
        	#Apos 3 segundos aumenta a temperatura
         for contagem in range(0,1):
                 sleep(1)
    temperatura.set(temp)
def termometroDiminuir():
    global temperatura
    temp = temperatura.get()
    for x in range(0,6):
         print('Temperatura Ambiente')
         temp = temp - 1 
         print(temp)
         mqttc.publish("termometro", str(temp))
            #Apos 3 segundos aumenta a temperatura
         for contagem in range(0,1):
                 sleep(1)
    temperatura.set(temp)


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


main()   
    