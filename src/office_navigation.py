from utils.brick import Motor, EV3ColorSensor, wait_ready_sensors

from wheels import Wheels
from delivery import DeliverySystem
import office_scanning as os

## Constants to define: 92(23 * 3), 23, 69 (23*3), 46 (23*2), 5
BLOCK_CM = 22
OFFICE_ENTRANCE_DISTANCE_CM = 2

#Counters

class NavigationSystem:
    def __init__(self, wheels: Wheels, delivery: DeliverySystem, color_sensor: EV3ColorSensor):
        self.wh = wheels
        self.color_sensor = color_sensor
        self.office_entered = 0
        self.delivery = delivery
        self.count = 0
        # MOVEMENT CONSTANTS
        self.D1 = 90
        self.D2 = 77
        self.CORNER_TO_ENTRANCE = 10
        self.D3 = 44

    def enter_office(self):
        """
        Perform a 90-degree turn at a corner, and advance to the entrance of an office.
        """
        self.wh.turn_90_right()

    def exit_office(self):
        """
        Exit the office by reversing the entrance process.
        """
        self.wh.turn_90_left_back()

    
    def go_to_first_office(self):
        """
        Navigate to first office on the board (lower left office).
        """
        self.office_entered += 1

        # Move forward towards the corner
        self.wh.go_straight(self.D1)

        # Turn the corner and advance towards the entrance
        self.wh.turn_90_right()

        self.wh.go_straight(self.CORNER_TO_ENTRANCE)

        self.enter_office()

        # Detect color to confirm arrival at office, for debugging
        #detected_color = color_detect.detect_color(self.color_sensor)
        #print(f"Arrived at office with color: {detected_color}")

        self.scan_room()

        self.exit_office()

       
    def go_to_office2(self):

        '''
        Navigate to second office on the board.
        '''
        self.office_entered += 1
        
        self.wh.go_straight(self.D2)

        self.wh.turn_90_right()

        self.wh.go_straight(self.CORNER_TO_ENTRANCE)

        self.enter_office()

        self.scan_room()

        if (self.count == 2) :
            self.return_to_mailroom_from_office2()
        else:
            self.exit_office()    

    def go_to_office3(self):
        '''
        Navigate to third office on the board.
        '''
        self.office_entered += 1

        self.wh.go_straight(self.D2)

        self.wh.turn_90_right()

        self.wh.go_straight(self.CORNER_TO_ENTRANCE)

        self.enter_office()

        self.scan_room()

        if (self.count == 2) :
            self.return_to_mailroom_from_office3()
        
        self.exit_office()
        

    def go_to_office4(self):
        '''
        Navigate to fourth office on the board.
        '''
        self.office_entered += 1

        self.wh.go_straight(self.D3)
      
        self.enter_office()

        self.scan_room()

        self.return_to_mailroom_from_office4()

    def return_to_mailroom_from_office2(self):
        '''
        Return to mailroom after delivering at office 2.
        '''
        self.wh.turn_90_right_back()

        self.wh.go_straight(BLOCK_CM)

        self.wh.turn_90_left()

        self.wh.go_straight((BLOCK_CM * 2)-5)

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
        self.wh.turn_90_right_back()

        self.wh.go_straight(BLOCK_CM)
        
        self.wh.turn_90_left()

        self.wh.go_straight(BLOCK_CM * 2)

    def scan_room(self):
        result = os.scanOffice(self.wh, self.color_sensor)
        if result[0] > 0: #when green detected
            self.wh.go_straight(-7)
            self.wh.turn_180(True)
            self.delivery.drop_package()
            self.wh.turn_180(False)
            self.wh.go_straight(7)
            self.wh.reverse_previous_position(result[1], result[2])
            self.wh.go_straight(-result[0])

if __name__ == "__main__":
    wheels = Wheels("B", "C")
    delivery = DeliverySystem("D")
    color_sensor = EV3ColorSensor(2)
    wait_ready_sensors()

    nav = NavigationSystem(wheels, delivery, color_sensor)
    nav.go_to_first_office()
        
