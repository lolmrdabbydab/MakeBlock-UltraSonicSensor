from megapi import *

# -=Movement=-
def Forward(port):
	sleep(0.4);
	bot.encoderMotorMove(port,100,-1000, Backward);

def Backward(port):
	sleep(0.4);
	print("Running Backward")
	bot.encoderMotorMove(port,100,1000, Forward);

# -=UltrasonicSensor=-
def UltraSonic(port):
	print("distance:"+str(port)+" cm");


# -=Main=-
if __name__ == '__main__':
	bot = MegaPi()
	bot.start()
	bot.encoderMotorRun(4,0);
	sleep(1);
	for i in range(10):
		print("Port 4 Forward")
		Forward(1);
	
	for i in range(10):
		print("Port 4 Backward")
		Backward(1);

	'''
	print("Port 2")

	Forward(2);
	'''
	while True:
		sleep(0.1);
		bot.ultrasonicSensorRead(6,UltraSonic);
		continue;