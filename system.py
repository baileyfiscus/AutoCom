#AutoCom protoype system code. To be implemented across 3 raspberry pi's

import time
import serial

ser = serial.Serial('/dev/ttyUSB0',4800)
ser1 = serial.Serial('/dev/ttyS0',115200,timeout = 3)
LIDAR = ""
GPS = ""

def read_gps():
	x = ser.readline()
	if x[0:7]=='$GPGGA,':
		time = x[7:17] #time is in Grenwich time (I.E 5 hours ahead of Hoboken)
        GPS = time
	    #return time
        #ser.close()

def read_lidar():
    while(ser.in_waiting >= 9):
        if((b'Y' == ser.read()) and ( b'Y' == ser.read())):
            Dist_L = ser.read()
            Dist_H = ser.read()
            Dist_Total = ((ord(Dist_H) * 256) + (ord(Dist_L))) / 10
        LIDAR = str(Dist_Total)
	    #print Dist_Total
            #for i in range (0,5):
                #ser.read()
while True:
    gps = read_gps()
    lidar = read_lidar()
    print gps
    print lidar
	time.sleep(0.5)
