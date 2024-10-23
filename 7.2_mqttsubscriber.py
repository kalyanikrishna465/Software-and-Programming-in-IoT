import paho.mqtt.client as mqtt

# MQTT Broker settings
broker = "localhost"  # Change to your broker address
port = 1883  # Default MQTT port
topic = "home/temperature"

# Callback function when the client receives a message
def on_message(client, userdata, msg):
    print(f"Received message '{msg.payload.decode()}' from topic '{msg.topic}'")

# Create an MQTT client instance
client = mqtt.Client()

# Attach the on_message callback
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker, port, 60)

# Subscribe to the topic
client.subscribe(topic)

# Start the loop to process network events
client.loop_start()

try:
    while True:
        pass  # Keep the subscriber running

except KeyboardInterrupt:
    pass
finally:
    client.loop_stop()
    client.disconnect()