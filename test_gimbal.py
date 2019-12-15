#This is a simple python script to move a raspberry pi robot using WiFi
#For Complete Tutorial, visit http://rootsaid.com/robot-control-over-wifi/

import RPi.GPIO as GPIO
import socket
import csv
import time
import os

global duty
duty = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)   
GPIO.setup(18,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
#GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)  

#def GPIO17_callback(channel):
#    pl.stop()
#    pr.stop()
#    GPIO.cleanup()
#    exit()

#GPIO.add_event_detect(17,GPIO.FALLING, callback=GPIO17_callback, bouncetime=300)

pl = GPIO.PWM(18, 50)
pl.start(0)

pr = GPIO.PWM(13, 50)
pr.start(0)


def setAngle(angle):
    global duty
    duty = (angle+90)/18 + 2
    
while True:
 setAngle(60)
 pr.ChangeDutyCycle(duty)
 #time.sleep(2)
 setAngle(-90)
 pl.ChangeDutyCycle(duty)
 #time.sleep(2)

 #print raw

 

pl.stop()
pr.stop()
GPIO.cleanup()
