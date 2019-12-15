#This is a simple python script to move a raspberry pi robot using WiFi
#For Complete Tutorial, visit http://rootsaid.com/robot-control-over-wifi/

import RPi.GPIO as GPIO
import socket
import csv
import time
import os
import re
import subprocess


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)   
GPIO.setup(27,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
#GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)  

#Setting up UDP ip address and port 
UDP_IP = "10.148.3.90"
UDP_PORT = 5050

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))

#def GPIO17_callback(channel):
#    pl.stop()
#    pr.stop()
#    GPIO.cleanup()
#    exit()

#GPIO.add_event_detect(17,GPIO.FALLING, callback=GPIO17_callback, bouncetime=300)

pl = GPIO.PWM(27, 50)
pl.start(0)

pr = GPIO.PWM(26, 50)
pr.start(0)

while True:
 data, addr = sock.recvfrom(1024)
 raw=data

 #print raw

 if raw=="forward":
    pr.ChangeDutyCycle(7.9)
    pl.ChangeDutyCycle(5.9) 
    print "Robot Move Forward"
  
  
 elif raw=="stop":
    pr.ChangeDutyCycle(0)
    pl.ChangeDutyCycle(0)
    print "Robot Stop"
    

 elif raw=="backward":
    pr.ChangeDutyCycle(5.9)
    pl.ChangeDutyCycle(7.9)
    print "Robot Move Backward"

 elif raw=="right":
    pr.ChangeDutyCycle(7.9)
    pl.ChangeDutyCycle(0)  
    print "Robot Move Left"

 elif raw=="left":
    pr.ChangeDutyCycle(0)
    pl.ChangeDutyCycle(5.9)   
    print "Robot Move Right"

 else:
    print "Killing all processes and sending control back to user"  
    pr.ChangeDutyCycle(0)
    pl.ChangeDutyCycle(0)
    subprocess.call("./kill_process.sh")

pl.stop()
pr.stop()
GPIO.cleanup()
