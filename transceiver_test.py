#Code to receive data over the socket

import socket
import RPi.GPIO as GPIO
import time

MESSAGE = "80085"
UDP_IP_SEND = "155.246.201.102" # This is the IP address of the other pi
UDP_PORT_SEND = 5006 # This has to match the UDP_PORT_RECEIVE of the other pi

UDP_IP_RECEIVE = "155.246.202.92" # This is the IP address of this pi
UDP_PORT_RECEIVE = 5005
sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP_RECEIVE, UDP_PORT_RECEIVE))
sock.setblocking(0)
stupidVar = 0

def send():
    print "UDP target IP:", UDP_IP_SEND
    print ", UDP target port:", UDP_PORT_SEND
    print ", message:", MESSAGE
    sendSock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sendSock.sendto(MESSAGE, (UDP_IP_SEND, UDP_PORT_SEND))

def receive():
    try:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        "received message:", data
    except:
        stupidVar = 0

if __name__ == '__main__':
    while True:
        send()
        receive()
