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
	distanceList = list(port)
	filteredList = [filter(None, distanceList)]
	port = filteredList[0]
	return int(port)

# -=Main=-
if __name__ == '__main__':
	bot = MegaPi()
	bot.start()

	while True:
		distance = bot.ultrasonicSensorRead(6,UltraSonic)
		print(distance)
		print(type(distance))
		sleep(2)
		'''
		if distance < 8:
			Forward(4)
			'''
