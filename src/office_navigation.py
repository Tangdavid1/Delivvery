from utils.brick import Motor, EV3ColorSensor

import wheels as wh
import office_scanningV2 as os
import color_average_finder
import color_detect
import time 
import math

## Constants to define: 92(23 * 3), 23, 69 (23*3), 46 (23*2), 5
BLOCK_CM = 23
OFFICE_ENTRANCE_DISTANCE_CM = 5

#Counters
office_entered = 0

class NavigationSystem:
    def __init__(self, left_motor_port="B", right_motor_port="C", color_sensor_port=1):
        self.left_motor = Motor(left_motor_port)
        self.right_motor = Motor(right_motor_port)
        self.color_sensor = EV3ColorSensor(color_sensor_port)

    def enter_office(self):
        """
        Perform a 90-degree turn at a corner, and advance to the entrance of an office.
        """
        wh.turn_90_right(self)
        wh.move_straight(OFFICE_ENTRANCE_DISTANCE_CM)

    def exit_office(self):
        """
        Exit the office by reversing the entrance process.
        """
        wh.turn_90_left(self)

    
    def go_to_first_office(self):
        """
        Navigate to first office on the board (lower left office).
        """
        office_entered += 1

        # Move forward towards the corner
        wh.go_straight(BLOCK_CM * 4)

        # Turn the corner and advance towards the entrance
        wh.turn_90_right(self)

        wh.go_straight(BLOCK_CM)

        self.enter_office()

        # Detect color to confirm arrival at office, for debugging
        detected_color = color_detect.detect_color(self.color_sensor)
        print(f"Arrived at office with color: {detected_color}")

        self.scanOffice(Motor)  

        self.exit_office()

       
    def go_to_office2(self):

        '''
        Navigate to second office on the board.
        '''
        office_entered += 1
        
        wh.go_straight(BLOCK_CM * 3)

        wh.turn_90_right(self)

        wh.go_straight(BLOCK_CM)

        wh.enter_office(self)

        self.scanOffice(Motor)

        if (self.count == 2) :
            self.return_to_mailroom_from_office2()
        else:
            self.exit_office()    

    def go_to_office3(self):
        '''
        Navigate to third office on the board.
        '''
        office_entered += 1

        wh.go_straight(BLOCK_CM * 3)

        wh.turn_90_right(self)

        wh.go_straight(BLOCK_CM)

        wh.enter_office(self)

        self.scanOffice(Motor)

        if (self.count == 2) :
            self.return_to_mailroom_from_office3()
        
        self.exit_office()
        

    def go_to_office4(self):
        '''
        Navigate to fourth office on the board.
        '''
        office_entered += 1

        wh.go_straight(BLOCK_CM * 2)
      
        wh.enter_office(self)

        self.scanOffice(Motor)

        self.return_to_mailroom_from_office4()

    def return_to_mailroom_from_office2(self):
        '''
        Return to mailroom after delivering at office 2.
        '''
        wh.turn_90_right(self)

        wh.go_straight(BLOCK_CM)

        wh.turn_90_left(self)

        wh.go_straight(BLOCK_CM * 2)

        wh.turn_90_left(self)

        wh.go_straight(BLOCK_CM * 2)

    def return_to_mailroom_from_office3(self):
        '''
        Return to mailroom after delivering at office 3.
        '''

        wh.go_straight(BLOCK_CM)

        wh.turn_90_right(self)

        wh.go_straight(BLOCK_CM * 2)

    def return_to_mailroom_from_office4(self):
        '''
        Return to mailroom after delivering at office 4.
        '''
        wh.turn_90_right(self)

        wh.go_straight(BLOCK_CM)
        
        wh.turn_90_left(self)

        wh.go_straight(BLOCK_CM * 2)



        

        
        