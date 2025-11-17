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

def wait_for_motor(motor: Motor):
    while math.isclose(motor.get_speed(), 0):
        time.sleep(MOTOR_POLL_DELAY)
    while not math.isclose(motor.get_speed(), 0):
        time.sleep(MOTOR_POLL_DELAY)


def init_motor(motor: Motor):
    try:
        motor.reset_encoder()
        motor.set_limits(POWER_LIMIT, SPEED_LIMIT)
        motor.set_power(0)
    except IOError as error:
        print(error)


def go_forward_single(motor: Motor, distance_cm: int):
    #calculate distance to move in degrees
    deg_to_move = int(distance_cm*DISTANCE_TO_DEG)
    # move forward
    try:
        motor.set_position_relative(deg_to_move)
    except IOError as error:
        print(error)

def go_forward_both_wheels(left_motor: Motor, right_motor: Motor, distance_cm: int):
    try:
        go_forward_single(left_motor, distance_cm)
        go_forward_single(right_motor, distance_cm)
        wait_for_motor(right_motor)
    except IOError as error:
        print(error)


def turn_180(left_motor: Motor, right_motor: Motor):
    deg_to_move = int(207*ORIENT_TO_DEG)

    try:
        left_motor.set_position_relative(deg_to_move)
        right_motor.set_position_relative(-deg_to_move)
        wait_for_motor(right_motor)
    except IOError as error:
        print(error)

def turn_90_left(left_motor: Motor, right_motor: Motor):
    deg_to_move = int(200*ORIENT_TO_DEG)

    try:
        right_motor.set_position_relative(deg_to_move)
        wait_for_motor(right_motor)
    except IOError as error:
        print(error)


        
def turn_90_right(left_motor: Motor, right_motor: Motor):
    deg_to_move = int(200*ORIENT_TO_DEG)

    try:
        left_motor.set_position_relative(deg_to_move)
        wait_for_motor(left_motor)
    except IOError as error:
        print(error)


#Turn angle method. pass an angle and direction to turn

def turn_angle(left_motor: Motor, right_motor: Motor, angle_deg: int, direction: str):
    deg_to_move = int(angle_deg*ORIENT_TO_DEG)

    try:
        if direction == "left":
            right_motor.set_position_relative(deg_to_move)
            wait_for_motor(right_motor)

        elif direction == "right":
            left_motor.set_position_relative(deg_to_move)
            wait_for_motor(left_motor)
    except IOError as error:
        print(error)

if __name__ == "__main__":
    try:
        print("movement test.")
        init_motor(LEFT_MOTOR)
        init_motor(RIGHT_MOTOR)
        init_motor(CONVEYOR)
#        go_forward_single(CONVEYOR, 25)
 #       wait_for_motor(CONVEYOR)

        #print("try to move forward")
        go_forward_both_wheels(LEFT_MOTOR, RIGHT_MOTOR, 50)

        #print("try to rotate 180")
        #turn_180(LEFT_MOTOR, RIGHT_MOTOR)

        #print("try to rotate 90 left")
        #turn_90_left(LEFT_MOTOR, RIGHT_MOTOR)

        print("try to rotate 90 right")
        turn_90_right(LEFT_MOTOR, RIGHT_MOTOR)
        go_forward_both_wheels(LEFT_MOTOR, RIGHT_MOTOR, 80)
        turn_90_right(LEFT_MOTOR, RIGHT_MOTOR)
        go_forward_both_wheels(LEFT_MOTOR, RIGHT_MOTOR, 20)
        turn_90_right(LEFT_MOTOR, RIGHT_MOTOR)
        go_forward_both_wheels(LEFT_MOTOR, RIGHT_MOTOR, 10)
        turn_90_right(LEFT_MOTOR, RIGHT_MOTOR)
        go_forward_both_wheels(LEFT_MOTOR, RIGHT_MOTOR, 80)
        turn_90_right(LEFT_MOTOR, RIGHT_MOTOR)

    except KeyboardInterrupt:
        print("Ended program")
   
