import time
import paho.mqtt.client as mqtt
broker_url = "iot.eclipse.org"


def mqtt_client_connect():
    print("connected to: ", broker_url)
    client.connect(broker_url)
    client.loop_start()


client = mqtt.Client("client_name")
mqtt_client_connect()

while True:
    print('MQTT TA COMEÇANDO A TER ROSTO')