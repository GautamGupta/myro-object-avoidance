from myro import *
init("/dev/tty.Fluke2-052F-Fluke2")

forward(1)                              #forward till it sees obstacle
done = 0

while done == 0:
    if getObstacle("center") > 4500:
        done = 1

turnLeft(1)                             #turns till it sees a clear path
done = 0

while done == 0:
    if getObstacle("center") < 5:
        done = 1

turnLeft(1, 0.2)                        #turns a wee bit extra
forward(1)                              #goes forward till clear path on right
done = 0

while done == 0:
    if getObstacle("right") < 5:
        done = 1

forward(1, 1.8)                         #forward a wee bit extra
turnRight(1, 1.1)                       #90 degree right turn
forward(1)                              #goes forward till clear path on right
done = 0

while done == 0:
    if getObstacle("right") < 5:
        done = 1

forward(1, 1.8)                         #forward a wee bit extra
turnRight(1, 1.1)                       #90 degree right turn
forward(1, 3)                           #forward back to middle of boxish
turnLeft(1, 1.1)                        #90 degree left turn
forward(1, 3)                           #hey look im back on the path
