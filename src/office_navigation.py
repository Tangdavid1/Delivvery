from utils.brick import EV3GyroSensor, Motor, EV3ColorSensor, wait_ready_sensors

from wheels import Wheels
from delivery import DeliverySystem
import office_scanning as os
import time

## Constants to define: 92(23 * 3), 23, 69 (23*3), 46 (23*2), 5
BLOCK_CM = 26
OFFICE_ENTRANCE_DISTANCE_CM = 2

#Counters

class NavigationSystem:
    def __init__(self, wheels: Wheels, delivery: DeliverySystem, color_sensor: EV3ColorSensor, gyro_sensor: EV3GyroSensor):
        self.wh = wheels
        self.color_sensor = color_sensor
        self.delivery = delivery
        self.count = 0
        self.gyro = gyro_sensor
        # MOVEMENT CONSTANTS
        self.D1 = 90
        self.D2 = 77
        self.CORNER_TO_ENTRANCE = 9
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
        time.sleep(1)
        # Move forward towards the corner
        self.wh.go_straight_gyro(self.gyro, 6.6, 0)

        # Turn the corner and advance towards the entrance
        self.wh.turn_90_right()
        time.sleep(1)

        self.wh.adjust_position_gyro(self.gyro, -90)

        time.sleep(1)
        self.wh.go_straight_gyro(self.gyro, 0.7, 90)
        time.sleep(1)
        self.enter_office()        
        time.sleep(1)
        
        self.wh.go_straight(-2)
        self.scan_room()
        time.sleep(1)
        self.wh.go_straight(3)

        self.exit_office()

        time.sleep(1)

        #self.wh.adjust_position_gyro(self.gyro, -90)

        time.sleep(1)

       
    def go_to_office2(self):
        '''
        Navigate to second office on the board.
        '''
        # Poll the gyro to see what it's currently reading
        angle = self.gyro.get_value()[0]
        
        # move straight according to what the gyro is reading
        
        if angle < -90:
            self.wh.go_straight_gyro(self.gyro, 5.5, 92)
        elif angle > -90:
            self.wh.go_straight_gyro(self.gyro, 5.5, 80)
        elif angle == -90:
            self.wh.go_straight_gyro(self.gyro, 5.5, 90)
        
        self.wh.turn_90_right()

        #self.wh.adjust_position_gyro(self.gyro, -180)
        time.sleep(1)
        self.wh.go_straight_gyro(self.gyro, 0.5, 180)
        time.sleep(1)
        self.enter_office()
        
        self.wh.go_straight(-2)

        self.scan_room()
        time.sleep(1)
        self.wh.go_straight(3)

        if (self.delivery.count != 2) :
            self.exit_office()    
            #self.wh.adjust_position_gyro(self.gyro, -180)
        
        time.sleep(1)


    def go_to_office3(self):
        '''
        Navigate to third office on the board.
        '''
        # Poll the gyro to see what it's currently reading
        angle = self.gyro.get_value()[0]
        
        if angle < -180:
            self.wh.go_straight_gyro(self.gyro, 5.5, 186)
        elif angle > -180:
            self.wh.go_straight_gyro(self.gyro, 5.5, 173)
        elif angle == -180:
            self.wh.go_straight_gyro(self.gyro, 5.5, 180)
        
        #self.wh.go_straight_gyro(self.gyro, 5.4, 186)

        self.wh.turn_90_right()

        #self.wh.adjust_position_gyro(self.gyro, -270)
        time.sleep(1)
        self.wh.go_straight_gyro(self.gyro, 0.5, 270)
        time.sleep(1)

        self.enter_office()

        self.wh.go_straight(-2)
        self.scan_room()
        time.sleep(1)
        self.wh.go_straight(3)

        if (self.count == 2) :
            self.return_to_mailroom_from_office3()
        
        self.exit_office()
        #self.wh.adjust_position_gyro(self.gyro, -270)
        time.sleep(1)

    def go_to_office4(self):
        '''
        Navigate to fourth office on the board.
        '''
        # Poll the gyro to see what it's currently reading
        angle = self.gyro.get_value()[0]
        
        if angle < -280:
            self.wh.go_straight_gyro(self.gyro, 3.8, 280)
        elif angle < -270:
            self.wh.go_straight_gyro(self.gyro, 3.8, 273)
        elif angle > -270:
            self.wh.go_straight_gyro(self.gyro, 3.8, 260)
        elif angle == -270:
            self.wh.go_straight_gyro(self.gyro, 3.8, 270)
        
        #self.wh.go_straight_gyro(self.gyro, 3.8, 283)

        self.enter_office()

        self.wh.go_straight(-3)
        self.scan_room()
        self.wh.go_straight(3)

        self.return_to_mailroom_from_office4()


    def return_to_mailroom_from_office2(self):
        '''
        Return to mailroom after delivering at office 2.
        '''
        self.wh.turn_90_right_back()

        self.wh.go_straight(BLOCK_CM)

        self.wh.turn_90_left()

        self.wh.go_straight(30)

        self.wh.turn_90_left()

        #self.wh.go_straight(35)
        self.wh.go_straight_gyro(self.gyro, 3.0, 183)


    def return_to_mailroom_from_office3(self):
        '''
        Return to mailroom after delivering at office 3.
        '''

        self.wh.go_straight(BLOCK_CM)

        self.wh.turn_90_right()

        #self.wh.go_straight(35)
        self.wh.go_straight_gyro(self.gyro, 3.0, 360)


    def return_to_mailroom_from_office4(self):
        '''
        Return to mailroom after delivering at office 4.
        '''
        self.wh.turn_90_right_back()

        self.wh.go_straight(BLOCK_CM)
        
        self.wh.turn_90_left()

        #self.wh.go_straight(35)
        self.wh.go_straight_gyro(self.gyro, 3.0, 360)


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
    gyro_sensor = EV3GyroSensor(1)
    wait_ready_sensors()

    nav = NavigationSystem(wheels, delivery, color_sensor, gyro_sensor)
    nav.go_to_first_office()
    nav.go_to_office2()
    nav.go_to_office3()
    nav.go_to_office4()
        
