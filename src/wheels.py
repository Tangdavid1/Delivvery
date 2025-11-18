from utils.brick import Motor, TouchSensor
import time
import math

class Wheels:
    # Initializer
    def __init__(self, left_wheel_port, right_wheel_port):
        # Initialize motors
        self.RIGHT_MOTOR = Motor("C")
        self.LEFT_MOTOR = Motor("B")
        # Constant values
        self.WHEEL_DIAMETER_CM = 4.3
        self.WHEEL_RADIUS_CM = self.WHEEL_DIAMETER_CM/2
        self.AXLE_LENGTH_CM = 7.5
        # More constants regarding motors
        self.ORIENT_TO_DEG = self.AXLE_LENGTH_CM/self.WHEEL_RADIUS_CM
        self.DISTANCE_TO_DEG = 360/(math.pi*self.WHEEL_DIAMETER_CM)
        self.POWER_LIMIT = 100
        self.SPEED_LIMIT = 720
        self.FWD_SPEED = 100
        self.MOTOR_POLL_DELAY = 0.05
    
    # Method that waits for motor to complete their movement
    def wait_for_motor(self, motor: Motor):
        while math.isclose(motor.get_speed(), 0):
            time.sleep(self.MOTOR_POLL_DELAY)
        while not math.isclose(motor.get_speed(), 0):
            time.sleep(self.MOTOR_POLL_DELAY)
    
    # Method that initializes a motor by setting correct limits
    def init_motor(self, motor: Motor):
        try:
            motor.reset_encoder()
            motor.set_limits(self.POWER_LIMIT, self.SPEED_LIMIT)
            motor.set_power(0)
        except IOError as error:
            print(error)
    
    def go_forward_single(self, motor: Motor, distance_cm: int):
        #calculate distance to move in degrees
        deg_to_move = int(distance_cm*DISTANCE_TO_DEG)
        # move forward
        try:
            motor.set_position_relative(deg_to_move)
        except IOError as error:
            print(error)

    def go_forward_both_wheels(self, left_motor: Motor, right_motor: Motor, distance_cm: int):
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

    
