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
status = 'Status'



def on_connect(client, userdata, flags, rc):
    print("Connectado with result code "+str(rc))

    mqttc.subscribe("alarme")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print (msg.topic+" "+str(msg.payload))
    global status 
    status = msg.payload


mqttc = mqtt.Client(client_id='alarme')
mqttc.connect(broker,port)
mqttc.on_connect = on_connect
mqttc.on_message = on_message



def main():    
	root.title("MQTT interface")

    #### Frame 1 #####        
	frame4 = ttk.Frame(root, padding=10)
	frame4.grid(row=0, column=0)
    
	frame_4_label = ttk.Label(frame4, text='Alarme')
	frame_4_label.grid(row=0, column = 0)
    
	image = Image.open('tablet.png')
	image = image.resize((120, 150), Image.ANTIALIAS)
	leitor = ImageTk.PhotoImage(image,master = root)    
	valor_alarme = ttk.Label(frame4,text='',image = leitor, compound='center')
    #abaixarSom_button['command'] = lambda: VolumeSom()
	valor_alarme.grid(row=1, column=0)

	

	 
	while True:
		root.update()
		mqttc.loop(.1)

        
		valor_alarme["text"] = status
        
        

if __name__ == '__main__':
    main()
    sys.exit(0)
        

    



main() 

