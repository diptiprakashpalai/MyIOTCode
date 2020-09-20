import paho.mqtt.client as mqtt
import time
def on_message (client, userdata, message):
	print ("message received", str(message.payload.decode("utf-8")))
	print ("message topic", message.topic)
	print ("message qos", message.qos)
	print ("message retain flag", message.retain)


client = mqtt.Client ("P1")
for i in range (0,10):
    client.on_message = on_message
    print ("connecting to the broker")
    client.connect ("broker.mqttdashboard.com", 8000, 60)
    client.loop_start()
    client.subscribe("Shaswoti/Home/Automation")
    #client.publish ("Shaswoti/Home/Automation", "Mana")
    time.sleep(2)
    i = i+1
    client.loop_stop()
    print ("Count is %d" %i)
