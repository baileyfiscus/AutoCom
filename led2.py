#! /usr/bin/python
# Import thee libraries we need
import RPi.GPIO as GPIO
import time
#Set the LED GPIO mode
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Set the LED GPIO number
LED =21
LED1 =20
LED2 =16
#Set the LED GPIO pin as an output
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
#Turn the GPIO pin on 
GPIO.output(LED,True)
GPIO.output(LED1,True)
GPIO.output(LED2,True)
#wait 5 seconds
time.sleep(5)
#tURN THE GPIO PIN OFF
GPIO.output(LED,False)
GPIO.output(LED1,False)
GPIO.output(LED2,False)
