from megapi import *
import pygame
import RPi.GPIO as GPIO

distance = 123

# -=Function=-
def Forward(port, speed):
	sleep(0.4)
	bot.encoderMotorRun(port,speed)

def Backward(port, speed):
	bot.encoderMotorRun(port, speed)

# -=UltrasonicSensor=-
def UltraSonic(port):
	global distance
	distance = port
	print(distance)

# -=SoundPlay=-
def SoundPlay(SoundFile):
	SoundList = ["Ms C.mp3", "Mr Williams.mp3"] # Ms. C = 0 | Mr. W = 1
	pygame.mixer.init()
	pygame.mixer.music.set_volume(0.2) # Volume: (0 - 1)
	pygame.mixer.music.load(SoundList[SoundFile])
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
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

	while True:
		# -=SET UP=-
		if GPIO.input(speaker_buttonPin1) == GPIO.HIGH:
			output = 1
		
		elif GPIO.input(speaker_buttonPin2) == GPIO.HIGH:
			output = 2
		
		else:
			pass

		# -=GO OUT=-
		if output == 1:
			
			# Sound
			SoundPlay(0)
				
			# Ultra Sonic
			bot.ultrasonicSensorRead(6,UltraSonic)
			
			# Movement
			if distance < 8:
				Forward(4, 25)
			else:
				Forward(4, 25) # Left Wheel
				Backward(1, -25) # Right Wheel

		# -=BE QUIET=-
    	elif output == 2:
			if GPIO.input(sound_sensorPin) == GPIO.HIGH:
				SoundPlay(1)
		
		else:
			pass


# Or I can just do if robot button click output = 0
	
