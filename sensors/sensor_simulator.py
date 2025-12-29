import paho.mqtt.client as mqtt
import json
import time
import random

# Brokers to try
brokers = [
    ("broker.hivemq.com", 1883),
    ("test.mosquitto.org", 1883),
    ("broker.emqx.io", 1883)
]

topic = "smart_adri_irrigation/sensor"

soil_types = ["Loamy", "Clay", "Sandy"]
crops = ["Rice", "Wheat", "Sugarcane"]
seasons = ["Kharif", "Rabi", "Summer", "Winter"]

client = mqtt.Client()

def connect_to_broker():
    for broker, port in brokers:
        try:
            print(f"Trying to connect to broker: {broker}:{port}")
            client.connect(broker, port, keepalive=60)
            print(f"✅ Connected to broker: {broker}")
            return True
        except Exception as e:
            print(f"❌ Could not connect to {broker}:{port} -> {e}")
    return False

if not connect_to_broker():
    print("No brokers available. Exiting...")
    exit(1)

# Publish only every 10 seconds
counter = 0
while True:
    data = {
        "Rainfall": random.randint(0,200),
        "Temperature": random.randint(20,40),
        "Humidity": random.randint(30,90),
        "Soil_Type": random.choice(soil_types),
        "Crop": random.choice(crops),
        "Season": random.choice(seasons)
    }
    try:
        client.publish(topic, json.dumps(data))
        counter += 1
        # Print only every 3 publishes
        if counter % 3 == 0:
            print("Published:", data)
    except Exception as e:
        print("Publish failed:", e)
        if not connect_to_broker():
            print("No brokers available. Waiting 10 seconds...")
            time.sleep(10)
            continue
    time.sleep(2)  # Increase interval to reduce load
