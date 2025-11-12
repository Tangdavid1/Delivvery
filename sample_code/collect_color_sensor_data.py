#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
"""

# Add your imports here, if any
from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor, reset_brick


COLOR_SENSOR_DATA_FILE = "../data_analysis/color_sensor.csv"

# complete this based on your hardware setup
COLOR = EV3ColorSensor(2)
TOUCH = TouchSensor(1)

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.


def collect_color_sensor_data():
    "Collect color sensor data."
    try:
        file = open(COLOR_SENSOR_DATA_FILE, "w")
        while True:
            r, g, b, l = COLOR.get_value()
            if TOUCH.is_pressed():
                print([r, g, b])
                file.write(f"[{r}, {g}, {b}]\n")
    except BaseException:  # want to stop the program when we Ctrl-C
        print("Done.")
    finally:
        file.close()
        reset_brick()
        exit()


if __name__ == "__main__":
    collect_color_sensor_data()
