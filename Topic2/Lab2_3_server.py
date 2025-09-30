# -*- coding: utf-8 -*-
import zmq
import random
import time

import Adafruit_DHT

# Setup DHT11 
sensor_args = {'11' : Adafruit_DHT.DHT11,
               '22': Adafruit_DHT.DHT22,
               '2302': Adafruit_DHT.AM2302}
sensor = sensor_args['11']

# GPIO#, ex: GPIO4 = Pin7
gpio = 4

context = zmq.Context()
socket = context.socket(zmq.PUB)

# IP 記得更改
socket.connect("tcp://172.20.10.9:5556")


while True:
    # 從溫濕度模組取的數值
    # 此處會用到的 function
    #    1.  Adafruit_DHT.read_retry(...., ....)

    ''' start of you code '''
    humidity, temp = Adafruit_DHT.read_retry(sensor, gpio)
    humidity = str(humidity)
    temp = str(temp)  
    
    ''' end of you code '''

    socket.send(("temp = %s" % (temp)).encode('utf-8'))
    time.sleep(0.5)

    socket.send(("humidity = %s" % (humidity)).encode('utf-8'))
    time.sleep(0.5)
