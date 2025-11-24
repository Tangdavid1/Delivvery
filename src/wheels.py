from utils.brick import Motor, EV3ColorSensor
import time
import math
import color_utils.color_detect as color_detect

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
        self.DEG_180_TURN = 195
        self.DEG_90_TURN = 180

        try:
            self.RIGHT_MOTOR.reset_encoder()
            self.RIGHT_MOTOR.set_limits(self.POWER_LIMIT, self.SPEED_LIMIT)
            self.RIGHT_MOTOR.set_power(0)

            self.LEFT_MOTOR.reset_encoder()
            self.LEFT_MOTOR.set_limits(self.POWER_LIMIT, self.SPEED_LIMIT)
            self.LEFT_MOTOR.set_power(0)
        except IOError as error:
            print(error)
    
    
    def wait_for_motor(self, motor: Motor):
        """
        Waits for the given motor to complete its movement.
        """
        while math.isclose(motor.get_speed(), 0):
            time.sleep(self.MOTOR_POLL_DELAY)
        while not math.isclose(motor.get_speed(), 0):
            time.sleep(self.MOTOR_POLL_DELAY)
    

    def wait_for_motor_while_check_color(self, motor: Motor, color: str, color_sensor: EV3ColorSensor) -> bool:
        """
        Waits for the given motor to complete its movement, unless the color sensor detects the
        color we are looking for.
        """
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
        """
        Makes the robot go straight a certain distance. Both wheels move forward.
        """
        deg_to_move = int(distance_cm*self.DISTANCE_TO_DEG)
        try:
            self.LEFT_MOTOR.set_position_relative(deg_to_move)
            self.RIGHT_MOTOR.set_position_relative(deg_to_move)
            self.wait_for_motor(self.RIGHT_MOTOR)
        except IOError as error:
            print(error)


    def turn_180(self, right_left_not: bool):
        """
        Makes the robot turn 180°. If the second parameter is True, the robots turns clockwise. If
        False, the robot turns counter clockwise.
        """
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
        """
        Turns the robot 90 degrees to the left going forward. Only the right motor moves.
        """
        deg_to_move = int(self.DEG_180_TURN*self.ORIENT_TO_DEG)

        try:
            self.RIGHT_MOTOR.set_position_relative(deg_to_move)
            self.wait_for_motor(self.RIGHT_MOTOR)
        except IOError as error:
            print(error)


    def turn_90_right(self):
        """
        Turns the robot 90 degrees to the right going forward. Only the left motor moves.
        """
        deg_to_move = int(self.DEG_180_TURN*self.ORIENT_TO_DEG)

        try:
            self.LEFT_MOTOR.set_position_relative(deg_to_move)
            self.wait_for_motor(self.LEFT_MOTOR)
        except IOError as error:
            print(error)


    def turn_90_left_back(self):
        """
        Turns the robot 90 degrees to the left going backwards. Only the left motor moves.
        """
        deg_to_move = int(-self.DEG_90_TURN*self.ORIENT_TO_DEG)

        try:
            self.LEFT_MOTOR.set_position_relative(deg_to_move)
            self.wait_for_motor(self.LEFT_MOTOR)
        except IOError as error:
            print(error)


    def turn_90_right_back(self):
        """
        Turns the robot 90 degrees to the right going backwards. Only the right motor moves.
        """
        deg_to_move = int(-self.DEG_90_TURN*self.ORIENT_TO_DEG)

        try:
            self.RIGHT_MOTOR.set_position_relative(deg_to_move)
            self.wait_for_motor(self.RIGHT_MOTOR)
        except IOError as error:
            print(error)

         
    def turn_angle(self, angle_deg: int, direction: str):
        """
        Turns the robot a certain angle. Given the direction, can either be to the left or to the right.
        """
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

    
    def turn_angle_and_check_color(self, angle_deg: int, direction: str, color, sensor) -> tuple[bool, int]:
        """
        Turns the robot a certain angle, while checking a certain color. If it detects said color, it returns
        True as well as the difference in movement it managed to do before detecting the color
        """
        deg_to_move = int(angle_deg*self.ORIENT_TO_DEG)

        try:
            if direction == "left":
                pos_before = self.RIGHT_MOTOR.get_encoder()
                self.RIGHT_MOTOR.set_position_relative(deg_to_move)
                found_color = self.wait_for_motor_while_check_color(self.RIGHT_MOTOR, color, sensor)
                pos_after = self.RIGHT_MOTOR.get_encoder()
                difference = int(pos_after - pos_before)

            elif direction == "right":
                pos_before = self.LEFT_MOTOR.get_encoder()
                self.LEFT_MOTOR.set_position_relative(deg_to_move)
                found_color = self.wait_for_motor_while_check_color(self.LEFT_MOTOR, color, sensor)
                pos_after = self.LEFT_MOTOR.get_encoder()
                difference = int(pos_after - pos_before)
            
            if found_color:
                print(f"Found {color}!")
                return (True, difference)
            
            return (False, 0)
        except IOError as error:
            print(error)
    
    
    def reverse_previous_position(self, direction: str, difference: int):
        if direction == "left":
            self.RIGHT_MOTOR.set_position_relative(-difference)
            self.wait_for_motor(self.RIGHT_MOTOR)
        elif direction == "right":
            self.LEFT_MOTOR.set_position_relative(-difference)
            self.wait_for_motor(self.LEFT_MOTOR)
            

if __name__ == "__main__":
    #Testing movement
    wheels = Wheels("B", "C")
    wheels.turn_90_left_back()
    wheels.turn_90_left_back()
    wheels.turn_90_right_back()
    wheels.turn_90_right_back()
    wheels.turn_180(True)
    wheels.turn_180(False)
    wheels.turn_90_left()
    wheels.turn_90_right()
    

    #Testing moving and scanning
    
