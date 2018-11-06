import paho.mqtt.client as mqtt
broker = "localhost"
port = 1883

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connectado with result code "+str(rc))

    mqttc.subscribe("lampada")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    
mqttc = mqtt.Client(client_id='lampada')
mqttc.connect(broker,port)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.loop_forever()

  