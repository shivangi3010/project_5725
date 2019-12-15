#This is a simple python script to move a raspberry pi robot using WiFi
#For Complete Tutorial, visit http://rootsaid.com/robot-control-over-wifi/

import RPi.GPIO as GPIO
import socket
import csv
import time
import os
import math

UDP_IP = "10.148.11.149"

UDP_PORT = 5555  

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
sock.bind((UDP_IP, UDP_PORT))

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
        
while True:
    data, addr = sock.recvfrom(1024)
    
    acc_op = get_acc(data)
    
    y_theta = get_y_rotation(acc_op[0],acc_op[1],acc_op[2])
    x_theta = get_x_rotation(acc_op[0],acc_op[1],acc_op[2])
    #print(y_theta , "y_th" )
    print(x_theta , "x_th")
    #time.sleep(1)
    
    
    
