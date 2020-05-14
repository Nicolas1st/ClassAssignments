import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print('Connected to ' + str(rc))
    client.subscribe("topic/test")
    client.connection_flag = True


def on_disconnect(client, userdata, flags, rc):
    if rc != 0:
        print('Unexpected disconnection.')
    else:
        print('Disconnected.')
    client.unsubscribe("topic/test")
    client.connection_flag = False


def on_message(client, userdata, msg):
    if msg.payload.decode().lower() == "Stop":
        client.disconnect()


ip_address = input('What is the ip address of the mqtt broker you want to connect to? ')

client = mqtt.Client()
client.connected = False
client.connect(ip_address, 1883, 60)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.loop_start()

while client.connected:
    pass

client.disconnect()
client.loop_stop()


