import sys
from Adafruit_IO import MQTTClient
import time
import random
from simple_ai import *

AIO_FEED_ID = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = "congphu"
AIO_KEY = "aio_OzAl33En6huO0gVLFEIQGuGKDFs9"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + "feed id: " + feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
sensor_type = 0
counter_ai = 5

while True:
    counter = counter - 1
    if counter <= 0:
        counter = 10
        # print("Random data is publishing...")
        if sensor_type == 0:
            print("Temperature data is publishing...")
            sensor_type = 1
            temp = random.randint(10, 20)
            client.publish("cambien1", temp)
        elif sensor_type == 1:
            print("Light data is publishing...")
            sensor_type = 2
            light = random.randint(100, 500)
            client.publish("cambien2", light)
        elif sensor_type == 2:
            print("Humid data is publishing...")
            sensor_type = 0
            humi = random.randint(50, 70)
            client.publish("cambien3", humi)

    counter_ai = counter_ai - 1
    if counter_ai <= 0:
        counter_ai = 5
        previous_result = ai_result
        ai_result = image_dectector()
        print("AI output: ", ai_result)
        if previous_result != ai_result:
            client.publish("ai", ai_result)

    time.sleep(1)
    pass