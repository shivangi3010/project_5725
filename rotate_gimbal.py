#This is a simple python script to move the gimbal using readings of accelerometer

import RPi.GPIO as GPIO
import socket
import csv
import time
import os
import math

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)   
GPIO.setup(18,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

UDP_IP = "10.148.3.90"

UDP_PORT = 5555  

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
sock.bind((UDP_IP, UDP_PORT))

# for horizontal rotation
pl = GPIO.PWM(18, 50)
pl.start(0)

# for vertical rotation
pr = GPIO.PWM(13, 50)
pr.start(0)

def setAngle(angle):
    return (angle+90)/18 + 2
   
def dist(a,b):
    return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return math.degrees(radians)
 
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def get_acc(data):
	imu_op = data.split(',')    
	acc_x = float(imu_op[2])
	acc_y = float(imu_op[3])
	acc_z = float(imu_op[4])
	return [acc_x,acc_y,acc_z]

flag = True;

while True:
    data, addr = sock.recvfrom(1024)

    acc_op = get_acc(data)
    
    y_theta = get_y_rotation(acc_op[0],acc_op[1],acc_op[2])
    x_theta = get_x_rotation(acc_op[0],acc_op[1],acc_op[2])
    
    duty_x = int(setAngle(x_theta))
    duty_y = int(setAngle(-y_theta))
    
    if flag :
        pr.ChangeDutyCycle(duty_x)
        pl.ChangeDutyCycle(duty_y)
        x_old = duty_x
        y_old = duty_y
        flag = False
    
    # to stablize the movement of gimbal
    if abs(duty_x - x_old) >= 1:
        pr.ChangeDutyCycle(duty_x)
        x_old = duty_x
    else:
        pr.ChangeDutyCycle(0)
    
    if abs(duty_y - y_old) >= 1 :
        pl.ChangeDutyCycle(duty_y)
        y_old = duty_y
    else:
        pl.ChangeDutyCycle(0)

pl.stop()
pr.stop()
GPIO.cleanup()  
