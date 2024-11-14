import Adafruit_DHT
import paho.mqtt.client as mqtt
import time
import json

SENSOR = Adafruit_DHT.DHT11
GPIO_PIN = 4

BROKEN_ADRESS = "IP_DO_BROKER_BITDOGLAB"
TOPIC - "bitdoglab/raspberry/dados"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker no bitdoglab!")
    else:
        print(f"erro de conexão com broker: {rc}")

ckient = mqtt.Client("RaspberryPi_RealData")
client.on_connect = on_connect
client.connect(BROKER_ADRESS)

try:
    client.loop_start()
    while True: 
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, GPIO_PIN)

        if humidity is not None and temperature is not None:
            data = {
                "temperatura": temperature,
                "umidade": humidity
            }
            message = json.dumps(data)

            client.publish(topic, message)
            print(f"dados reais enviados: {nessage}")
        else:
            print("falha na leitura do sensor. retransmitindo...")

        time.sleep(10)

except KeyboardInterrupt:
    print("encerrando...")
finally:
    client.loop_stop()
    client.disconnect()