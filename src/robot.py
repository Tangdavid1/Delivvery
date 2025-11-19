#import dependencies
from utils.brick import EV3ColorSensor, wait_ready_sensors
from wheels import Wheels
from delivery import DeliverySystem
import office_scanningV2 as office

class Robot:
    def __init__(self,):
        pass
        self.touch_sensor = TouchSensor(1)
    def play():
        # run everything
        pass

if __name__ == "__main__":
    wheels = Wheels("B", "C")
    delivery = DeliverySystem("D")
    color_sensor = EV3ColorSensor(2)
    wait_ready_sensors()

    # process an office: scan for red, then start scanning for green, if green found, turn 180 and drop package
    if office.scanOffice(wheels, color_sensor) == 1:
        wheels.go_straight(-7)
        wheels.turn_180(True)
        delivery.drop_package()

    
