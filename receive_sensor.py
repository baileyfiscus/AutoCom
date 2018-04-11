#Code to receive data over the socket

import socket
import RPi.GPIO as GPIO
import time


UDP_IP = "155.246.202.131"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
GREEN = 20
YELLOW = 21
RED = 16

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    data_int = int(data)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(YELLOW, GPIO.OUT)
    GPIO.setup(GREEN, GPIO.OUT)
    if data_int <= 60:
        print "Red"
        GPIO.output(GREEN,False)
        GPIO.output(YELLOW,False)
        GPIO.output(RED,True)
        #time.sleep(1)
    if (60 < data_int <= 90):
        print "Yellow"
        GPIO.output(RED,False)
        GPIO.output(GREEN,False)
        GPIO.output(YELLOW,True)
        #time.sleep(1)
    if (90 < data_int <= 120):
        print "Green"
        GPIO.output(RED,False)
        GPIO.output(YELLOW,False)
        GPIO.output(GREEN,True)
        #time.sleep(1)
