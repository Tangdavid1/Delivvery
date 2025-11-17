import color_detect as color
import movement as mv
from utils.brick import Motor, TouchSensor
import time
import math


TOUCH_SENSOR = TouchSensor(2)
RIGHT_MOTOR = Motor("C")
LEFT_MOTOR = Motor("B")
CONVEYOR = Motor("D")

WHEEL_DIAMETER_CM = 4.3
WHEEL_RADIUS_CM = WHEEL_DIAMETER_CM/2
AXLE_LENGTH_CM = 7.5
ORIENT_TO_DEG = AXLE_LENGTH_CM/WHEEL_RADIUS_CM
DISTANCE_TO_DEG = 360/(math.pi*WHEEL_DIAMETER_CM)

POWER_LIMIT = 100
SPEED_LIMIT = 720
FWD_SPEED = 100
MOTOR_POLL_DELAY = 0.05


try:
    print("movement test.")
    mv.init_motor(LEFT_MOTOR)
    mv.init_motor(RIGHT_MOTOR)
    mv.init_motor(CONVEYOR)
#        go_forward_single(CONVEYOR, 25)
#       wait_for_motor(CONVEYOR)

    #print("try to move forward")
    mv.go_forward_both_wheels(LEFT_MOTOR, RIGHT_MOTOR, 50)

    #print("try to rotate 180")
    #turn_180(LEFT_MOTOR, RIGHT_MOTOR)

    #print("try to rotate 90 left")
    #turn_90_left(LEFT_MOTOR, RIGHT_MOTOR)

    print("try to rotate 90 right")
    mv.turn_90_right(LEFT_MOTOR, RIGHT_MOTOR)
    mv.go_forward_both_wheels(LEFT_MOTOR, RIGHT_MOTOR, 80)
    mv.turn_90_right(LEFT_MOTOR, RIGHT_MOTOR)
    mv.go_forward_both_wheels(LEFT_MOTOR, RIGHT_MOTOR, 20)
    mv.turn_90_right(LEFT_MOTOR, RIGHT_MOTOR)
    mv.go_forward_both_wheels(LEFT_MOTOR, RIGHT_MOTOR, 10)
    mv.turn_90_right(LEFT_MOTOR, RIGHT_MOTOR)
    mv.go_forward_both_wheels(LEFT_MOTOR, RIGHT_MOTOR, 80)
    mv.turn_90_right(LEFT_MOTOR, RIGHT_MOTOR)

except KeyboardInterrupt:
    print("Ended program")

