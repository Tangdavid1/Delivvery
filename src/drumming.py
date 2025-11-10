"""
Drumming mechanism code.
"""
"""
Drumming mechanism code.
Author: David Tang
Date: October 12th, 2025
"""

from utils.brick import Motor, BP, TouchSensor, wait_ready_sensors, SensorError
import time


def drumming():
    """
     Controls a BrickPi motor that simulates a drumming motion.
     The arm will move between 0° (up) and 120° (down) when the touch sensor is pressed.
     """

    # Initialize sensors and motor
    motor = Motor("A")          # Drumming motor
    trigger = TouchSensor(1)  # Sensor to start drumming
    emergency = TouchSensor(2)  # Optional emergency stop

    # Ensure hardware is ready
    wait_ready_sensors(True)

    # Calibrate initial position
    motor.reset_encoder()
    print("Drumming system ready. Press the touch sensor to start.")

    active = False
    try:
        while True:
            # Emergency stop
            if emergency.is_pressed():
                print("Emergency stop triggered. Stopping all motors.")
                active = False
                break

            # Trigger drumming
            if trigger.is_pressed():
                print("active...")
                active = True



            if active:
                print("Drumming...")
                motor.set_position(120)
                time.sleep(0.4)
                motor.set_position(0)
                time.sleep(0.4)


            #time.sleep(0.1)  # Avoid busy looping

    except SensorError as e:
        print("Sensor error:", e)

    except KeyboardInterrupt:
        print("Interrupted by user.")

    finally:
        print("Resetting BrickPi and shutting down safely.")
        BP.reset_all()

if __name__ == "__main__":
    #Use this for testing of this functionality
    drumming()

