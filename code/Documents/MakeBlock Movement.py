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
	print("distance:"+str(port)+" cm")
	return int(port)

# -=Main=-
if __name__ == '__main__':
	bot = MegaPi()
	bot.start()

	while True:
		# Ultra Sonic
		#distance = UltraSonic(6)

		# Movement
		'''
		if distance < 8:
			Forward(4)
		'''
	
		Forward(4) # Left Wheel
		Forward(1) # Right Wheel