from utils.brick import Motor, EV3ColorSensor
import time
import math
import color_detect

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
        self.SPEED_LIMIT = 600
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
    
    def wait_for_motor_while_check_color(self, motor: Motor, color: str, color_sensor: EV3ColorSensor) -> bool:
        while math.isclose(motor.get_speed(), 0):
            time.sleep(self.MOTOR_POLL_DELAY)
        while not math.isclose(motor.get_speed(), 0):
            rgb = color_sensor.get_rgb()
            while(rgb[0]==None or rgb[1]==None or rgb[2]==None):
                rgb = color_sensor.get_rgb()
            scanned_color = color_detect.computeDistance(rgb)
            if scanned_color == color:
                return True
            time.sleep(self.MOTOR_POLL_DELAY)
        return False
            

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
    def turn_angle_and_check_color(self, angle_deg: int, direction: str, color, sensor) -> bool:
        deg_to_move = int(angle_deg*self.ORIENT_TO_DEG)

        try:
            if direction == "left":
                self.RIGHT_MOTOR.set_position_relative(deg_to_move)
                found_color = self.wait_for_motor_while_check_color(self.RIGHT_MOTOR, color, sensor)

            elif direction == "right":
                self.LEFT_MOTOR.set_position_relative(deg_to_move)
                found_color = self.wait_for_motor_while_check_color(self.LEFT_MOTOR, color, sensor)
            
            if found_color:
                print(f"Found {color}!")
                return True
            
            return False
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

    #Testing moving and scanning
    
