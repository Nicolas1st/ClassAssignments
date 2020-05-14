from SunCloudStuff import *
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

publisher = mqtt.Client()
publisher.connected = False
publisher.connect(ip_address, 1883, 60)

publisher.on_connect = on_connect
publisher.on_disconnect = on_disconnect
publisher.on_message = on_message

publisher.loop_start()

sun = Sun(100, math.pi/2, 12)  # height, angle, day_length
cloud = Cloud(60, 10, -50, 10)  # height, width, position, velocity
sensor = LightDetector(0)
for i in range(100):
    sun.move(1)
    cloud.move(10)
    print(sensor.is_sunny(sun, cloud))
    publisher.publish(sensor.is_sunny(sun, cloud))

publisher.disconnect()
publisher.loop_stop()
