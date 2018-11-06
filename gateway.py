import ssl
import sys
import paho.mqtt.client as mqtt
import paho.mqtt.publish

broker = "localhost"
port = 1883
from  time import sleep 

mqttc = mqtt.Client("gateway")
mqttc.connect(broker,port)
mqttc.loop_start()

while True:
	mqttc.publish("lampada", "off")

	for contagem in range(0,5):
		sleep(1)

	mqttc.publish("som", "up")

	mqttc.publish("tranca", "locked")

	for contagem in range(0,5):
		sleep(1)

	mqttc.publish("alarme", "6:00")


	for x in range(0,6):
		temp = 30 + x 
    	mqttc.publish("termometro : ", str(temp))
    	#Apos 3 segundos aumenta a temperatura
    	for contagem in range(0,3):
	    	sleep(1)
	    
  	#Depois de 5 segundos a lampada acende  
	for contagem in range(0,5):
		sleep(1)

	mqttc.publish("lampada", "on")
    
	
	for contagem in range(0,10):
		sleep(1)

	mqttc.disconnect() #disconnect
	mqttc.loop_stop() 

