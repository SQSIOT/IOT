#!/usr/bin/env python
import socket
TCP_IP = '192.168.1.102'
TCP_PORT = 80
BUFFER_SIZE = 1024
MESSAGE1 = "/gpio/0"
MESSAGE2 = "/gpio/1"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

if(msg == MESSAGE1)
{
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()
}
if(msg == MESSAGE2)
{
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()
}
print "received data:", data
