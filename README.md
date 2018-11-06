# Distribuidos
#Repositorio para o Trabalho de MQTT

Inicialmente deve-se baixar e configurar o Mosquitto e baixar a Função Paho. Seguiu-se os seguintes passos:

1. Instalando o Mosquitto
> sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
> sudo apt-get update
> sudo apt-get install mosquitto mosquitto-clients

2.Instalando o Paho
>pip install paho-mqtt

3. Configurando o Mosquitto 
> sudo nano /etc/mosquitto/mosquitto.conf

E configurando o arquivo para estar dessa forma:
persistence true
persistence_location /var/lib/mosquitto/
allow_anonymous false
log_dest file /var/log/mosquitto/mosquitto.log
include_dir /etc/mosquitto/conf.d

> wget https://github.com/eclipse/mosquitto/blob/master/mosquitto.conf

4.Adcionando informações para Mosquitto
> sudo nano /etc/mosquitto/conf.d/default.conf

password_file /etc/mosquitto/passwd
listener 1883 localhost
listener 8883
certfile /etc/letsencrypt/live/[hostname]/fullchain.pem
cafile /etc/letsencrypt/live/[hostname]/chain.pem
keyfile /etc/letsencrypt/live/[hostname]/privkey.pem

Finalmente, para testar se funcionou fizemos um Subscriber e Publisher de teste dessa forma:
#para o subscriber
mosquitto_sub -h localhost -p 1883 -t [topic] 
#para o publisher
mosquitto_pub -h  localhost -p 1883 -t [topic]  -m [message] 

