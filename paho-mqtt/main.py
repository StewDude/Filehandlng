import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buf):
    print("log: " + buf)

def on_connect(client, userdata, flags, rc):
    if(rc == 0):
        print("connected OK")
    else:
        print("Bad connection! Return code = "+ str(rc))

def on_disconnect(client, userdata, flags, rc = 0):
    print("Disconnected. Return code = "+str(rc))

broker = "192.168.1.145"

client = mqtt.Client("paho1")

client.on_log = on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect

print("Connecting to broker...")

client.connect(broker)
client.loop_start()
client.publish("paho/test", "My first message.")
time.sleep(4)
client.loop_stop()
client.disconnect()

