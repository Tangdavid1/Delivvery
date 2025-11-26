from utils.brick import Motor, TouchSensor
import time 
import sys

left_motor = Motor("B")
right_motor=Motor("C")
touch_sensor=TouchSensor(1)

def stop_all():
    #Stop all motors immediately
    left_motor.set_power(0)
    right_motor.set_power(0)
    print("Emergency Stop has been activated")
    sys.exit(0)

def check_emergency():
    if touch_sensor.is_pressed():
        stop_all()

if __name__=="__main__":
    print("Press the touch sensor to stop the robot")
    while True: 
        check_emergency() 
        time.sleep(0.05)
