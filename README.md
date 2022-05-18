# MakeBlock-UltraSonicSensor

[![GitHub release](https://img.shields.io/github/release/ssi5/MakeBlock-UltraSonicSensor.svg)](https://GitHub.com/ssi5/MakeBlock-UltraSonicSensor/releases/)
[![MIT license](https://img.shields.io/github/license/ssi5/MakeBlock-UltraSonicSensor)](https://ssi5.mit-license.org/)

This _passion project_ by the students My Nguyen, Thai Le, Phu Le and Triet Do. They applied for the SAMK robot competition 2022.

## SAMK Competition

More about the competition of the SATAKUNTA UNIVERSITY OF APPLIED SCIENCES (SAMK) and this competition: 

https://www.samk.fi/en/education/master-robot-builders/

### Stage 1: May 10th, 2022

The submission from May 9th was successful on May 10th, when 17 out of 78 teams were selected for the final round!

### Final round: May 20th, 2022

We have to wait for the outcome.

## Video of the final product

A video about this project can be [found on YouTube](https://youtu.be/Inp2bbtwn5M)

The presentation ... *will be linked here soon*.

## Build

And that is how it looks like:

![Picture from Friday 2022-05-06](docs/2022-05-06_robot.png)

## Code

The program was running on the Raspberry Pi in python, addressing the MegaPi via serial interface. For transportation the `megapi` library was imported, for audio output the `pygame` library.

This is the final code from May 17th for the final round in this competition:

``` py
from megapi import *
import time
import pygame
import RPi.GPIO as GPIO

announce = time.time()
turning = time.time()
distance = 123

# -=Function=-
def Forward(port, speed):
	sleep(0.4)
	bot.encoderMotorRun(port,-speed)

def Backward(port, speed):
	bot.encoderMotorRun(port, speed)

def Left(port, speed, dist):
	bot.encoderMotorMove(port, speed, dist, Forward)

# -=UltrasonicSensor=-
def UltraSonic(port):
	global distance
	distance = port
	print(distance)

# -=SoundPlay=-
def SoundPlay(SoundFile):
	SoundList = ["Ms C.mp3", "Mr Williams.mp3", "beep.mp3"] # Ms. C = 0 | Mr. W = 1 | beep = 2
	pygame.mixer.init()
	pygame.mixer.music.set_volume(0.2) # Volume: (0 - 1)
	pygame.mixer.music.load(SoundList[SoundFile])
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == False:
		continue

def LightOn(pin):
	GPIO.output(pin, GPIO.HIGH) # Green = 40 | Blue = 36 | Red = 38

def LightOff():
	GPIO.output(36, GPIO.LOW)
	GPIO.output(38, GPIO.LOW)
	GPIO.output(40, GPIO.LOW)

# -=GPIO=-
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

	# Speaker
speaker_buttonPin1 = 32
speaker_buttonPin2 = 22
GPIO.setup(speaker_buttonPin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(speaker_buttonPin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)

    # Sound Sensor
sound_sensorPin = 18
GPIO.setup(sound_sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# -=Main=-
if __name__ == '__main__':
	bot = MegaPi()
	bot.start()
	output = 0
	LightOn(40)
	SoundPlay(2)

	while True:
		# -=SET UP=-
		if GPIO.input(speaker_buttonPin1) == GPIO.HIGH:
			output = 1
		
		if GPIO.input(speaker_buttonPin2) == GPIO.HIGH:
			output = 2
			Forward(4, 0)
			Backward(1, 0)

		# -=GO OUT=-
		if output == 1:
			LightOff()
			LightOn(36)
			
			# Sound
			if time.time() - announce > 10:
				announce = time.time()
				SoundPlay(0)
				
			# Measure Distance (Store in "Distance" global variable)
			bot.ultrasonicSensorRead(6,UltraSonic)
			
			# Movement
			if distance < 20:
				turning = time.time() + 3.5
			
			if (turning - time.time()) > 0:
				# turn
				Left(4, 50, 150)
				Backward(1, 0)
			
			else:
				# drive straight
				Forward(4, 50)
				Backward(1, 50)
		
		# -=BE QUIET=-
		elif output == 2:
			LightOff()
			LightOn(38)
			Forward(4, 0)
			Backward(1, 0)
			if GPIO.input(sound_sensorPin) == GPIO.HIGH:
				SoundPlay(1)
		
		else:
			pass
```

## Remarks
