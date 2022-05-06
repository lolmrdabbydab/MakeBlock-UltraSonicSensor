from megapi import *
import pygame
import RPi.GPIO as GPIO

# -=Function=-
def Forward(port):
	sleep(0.4)
	bot.encoderMotorMove(port,100,-1000, Backward)

def Backward(port):
	sleep(0.4)
	print("Running Backward")
	bot.encoderMotorMove(port,100,1000, Forward)

# -=UltrasonicSensor=-
def UltraSonic(port):
	if port == None:
		port = 400
	return port

# -=Main=-
if __name__ == '__main__':
	bot = MegaPi()
	bot.start()

	while True:
		distance = bot.ultrasonicSensorRead(6,UltraSonic)
		if distance < 8:
			Forward(4)
