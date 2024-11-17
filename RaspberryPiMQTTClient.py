import Adafruit_DHT
import paho.mqtt.client as mqtt
import time
import json

SENSOR = Adafruit_DHT.DHT11
GPIO_PIN = 4

BROKER_ADRESS = "IP_DO_BROKER_BITDOGLAB"
TOPIC = "bitdoglab/raspberry/dados"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker no BitDogLab!")
    else:
        print(f"Erro de conexão com o broker: {rc}")

client = mqtt.Client("RaspberryPi_RealData")
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
            client.publish(TOPIC, message)
            print(f"Dados reais enviados: {message}")
        else:
            print("Falha na leitura do sensor. Tentando novamente...")

        time.sleep(10)

except KeyboardInterrupt:
    print("Encerrando...")

finally:
    client.loop_stop()
    client.disconnect()
