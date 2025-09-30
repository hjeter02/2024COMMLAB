# -*- coding: utf-8 -*-
import os
import zmq

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:7788")

print('Worker %s is running ...' % os.getpid())

while True:
    # Receive a, b from the client
    # 此處會用到的 function
    #   1. socket.recv_multipart()
    ''' start of you code '''
    a,b=socket.recv_multipart()
    ans=int(a.decode())+int(b.decode())
    print('compute %s + %s and send response'%(a.decode(),b.decode()))
    socket.send_multipart([str(ans),str(os.getpid())])
    ''' end of you code '''

    # Return the result back to the client
    # 此處會用到的 function
    #   1. socket.send_string(....)
    ''' start of you code '''
    
    ''' end of you code '''




