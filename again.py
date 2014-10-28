from myro import *
init("/dev/tty.Fluke2-052F-Fluke2")

forward(1)
done = 0

while done == 0:
    if getObstacle("center") > 3500:
        done = 1

turnLeft(1)
done = 0

while done == 0:
    if getObstacle("center") < 5:
        done = 1

done = 0
counter = 0

while counter < 2:
	forward(1, 0.5)
	turnRight(1, 0.68)
	if getObstacle("center") < 5:
		counter += 1
		turnLeft(1, 0.64)
		forward(1, 0.5)
		turnRight(1, 0.67)
		forward(1, 0.5)
	else:
		turnLeft(1, 0.65)

forward(1, 2)
turnLeft(1, 0.65)
forward(1, 2)