# -*- coding: utf-8 -*-
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

# IP 記得更改
socket.bind("tcp://172.20.10.9:5556")

# Subscribe to two topics, humidity and temp
# 此處會用到的 function
#   1. socket.setsockopt(zmq.SUBSCRIBE, ....)
''' start of you code '''
topicfilter1 = "humidity"

topicfilter2 = "temp"

socket.setsockopt(zmq.SUBSCRIBE, topicfilter1)

socket.setsockopt(zmq.SUBSCRIBE, topicfilter2)
''' end of you code '''

print("Start!!\n")

temp_sum = 0
humid_sum = 0

for i in range(10):
    # receive temperature
    # 接收到的 mes string 做切割，取出數字的部分，split 後會產生 string list
    # 此處會用到的 function
    #   1. socket.recv()
    #   2. string.split
    ''' start of you code '''
    #mes = socket.recv()
    #print(mes)
    #splitted_str = 
    temp = socket.recv()
    tm = temp.decode()
    print("%s" %(tm))
    temp_s = tm.split(' ')
    temp_sum += int(float(temp_s[2]))
    ''' end of you code '''

    # receive humidity
    # 接收到的 mes string 做切割，取出數字的部分，split 後會產生 string list
    # 此處會用到的 function
    #   1. socket.recv()
    #   2. string.split
    ''' start of you code '''
    #mes = socket.recv()
    #print(mes)
    #splitted_str = 
    humidity = socket.recv()
    hm = humidity.decode()
    print("%s" %(hm))
    humidity_s = hm.split(' ')
    humid_sum += int(float(humidity_s[2]))
    ''' end of you code '''

# Compute average value
print("avg temperature: {}".format(temp_sum / 10.0))
print("avg humidity: {}".format(humid_sum / 10.0))