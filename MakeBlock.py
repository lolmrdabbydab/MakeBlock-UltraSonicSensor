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

	# Robot
robot_buttonPin = num
GPIO.setup(robot_buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


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
		
		elif GPIO.input(robot_buttonPin) == GPIO.HIGH:
			output = 0
		
		else:
			pass

		# -=GO OUT=-
		if output == 1:
			
			# Sound
			SoundPlay(0)
				
			# Ultra Sonic
			distance = bot.ultrasonicSensorRead(6,UltraSonic)
			
			# Movement
			if distance < 8:
				Forward(4)
			Forward(4) # Left Wheel
			Backward(1) # Right Wheel

		# -=BE QUIET=-
    	elif output == 2:
			if GPIO.input(sound_sensorPin) == GPIO.HIGH:
				SoundPlay(1)
		
		else:
			pass


# Or I can just do if robot button click output = 0
	
