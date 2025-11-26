#import dependencies
from office_navigation import NavigationSystem
from utils.brick import EV3ColorSensor, wait_ready_sensors
from wheels import Wheels
from delivery import DeliverySystem
import office_scanning as office

class Robot:
    def __init__(self, left_wheel_port: str, right_wheel_port: str, conveyor_belt_port: str, color_sensor_port: int, touch_sensor_port: int):
        self.WHEELS = Wheels(left_wheel_port, right_wheel_port)
        self.DELIVERY_SYSTEM = DeliverySystem(conveyor_belt_port)
        self.COLOR_SENSOR = EV3ColorSensor(color_sensor_port)
        self.NAVIGATION_SYSTEM = NavigationSystem(self.WHEELS, self.DELIVERY_SYSTEM, self.COLOR_SENSOR)
    
    def play():
        # run everything
        pass

if __name__ == "__main__":
    wheels = Wheels("B", "C")
    delivery = DeliverySystem("D")
    color_sensor = EV3ColorSensor(2)
    wait_ready_sensors()

    # process an office: scan for red, then start scanning for green, if green found, turn 180 and drop package
    result = office.scanOffice(wheels, color_sensor)
    if result[0] > 0: #when green detected
        wheels.go_straight(-7)
        wheels.turn_180(True)
        delivery.drop_package()
        wheels.turn_180(False)
        wheels.go_straight(7)
        wheels.reverse_previous_position(result[1], result[2])
        wheels.go_straight(-result[0])


    
