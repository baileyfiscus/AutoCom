#Code to receive data over the socket

import threading
from threading import Thread
import socket
import RPi.GPIO as GPIO
import time
import csv

MESSAGE = "80085"
UDP_IP_SEND = "155.246.202.88" # This is the IP address of the other pi
UDP_PORT_SEND = 5006 # This has to match the UDP_PORT_RECEIVE of the other pi

UDP_IP_RECEIVE = "155.246.201.234" # This is the IP address of this pi
UDP_PORT_RECEIVE = 5005
sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP_RECEIVE, UDP_PORT_RECEIVE))

def send():
    f.write("UDP target IP:", UDP_IP)
    f.write(", UDP target port:", UDP_PORT)
    f.write(", message:", MESSAGE)
    f.write(", @", time.clock())
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

def receive():
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    data_int = int(data)

if __name__ == '__main__':
    f.open('traffic.txt','w')
    while True:
        send()
        receive()
    # Thread(target = send).start()
    # Thread(target = receive).start()
