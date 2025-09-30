# -*- coding: utf-8 -*-
import zmq
import random
import time

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.bind("tcp://*:7788")

# wait for all workers connected
time.sleep(1)

for i in range(9):
    a = str(random.randint(0, 100))
    b = str(random.randint(0, 100))
    
    # Send integer a, b to servers
    # 此處會用到的 functions
    #   1. socket.send_multipart
    ''' start of you code '''
    print("compute %s + %s ..."%(a,b))
    socket.send_multipart([a.encode('utf-8'),b.encode('utf-8')])
    ''' end of you code '''

    # receive results from servers
    # 此處會用到的 function
    #   1. socket.recv()
    ''' start of you code '''
    ans,addres=socket.recv_multipart()
    print('= %s (from worker %s)'%(ans.decode('utf-8'),addres.decode('utf-8')))
    ''' end of you code '''

