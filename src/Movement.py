from utils.brick import Motor, TouchSensor
import time
import math

TOUCH_SENSOR = TouchSensor(2)
RIGHT_MOTOR = Motor("C")
LEFT_MOTOR = Motor("B")
WHEEL_DIAMETER_CM = 4.3

POWER_LIMIT = 80
SPEED_LIMIT = 720
FWD_SPEED = 100

def init_motor(motor: Motor):
    try:
        motor.reset_encoder()
        motor.set_limits(POWER_LIMIT, SPEED_LIMIT)
        motor.set_power(0)
    except IOError as error:
        print(error)


def go_forward(distance_cm, speed):
    #calculate distance to move in degrees
    deg_to_move = int(distance_cm*(360/(math.pi*WHEEL_DIAMETER_CM)))
    # move forward
    try:
        LEFT_MOTOR.set_dps(speed)
        RIGHT_MOTOR.set_dps(speed)
        LEFT_MOTOR.set_position_relative(deg_to_move)
        RIGHT_MOTOR.set_position_relative(deg_to_move)
    except IOError as error:
        print(error)


#def turn_180():

#def turn_90_left():
    
#def turn_90_right():

if __name__ == "__main__":
    try:
        print("movement test.")
        init_motor(LEFT_MOTOR)
        init_motor(RIGHT_MOTOR)

        print("try to move forward")
        go_forward(10,FWD_SPEED)

    except KeyboardInterrupt:
        print("Ended program")
   
