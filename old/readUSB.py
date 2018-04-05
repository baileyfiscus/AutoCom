import serial
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.IN)
#print GPIO.input(2)
print GPIO.input(3)
ser = serial.Serial('/dev/ttyUSB0',4800)
#Writes the data from the gps 100 times to a text file
#f = open("GPS_Data.txt","w+")

#print '>Writing data...'
#for i in range(100):
#	x = ser.readline()
#	f.write(x)
#f.close()
#print x

#Constant readings from the gps
while True:
	x = ser.readline()
	if x[0:7]=='$GPGGA,':
		time = x[7:17]
		#time is in Grenwich time (I.E 5 hours ahead of Hoboken)
		print time
ser.close()
