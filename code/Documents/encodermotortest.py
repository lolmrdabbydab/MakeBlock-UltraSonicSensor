from megapi import *

def onForwardFinish(slot):
	sleep(0.4);
	bot.encoderMotorMove(slot,100,-1000,onBackwardFinish);

def onBackwardFinish(slot):
	sleep(0.4);
	print("slot")
	bot.encoderMotorMove(slot,100,1000,onForwardFinish);

if __name__ == '__main__':
	bot = MegaPi()
	bot.start()
	bot.encoderMotorRun(4,0);
	sleep(1);
	onForwardFinish(4);
	while 1:
		continue;