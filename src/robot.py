#import dependencies
from office_navigation import NavigationSystem
from utils.brick import EV3ColorSensor, EV3GyroSensor, wait_ready_sensors, TouchSensor, reset_brick
from wheels import Wheels
from delivery import DeliverySystem
import office_scanning as office

class Robot:
    def __init__(self, left_wheel_port: str, right_wheel_port: str, conveyor_belt_port: str, color_sensor_port: int, touch_sensor_port: int, gyro_sensor_port: int):
        self.WHEELS = Wheels(left_wheel_port, right_wheel_port, touch_sensor_port)
        self.DELIVERY_SYSTEM = DeliverySystem(conveyor_belt_port)
        self.COLOR_SENSOR = EV3ColorSensor(color_sensor_port)
        self.GYRO_SENSOR = EV3GyroSensor(gyro_sensor_port)
        self.NAVIGATION_SYSTEM = NavigationSystem(self.WHEELS, self.DELIVERY_SYSTEM, self.COLOR_SENSOR, self.GYRO_SENSOR)
        #self.EMERGENCY_STOP = TouchSensor(touch_sensor_port)
        self.status = "idle"
        wait_ready_sensors()
    
    def play(self):
        self.NAVIGATION_SYSTEM.go_to_first_office()
        self.NAVIGATION_SYSTEM.go_to_office2()

        if (self.DELIVERY_SYSTEM.count == 2):
            self.NAVIGATION_SYSTEM.return_to_mailroom_from_office2()
            self.DELIVERY_SYSTEM.play_sound_once_all_is_visited()
            reset_brick()
            return
        
        self.NAVIGATION_SYSTEM.go_to_office3()
        
        if (self.DELIVERY_SYSTEM.count == 2):
            self.NAVIGATION_SYSTEM.return_to_mailroom_from_office3()
            self.DELIVERY_SYSTEM.play_sound_once_all_is_visited()
            reset_brick()
            return
        
        self.NAVIGATION_SYSTEM.go_to_office4()
        self.DELIVERY_SYSTEM.play_sound_once_all_is_visited()
        
        reset_brick()
        

if __name__ == "__main__":
    robot = Robot("B", "C", "D", 2, 4, 1)
    #Process a single office
    try:
        robot.play()
    except IOError:
        reset_brick()
