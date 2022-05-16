from megapi import *

def onRead(v):
	print("distance:"+str(v)+" cm");

if __name__ == '__main__':
	bot = MegaPi()
	bot.start()
	while 1:
		sleep(0.1);
		bot.ultrasonicSensorRead(6,onRead);