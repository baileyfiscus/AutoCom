# Author: Bailey Fiscus

import socket
import RPi.GPIO as GPIO
import time
import serial

ser1 = serial.Serial('/dev/ttyS0',115200,timeout = 3)
LIDAR = ""
GPS = ""
MESSAGE = ""
UDP_IP_SEND = "155.246.201.102" # This is the IP address of the other pi
UDP_PORT_SEND = 5006 # This has to match the UDP_PORT_RECEIVE of the other pi

UDP_IP_RECEIVE = "155.246.202.92" # This is the IP address of this pi
UDP_PORT_RECEIVE = 5005
sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP_RECEIVE, UDP_PORT_RECEIVE))
sock.setblocking(0)

errorVar = 0 # used to fix issue with indentation after try/ except in receive()
GREEN = 20
YELLOW = 21
RED = 16

def read_lidar():
    Dist_Total = 0
    while(Dist_Total == 0):
        while(ser1.in_waiting >= 9):
            if((b'Y' == ser1.read()) and ( b'Y' == ser1.read())):
                Dist_L = ser1.read()
                Dist_H = ser1.read()
                Dist_Total = ((ord(Dist_H) * 256) + (ord(Dist_L))) / 10
    return str(Dist_Total)

def send():
    LIDAR = read_lidar()
    MESSAGE = LIDAR
    print "UDP target IP:", UDP_IP_SEND, "UDP target port:", UDP_PORT_SEND, "message:", MESSAGE
    sendSock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
    sendSock.setblocking(0)
    sendSock.sendto(MESSAGE, (UDP_IP_SEND, UDP_PORT_SEND))

def receive():
    try:
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
        if (120 < data_int):
            print "Green"
            GPIO.output(RED,False)
            GPIO.output(YELLOW,False)
            GPIO.output(GREEN,False)
    except:
        errorVar = 0

if __name__ == '__main__':
    while True:
        send()
        receive()
