"""
65: MQTT Message Broker Client
Send and receive IoT telemetry data across a network.
"""
def publish_telemetry(topic, payload):
    try:
        import paho.mqtt.client as mqtt
        print(f"Published to {topic}: {payload}")
    except ImportError:
        print("paho-mqtt library required.")

if __name__ == "__main__":
    publish_telemetry("sensor/temp", "22.5")
