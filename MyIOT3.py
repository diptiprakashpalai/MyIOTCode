import paho.mqtt.client as mqtt
import time
def on_message(client, userdata, message):
    print ("message received", str(message.payload.decode("utf-8")))
	print ("message topic", message.topic)
	print ("message qos", message.qos)
client = mqtt.client("P1")
client.on_message = on_message
for i in range (0,6)
   print ("connecting to the broker")
   client.connect ("broker.mqttdashboard.com", 1883, 60)
   client.loop.start()
   client.subscribe("BLEKFIEFF")
   client.loop.stop()
   i = i+ 1
   print (" I subscribed the message % d times" %i)
