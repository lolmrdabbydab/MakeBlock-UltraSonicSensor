from megapi import *
import time
import pygame
import RPi.GPIO as GPIO

announce = time.time()
distance = 123

# -=Function=-
def Forward(port, speed):
	sleep(0.4)
	bot.encoderMotorRun(port,-speed)

def Backward(port, speed):
	bot.encoderMotorRun(port, speed)

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

# -=GPIO=-
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

	# Speaker
speaker_buttonPin1 = 32
speaker_buttonPin2 = 22
GPIO.setup(speaker_buttonPin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(speaker_buttonPin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Sound Sensor
sound_sensorPin = 18
GPIO.setup(sound_sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# -=Main=-
if __name__ == '__main__':
	bot = MegaPi()
	bot.start()
	output = 0
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
			
			# Sound
			if time.time() - announce > 30:
				announce = time.time()
				SoundPlay(0)
				
			# Measure Distance (Store in "Distance" global variable)
			bot.ultrasonicSensorRead(6,UltraSonic)
			
			# Movement
			if distance < 20:
				Forward(4,50)
				Backward(1, 0)
			else:
				Forward(4, 50) # Left Wheel
				Backward(1, 50) # Right Wheel

		# -=BE QUIET=-
		elif output == 2:
			Forward(4, 0)
			Backward(1, 0)
			if GPIO.input(sound_sensorPin) == GPIO.HIGH:
				print("MAMA MIA")
				SoundPlay(1)
		
		else:
			pass
