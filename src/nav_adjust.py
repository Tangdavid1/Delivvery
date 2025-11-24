from utils.brick import EV3UltrasonicSensor
from wheels import Wheels
import time
import math


#def turn_angle(self, angle_deg: int, direction: str)

# On initialization, measure the initial distance from an object
def initialize(ultrasonic_port= "s1", initial_distance=30, time_interval=2):
    


    #continuously try to read from the ultrasonic sensor until a valid reading is obtained

    while True:

        try:
            #if distance measured is greater than initial distance, adjust to the left
            ultrasonic_sensor = EV3UltrasonicSensor(ultrasonic_port)
            distance = ultrasonic_sensor.get_value()
            if distance > initial_distance:
                initial_distance = distance
                Wheels.turn_angle(5, "left")


            #if distance is less than initial distance, adjust to the right
            elif distance < initial_distance:
                initial_distance = distance
                Wheels.turn_angle(5, "right")
            else:

            #no adjustment needed
                pass

        except IOError as error:

            print(error)

            time.sleep(time_interval)

if __name__ == "__main__":
    initialize()

    

    