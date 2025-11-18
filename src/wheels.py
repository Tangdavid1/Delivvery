from utils.brick import Motor, TouchSensor
import time
import math

class Wheels:
    # Initializer
    def __init__(self, left_wheel_port="B", right_wheel_port="C"):
        # Initialize motors
        self.RIGHT_MOTOR = Motor(right_wheel_port)
        self.LEFT_MOTOR = Motor(left_wheel_port)
        # Constant values
        self.WHEEL_DIAMETER_CM = 4.3
        self.WHEEL_RADIUS_CM = self.WHEEL_DIAMETER_CM/2
        self.AXLE_LENGTH_CM = 7.5
        # More constants regarding motors
        self.ORIENT_TO_DEG = self.AXLE_LENGTH_CM/self.WHEEL_RADIUS_CM
        self.DISTANCE_TO_DEG = 360/(math.pi*self.WHEEL_DIAMETER_CM)
        self.POWER_LIMIT = 80
        self.SPEED_LIMIT = 720
        self.FWD_SPEED = 100
        self.MOTOR_POLL_DELAY = 0.05
        # Constants for accurate movement
        self.DEG_180_TURN = 200

        try:
            self.RIGHT_MOTOR.reset_encoder()
            self.RIGHT_MOTOR.set_limits(self.POWER_LIMIT, self.SPEED_LIMIT)
            self.RIGHT_MOTOR.set_power(0)

            self.LEFT_MOTOR.reset_encoder()
            self.LEFT_MOTOR.set_limits(self.POWER_LIMIT, self.SPEED_LIMIT)
            self.LEFT_MOTOR.set_power(0)
        except IOError as error:
            print(error)
    
    # Method that waits for motor to complete their movement
    def wait_for_motor(self, motor: Motor):
        while math.isclose(motor.get_speed(), 0):
            time.sleep(self.MOTOR_POLL_DELAY)
        while not math.isclose(motor.get_speed(), 0):
            time.sleep(self.MOTOR_POLL_DELAY)
    

    def go_straight(self, distance_cm):
        deg_to_move = int(distance_cm*self.DISTANCE_TO_DEG)
        try:
            self.LEFT_MOTOR.set_position_relative(deg_to_move)
            self.RIGHT_MOTOR.set_position_relative(deg_to_move)
            self.wait_for_motor(self.RIGHT_MOTOR)
        except IOError as error:
            print(error)


    def turn_180(self, right_left_not: bool):
        if right_left_not:
            deg_to_move = int(self.DEG_180_TURN*self.ORIENT_TO_DEG)
        else:
            deg_to_move = int(-self.DEG_180_TURN*self.ORIENT_TO_DEG)

        try:
            self.LEFT_MOTOR.set_position_relative(deg_to_move)
            self.RIGHT_MOTOR.set_position_relative(-deg_to_move)
            self.wait_for_motor(self.RIGHT_MOTOR)
        except IOError as error:
            print(error)

    def turn_90_left(self):
        deg_to_move = int(self.DEG_180_TURN*self.ORIENT_TO_DEG)

        try:
            self.RIGHT_MOTOR.set_position_relative(deg_to_move)
            self.wait_for_motor(self.RIGHT_MOTOR)
        except IOError as error:
            print(error)


    def turn_90_right(self):
        deg_to_move = int(self.DEG_180_TURN*self.ORIENT_TO_DEG)

        try:
            self.LEFT_MOTOR.set_position_relative(deg_to_move)
            self.wait_for_motor(self.LEFT_MOTOR)
        except IOError as error:
            print(error)


    #Turn angle method. pass an angle and direction to turn
    def turn_angle(self, angle_deg: int, direction: str):
        deg_to_move = int(angle_deg*self.ORIENT_TO_DEG)

        try:
            if direction == "left":
                self.RIGHT_MOTOR.set_position_relative(deg_to_move)
                self.wait_for_motor(self.RIGHT_MOTOR)

            elif direction == "right":
                self.LEFT_MOTOR.set_position_relative(deg_to_move)
                self.wait_for_motor(self.LEFT_MOTOR)
        except IOError as error:
            print(error)


if __name__ == "__main__":
    #Testing movement
    wheels = Wheels("B", "C")
    wheels.turn_90_left()
    wheels.turn_90_left()
    wheels.turn_90_right()
    wheels.turn_90_right()
    wheels.turn_180(True)
    wheels.turn_180(False)
