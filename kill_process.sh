#!/bin/bash
sudo kill -9 $(ps -ef  | grep -m1 'python robot_controller.py' | awk '{print $2}')
sudo kill -9 $(ps -ef  | grep -m1 'python rotate_gimbal.py' | awk '{print $2}')
