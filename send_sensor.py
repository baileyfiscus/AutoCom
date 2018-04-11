#AutoCom protoype system code. To be implemented across 3 raspberry pi's

import time
import serial
import socket

ser = serial.Serial('/dev/ttyUSB0',4800)
ser1 = serial.Serial('/dev/ttyS0',115200,timeout = 3)
LIDAR = ""
GPS = ""
MESSAGE = ""
UDP_IP = "155.246.202.131"
UDP_PORT = 5005

def read_gps():
	x = ser.readline()
	if x[0:7]=='$GPGGA,':
		time = x[7:17] #time is in Grenwich time (I.E 5 hours ahead of Hoboken)
        GPS = time
        return
	    #return time
        #ser.close()

def read_lidar():
    while(ser.in_waiting >= 9):
        if((b'Y' == ser.read()) and ( b'Y' == ser.read())):
            Dist_L = ser.read()
            Dist_H = ser.read()
            Dist_Total = ((ord(Dist_H) * 256) + (ord(Dist_L))) / 10
        LIDAR = str(Dist_Total)
        return
	    #print Dist_Total
            #for i in range (0,5):
                #ser.read()
while True:
    # read_gps()
    read_lidar()
    # print "GPS: ", GPS
    print "Lidar: ", LIDAR
    MESSAGE = LIDAR
    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "message:", MESSAGE
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	# time.sleep(0.5)
