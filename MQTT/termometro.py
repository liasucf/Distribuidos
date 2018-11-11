import ssl
import sys
import paho.mqtt.client as mqtt
import paho.mqtt.publish
import tkinter
from  time import sleep 
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import os


#broker = "localhost"
broker="mosquitto.org"
port = 1883

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

root = tkinter.Tk()
global temperatura; temperatura = IntVar()
temperatura.set(30)
mqttc = mqtt.Client(client_id='termometro')
mqttc.connect(broker,port)
mqttc.loop_start()


def main():    
    
    root.title("MQTT interface")

    #### Frame 1 #####        
    frame4 = ttk.Frame(root, padding=10)
    frame4.grid(row=0, column=0)
    
    frame_4_label = ttk.Label(frame4, text='Temperatura')
    frame_4_label.grid(row=0, column = 0)
    
    image = Image.open('hot.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    hot = ImageTk.PhotoImage(image,master = root) 
    tempMais = ttk.Button(frame4,image = hot)
    tempMais['command'] = lambda: termometroAumentar()
    tempMais.grid(row=1, column=0)
    
    image = Image.open('cold.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    cold = ImageTk.PhotoImage(image,master = root) 
    tempMenos = ttk.Button(frame4,image = cold)
    tempMenos['command'] = lambda: termometroDiminuir()
    tempMenos.grid(row=1, column=1)

    root.mainloop()
    mqttc.disconnect() #disconnect
    mqttc.loop_stop() 


main() 

        
        