from myro import *
init("/dev/tty.Fluke2-052F-Fluke2")
forward(1)
done = 0

while done == 0:
	if getObstacle("center") > 4500:
		turnLeft(1, 0.87)
		forward(1, 2.1)
		turnRight(1, 0.95)
		forward(1, 4.8)
		turnRight(1, 0.95)
		forward(1, 2.1)
		turnLeft(1, 0.93)
		forward(1, 2)
		done = 1
