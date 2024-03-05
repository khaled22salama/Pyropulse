#Author: Khaled Salama
#LinkedIn: https://www.linkedin.com/in/5aledsalama/
# Overview: This Python script is designed to run on a Raspberry Pi Zero 2 W along with the Camera Module 3.
# It provides both live First Person View (FPV) footage for flying and high-definition recording to microSD.
# The live preview is displayed with DRM support, and the recorded video is encoded in H.264 format with a
# specified bitrate. The script is designed to be versatile, offering an FPV experience while allowing users
# to record high-quality footage during flights.
# It can record at 1080p 30FPS, but only with a GPU overclock. Short stutters still happen.
# Import necessary libraries and modules
import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN)
if GPIO.input(15) == 1:
	while GPIO.input(15) == 1:
		time.sleep(0.2)
	while GPIO.input(15) == 0:
		time.sleep(0.2)
	os.system("sudo poweroff")

else:
	command = "libcamera-vid -t 0 -b 9000000 --vflip --hflip --autofocus-mode=manual --lens-position=0.0 --width 1920 --height 1080 --framerate 30 --codec libav -o Flight"+str(int(time.time()))+".mp4 &"
	#command = "libcamera-vid -t 0 -b 9000000 --vflip --hflip --autofocus-mode=manual --lens-position=0.0 --width 1280 --height 720 --framerate 60 --codec libav -o Flight"+str(int(time.time()))+".mp4 &"
	#command = "libcamera-vid -t 0 -b 9000000 --encode main --preview lores --vflip --hflip --autofocus-mode=manual --lens-position=0.0 --width 1280 --height 720 --framerate 60 --codec libav -o Flight"+str(int(time.time()))+".mp4 &"
	os.system(command)

	while GPIO.input(15) == 0:
		time.sleep(0.1)
	#time.sleep(5)
	os.system("pkill -SIGINT libcamera-vid; sudo poweroff")
