#Code to receive data over the socket

import socket
import RPi.GPIO as GPIO
import time


UDP_IP = "155.246.202.131"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    data_int = int(data)
    if data <= 60:
        GPIO.setmode(GPIO.BCM)
        LED = 16
        GPIO.setup(LED, GPIO.OUT)
        GPIO.output(LED,True)
        time.sleep(5)
        GPIO.output(LED,False)
    if (60 < data <= 90):
        GPIO.setmode(GPIO.BCM)
        LED = 21
        GPIO.setup(LED, GPIO.OUT)
        GPIO.output(LED,True)
        time.sleep(5)
        GPIO.output(LED,False)
    if (90 < data <= 120):
        GPIO.setmode(GPIO.BCM)
        LED = 20
        GPIO.setup(LED, GPIO.OUT)
        GPIO.output(LED,True)
        time.sleep(5)
        GPIO.output(LED,False)
