# Program for Myro Scribbler Bot Object Avoidance
# -----------------------------------------------
# Authors:
# 
# Pranav Anand
# Olivia Cao
# Gautam Gupta
# Nakul Pathak
# Ross Semenov
# Wojciech Swiderski
# Jason Zukewich

from myro import *
from time import time

init("/dev/tty.Fluke2-052F-Fluke2")

# Robot class
class Gautmobile:

	# Setting parameter variables
	motorPower = 0.5
	leftTime = 0.64
	rightTime = 0.66
	forwardTime = 0.5
	distanceUpper = 2500
	distanceUpperFirst = 2500
	distanceLower = 5

	# Logic Variables
	done = 0
	counter = 0
	beginTime = 0
	turntime = 0
	iterations = 0

	# Move forward for set forwardTime
	def bitForward(self, times = 1):
		forward(self.motorPower, times * self.forwardTime)

	# 90 degree left turn
	def leftRight(self):
		self.turnLeftAngle(90)

	# 90 degree right turn
 	def rightRight(self):
		self.turnRightAngle(90)

	# Functions to calculate how long it took to turn at the beginning
	def startTime(self):
		self.beginTime = time()

	def endTime(self):
		self.turnTime = time() - self.beginTime
		return self.turnTime

	# Check for wall on right of robot
	def checkRight(self):
		value = False
		self.turnRightAngle(90)
		if getObstacle("center") > self.distanceUpper:
			value = True
		self.turnLeftAngle(90)
		return value

	# Turns for a set angle in degrees
	def turnRightAngle(self, angle):
		turnRight(self.motorPower, self.rightTime / 90 * angle)

	def turnLeftAngle(self, angle):
		turnLeft(self.motorPower, self.leftTime / 90 * angle)

	# Delaying functions
	def delayForward(self):
		while self.done == 0:
			if getObstacle("center") > self.distanceUpperFirst:
				self.done = 1
		self.done = 0

	def delayLeft(self):
		while self.done == 0:
			if getObstacle("right") < self.distanceLower:
				self.done = 1
		self.done = 0

# -------------------- Start of Run Sequence ----------------------

# Main function that runs the sequence for the robot
def run(power = 1, left = 0.647, right = 0.658, forwards = 0.6, upper = 2000, lower = 5, upperFirst = 2000):

	# Initialize
	robot = Gautmobile()

	robot.motorPower = power
	robot.leftTime = left
	robot.rightTime = right
	robot.forwardTime = forwards
	robot.distanceUpper = upper
	robot.distanceUpperFirst = upperFirst
	robot.distanceLower = lower

	# Drive forward until detects wall
	forward(robot.motorPower)
	robot.delayForward()

	# Turn left until no longer detects wall
	# Check times it takes to turn parallel to wall
	turnLeft(robot.motorPower)
	robot.startTime()
	robot.delayLeft()
	print "Time of turn: {}".format(robot.endTime())

	# Extra turn for angled
	if robot.motorPower != 1:
		turnLeft(robot.motorPower, 0.25)

	# Each counter represents turning around the corner of the box
	while robot.counter < 2:
		robot.bitForward()
		if robot.counter == 0:
			robot.iterations += 1
		if not robot.checkRight():
			robot.counter = robot.counter + 1
			robot.bitForward(2.7)
			robot.rightRight()
			robot.bitForward(2)

	robot.bitForward(robot.iterations)
	turnLeft(robot.motorPower, 2 * robot.leftTime - (robot.turnTime + 0.15 / robot.motorPower))
	robot.bitForward(4)
	# Turn back to correct angle

# -------------------- End of Run Sequence ----------------------

# User Control
finished = 0

while finished == 0:
	select = raw_input("Enter 'a' to select angled\nEnter 'r' to select right angle\nEnter 'q' to quit program\n")

	# Mode for third part
	if select == 'a':
		run(0.5, 1.2, 1.18, 0.5, 5500, 5, 5500)

	# Mode for first two parts
	elif select == 'r':
		run(0.5, 1.2, 1.18, 0.5, 5500, 5, 500)

	# Ends the program
	elif select == 'q':
		finished = 1
