#This is a simple python script to move a raspberry pi robot using WiFi
#For Complete Tutorial, visit http://rootsaid.com/robot-control-over-wifi/

import RPi.GPIO as GPIO
import socket
import csv

GPIO.setwarnings(False)


UDP_IP = "10.148.11.149"

UDP_PORT = 5555  

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    raw=data
    print raw
