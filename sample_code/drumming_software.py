
#Author: David tang
#Date: October 12th, 2025
#sample code we will use: I decided to use positional rotation instead of power/speed since it seems more reliable.
from utils.brick import Motor, BP, Motor, TouchSensor, EV3ColorSensor, wait_ready_sensors, SensorError
import time

#Assume we will be using port A for the motor for drumming.
EMERGENCY = TouchSensor("C")
T_SENSOR = TouchSensor("B")
motor = Motor("A")

# Designates to Encoder, that the current physical position is 0 degrees
# We should have the arm facing straight up.
wait_ready_sensors(True)
motor.reset_encoder()

while True:
    try:
        if  T_SENSOR.isPressed():
            # Rotate to position that is 120 degrees away from the 0 position
            motor.set_position(120)
            time.sleep(0.5)
            motor.get_position()
            motor.set_position(0)
            time.sleep(0.5)
    except SensorError as error:
        print(error)
except KeyboardInterrupt:
BP.reset_all()

