from utils.brick import Motor, EV3ColorSensor

import movement as mv
import office_scanning as os
import color_average_finder
import color_detect
import time 
import math

## Constants
FORWARD_DISTANCE_CM = 120
CORNER_DISTANCE_CM = 23

class NavigationSystem:
    def __init__(self, left_motor_port="B", right_motor_port="C", color_sensor_port=1):
        self.left_motor = Motor(left_motor_port)
        self.right_motor = Motor(right_motor_port)
        self.color_sensor = EV3ColorSensor(color_sensor_port)

    def navigate_to_ll_office(self):
        """
        Navigate to first office on the board (lower left office).
        """
        # Move forward towards the corner
        mv.move_straight(FORWARD_DISTANCE_CM, self.left_motor, self.right_motor)

        # Turn at the corner
        mv.turn_angle(90, self.left_motor, self.right_motor)

        # Move towards the office
        mv.move_straight(CORNER_DISTANCE_CM, self.left_motor, self.right_motor)

        # Turn at the office entrance corner
        mv.turn_angle(90, self.left_motor, self.right_motor)

        # Move into the office
        #### WAIT BUT IS IT 23 CM ALSO TO GET INTO THE OFFICE
        mv.move_straight(CORNER_DISTANCE_CM, self.left_motor, self.right_motor)

        # Detect color to confirm arrival at office, for debugging
        detected_color = color_detect.detect_color(self.color_sensor)
        print(f"Arrived at office with color: {detected_color}")

    def move_out_of_office(self):
        """
        Move out of the office to the hallway, assuming the robot is set to some reset position 
        """
        # Reset any orientation changes made inside the office, so that the robot faces the exit facing forward
        os.reset_positon()
        
        # Move back from the office (move 23 cm backwards from entrance)
        mv.move_straight(-CORNER_DISTANCE_CM, self.left_motor, self.right_motor)

        # Turn at the corner
        mv.turn_angle(90, self.left_motor, self.right_motor)

        # After turn, advance to next office, before turning the next corner
        mv.move_straight(FORWARD_DISTANCE_CM - CORNER_DISTANCE_CM, self.left_motor, self.right_motor)

        # Turn towards the hallway
        mv.turn_angle(90, self.left_motor, self.right_motor)

    def navigate_to_next_office(self):
        '''
        Navigate to the next office on the upper right side.
        '''
        mv.move_straight(CORNER_DISTANCE_CM, self.left_motor, self.right_motor)

        mv.turn_angle(90, self.left_motor, self.right_motor)

        mv.move_straight(CORNER_DISTANCE_CM, self.left_motor, self.right_motor)

        # Turn towards the mailroom
        mv.turn_angle(-90, self.left_motor, self.right_motor)


    
    def return_to_mailroom(self):
        """
        Navigate back to mailroom from office.
        """
        # Move back from the office
        mv.move_straight(-CORNER_DISTANCE_CM, self.left_motor, self.right_motor)

        # Turn back at the corner
        mv.turn_angle(-90, self.left_motor, self.right_motor)

        # Move back to mailroom
        mv.move_straight(-FORWARD_DISTANCE_CM, self.left_motor, self.right_motor)
