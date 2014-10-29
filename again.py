from myro import *
init("/dev/tty.Fluke2-052F-Fluke2")

class Guatmobile:

	# Setting constant parameters
	motorPower = 1
	leftTime = 0.64
	rightTime = 0.67
	forwardTime = 0.5

	# Logic variables
	done = 0
	counter = 0

	# Functions for movements

	# Move forward for set forwardTime
	def bitForward():
		forward(motorPower, forwardTime)

	# 90 degree left turn
	def leftRight():
		turnLeft(motorPower, leftTime)

	# 90 degree right turn
 	def rightRight():
		turnRight(motorPower, rightTime)

	forward(1)
	done = 0

	while done == 0:
    	if getObstacle("center") > 3500:
        	done = 1

	turnLeft(1)

	while done == 0:
    	if getObstacle("center") < 5:
        	done = 1

	done = 0
	counter = 0

	while counter < 2:
		self.bitForward()
		self.rightRight()
		if getObstacle("center") < 5:
			counter += 1
			self.leftRight()
			self.bitForward()
			self.rightRight()
			self.bitForward()
		else:
			leftRight()

	forward(1, 2)
	turnLeft(1, 0.65)
	forward(1, 2)