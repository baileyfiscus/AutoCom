#AutoCom protoype system code. To be implemented across 3 raspberry pi's
#February 2, 2018

import time
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import serial
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.IN)

print GPIO.input(3)
ser = serial.Serial('/dev/ttyUSB0',4800)

def read_gps():
	x = ser.readline()
	if x[0:7]=='$GPGGA,':
		time = x[7:17] #time is in Grenwich time (I.E 5 hours ahead of Hoboken)
	    return time
        #ser.close()

def read_lidar():
    SPI_PORT   = 0
    SPI_DEVICE = 0
    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
	return mcp.read_adc(0)

while True:
    #gps = read_gps()
    #lidar = read_lidar
    print gps
    print lidar
	time.sleep(0.5)
