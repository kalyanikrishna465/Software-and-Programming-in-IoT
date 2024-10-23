import paho.mqtt.client as mqtt
import random
import time

# MQTT Broker settings
broker = "localhost"  # Change to your broker address
port = 1883  # Default MQTT port
topic = "home/temperature"

# Callback function when the client receives a CONNACK response from the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

# Create an MQTT client instance
client = mqtt.Client()

# Attach the on_connect callback
client.on_connect = on_connect

# Connect to the MQTT broker
client.connect(broker, port, 60)

# Start the loop to process network events
client.loop_start()

try:
    while True:
        # Generate a random temperature value
        temperature = random.uniform(20.0, 30.0)
        # Publish the temperature to the topic
        client.publish(topic, temperature)
        print(f"Published {temperature:.2f} to topic '{topic}'")
        time.sleep(2)  # Publish every 2 seconds

except KeyboardInterrupt:
    pass
finally:
    client.loop_stop()
    client.disconnect()