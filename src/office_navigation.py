from utils.brick import Motor, EV3ColorSensor

from wheels import Wheels
import office_scanningV2 as os
import color_detect
import time 
import math

## Constants to define: 92(23 * 3), 23, 69 (23*3), 46 (23*2), 5
BLOCK_CM = 15
OFFICE_ENTRANCE_DISTANCE_CM = 2

#Counters


class NavigationSystem:
    def __init__(self, left_motor_port="B", right_motor_port="C", color_sensor_port=2):
        self.wh = Wheels("B", "C")
        self.color_sensor = EV3ColorSensor(color_sensor_port)
        self.office_entered = 0

    def enter_office(self):
        """
        Perform a 90-degree turn at a corner, and advance to the entrance of an office.
        """
        self.wh.turn_90_right()
        self.wh.go_straight(OFFICE_ENTRANCE_DISTANCE_CM)

    def exit_office(self):
        """
        Exit the office by reversing the entrance process.
        """
        self.wh.turn_90_left() #TODO CHANGE BY TURN LEFT IN REVERSE

    
    def go_to_first_office(self):
        """
        Navigate to first office on the board (lower left office).
        """
        self.office_entered += 1

        # Move forward towards the corner
        self.wh.go_straight(BLOCK_CM * 4)

        # Turn the corner and advance towards the entrance
        self.wh.turn_90_right()

        self.wh.go_straight(12)

        self.enter_office()

        # Detect color to confirm arrival at office, for debugging
        #detected_color = color_detect.detect_color(self.color_sensor)
        #print(f"Arrived at office with color: {detected_color}")

        os.scanOffice(self.wh, self.color_sensor)

        self.exit_office()

       
    def go_to_office2(self):

        '''
        Navigate to second office on the board.
        '''
        self.office_entered += 1
        
        self.wh.go_straight(BLOCK_CM * 3)

        self.wh.turn_90_right()

        self.wh.go_straight(BLOCK_CM)

        self.enter_office()

        os.scanOffice(self.wh, self.color_sensor)

        if (self.count == 2) :
            self.return_to_mailroom_from_office2()
        else:
            self.exit_office()    

    def go_to_office3(self):
        '''
        Navigate to third office on the board.
        '''
        self.office_entered += 1

        self.wh.go_straight(BLOCK_CM * 3)

        self.wh.turn_90_right()

        self.wh.go_straight(BLOCK_CM)

        self.enter_office()

        os.scanOffice(self.wh, self.color_sensor)

        if (self.count == 2) :
            self.return_to_mailroom_from_office3()
        
        self.exit_office()
        

    def go_to_office4(self):
        '''
        Navigate to fourth office on the board.
        '''
        self.office_entered += 1

        self.wh.go_straight(BLOCK_CM * 2)
      
        self.enter_office()

        os.scanOffice(self.wh, self.color_sensor)

        self.return_to_mailroom_from_office4()

    def return_to_mailroom_from_office2(self):
        '''
        Return to mailroom after delivering at office 2.
        '''
        self.wh.turn_90_right() #TODO CHANGE TO TURN BACK RIGHT

        self.wh.go_straight(BLOCK_CM)

        self.wh.turn_90_left()

        self.wh.go_straight(BLOCK_CM * 2)

        self.wh.turn_90_left()

        self.wh.go_straight(BLOCK_CM * 2)

    def return_to_mailroom_from_office3(self):
        '''
        Return to mailroom after delivering at office 3.
        '''

        self.wh.go_straight(BLOCK_CM)

        self.wh.turn_90_right()

        self.wh.go_straight(BLOCK_CM * 2)

    def return_to_mailroom_from_office4(self):
        '''
        Return to mailroom after delivering at office 4.
        '''
        self.wh.turn_90_right()

        self.wh.go_straight(BLOCK_CM)
        
        self.wh.turn_90_left()

        self.wh.go_straight(BLOCK_CM * 2)

if __name__ == "__main__":
    nav = NavigationSystem("B", "C", 2)
    nav.go_to_first_office()
