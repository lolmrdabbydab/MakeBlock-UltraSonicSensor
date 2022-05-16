import RPi.GPIO as GPIO
from megapi import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(18) == GPIO.HIGH:
        sleep(1)
        print("Button was pressed")