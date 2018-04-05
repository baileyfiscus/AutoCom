import serial
import time
import RPi.GPIO as GPIO

#LEDpin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#GPIO.setup(LEDpin,GPIO.OUT)
#GPIO.output(LEDpin,GPIO.LOW)

#ser = serial.Serial('/dev/ttyAMA0',115200,timeout = 3)
#ser = serial.Serial('/dev/ttyUSB1',115200,timeout = 3)
ser = serial.Serial('/dev/ttyS0',115200,timeout = 3)

''' Code for the RPi
ser.write(0x42)
ser.write(0x57)
ser.write(0x02)
ser.write(0x00)
ser.write(0x00)
ser.write(0x00)
ser.write(0x01)
ser.write(0x06)
'''

''' Code for Arduino
ser.write(bytes(b'B'))
ser.write(bytes(b'W'))
ser.write(bytes(2))
ser.write(bytes(0))
ser.write(bytes(0))
ser.write(bytes(0))
ser.write(bytes(1))
ser.write(bytes(6))
'''

while(True):
    while(ser.in_waiting >= 9):
        if((b'Y' == ser.read()) and ( b'Y' == ser.read())):
            Dist_L = ser.read()
            Dist_H = ser.read()
            Dist_Total = ((ord(Dist_H) * 256) + (ord(Dist_L))) / 10
	    print Dist_Total
            for i in range (0,5):
                ser.read()
