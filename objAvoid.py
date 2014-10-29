# Program for Myro Scribbler Bot Object Avoidance
# -----------------------------------------------
# Authors:
# 
# Pranav Anand
# Olivia Cao
# Guatam Gupta
# Nakul Pathak
# Ross Semenov
# Wojciech Swiderski
# Jason Zukewich

from myro import *
from time import time

init("/dev/tty.Fluke2-052F-Fluke2")

# Robot class
class Guatmobile:

	# Setting parameter variables
	motorPower = 1
	leftTime = 0.64
	rightTime = 0.66
	forwardTime = 0.5
	distanceUpper = 2500
	distanceLower = 5

	# Logic Variables
	done = 0
	counter = 0
	beginTime = 0
	turntime = 0

	# Move forward for set forwardTime
	def bitForward(self):
		forward(self.motorPower, self.forwardTime)

	# 90 degree left turn
	def leftRight(self):
		turnLeft(self.motorPower, self.leftTime)

	# 90 degree right turn
 	def rightRight(self):
		turnRight(self.motorPower, self.rightTime)

	# Functions to calculate how long it took to turn at the beginning
	def startTime(self):
		self.beginTime = time()

	def endTime(self):
		self.turnTime = time() - self.beginTime
		return self.turnTime

	# Check for wall on right of robot
	def checkRight(self):
		value = False
		self.rightRight()
		if getObstacle("center") > self.distanceUpper:
			value = True
		turnLeft(self.motorPower)
		self.delayLeft()
		stop()
		return value

	# Delaying functions
	def delayForward(self):
		while self.done == 0:
			if getObstacle(1) > self.distanceUpper:
				self.done = 1
		self.done = 0

	def delayLeft(self):
		while self.done == 0:
			if getObstacle(2) < self.distanceLower:
				self.done = 1
		self.done = 0

	def delayRight(self):
		while self.done == 0:
			if getObstacle(2) > self.distanceLower:
				self.done = 1
		self.done = 0

# -------------------- Start of Run Sequence ----------------------

# Main function that runs the sequence for the robot
def run(left = 0.65, right = 0.40, forwards = 0.5, upper = 3000, lower = 5):

	# Initialize
	robot = Guatmobile()

	robot.leftTime = left
	robot.rightTime = right
	robot.forwardTime = forwards
	robot.istanceUpper = upper
	robot.distanceLower = lower

	# Drive forward until detects wall
	forward(robot.motorPower)
	robot.delayForward()

	# Turn left until no longer detects wall
	turnLeft(robot.motorPower)
	robot.delayLeft()

	# Each counter represents turning around the corner of the box
	while robot.counter < 2:
		robot.bitForward()
		if not robot.checkRight():
			robot.counter = robot.counter + 1
			robot.bitForward()
			robot.rightRight()
			robot.bitForward()

	robot.bitForward()

	# Turn back to correct angle

# -------------------- End of Run Sequence ----------------------

# User Control
finished = 0

while finished == 0:
	select = raw_input("Enter 's' to select parameters\nEnter 'd' to run default values\nEnter 'q' to quit program\n")

	# Prompt user for all parameters
	if select == 's':
		left = raw_input("Left Time\n")
		right = raw_input("Right Time\n")
		forwards = raw_input("Forward Time\n")
		upper = raw_input("Upper Obstacle Limit\n")
		lower = raw_input("Lower Obstacle Limit\n")
		run(left, right, forwards, upper, lower)

	# Uses default parameters
	elif select == 'd':
		run()

	# Ends the program
	elif select == 'q':
		finished = 1