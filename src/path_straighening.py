"""
Note detection code.
"""
"""
Note Detection mechanism code.
Author: David Tang
Date: October 12th, 2025
"""

from utils import sound
from utils.brick import TouchSensor, EV3UltrasonicSensor, wait_ready_sensors, reset_brick
from time import sleep


DELAY_SEC = 1  # seconds of delay between measurements
US_SENSOR_DATA_FILE = "../data_analysis/us_sensor.csv"

TOUCH_SENSOR = TouchSensor(1)
US_SENSOR = EV3UltrasonicSensor(3)


def detect_note():
    #IMPLEMENT ME!
    tone1 = sound.Sound(duration=1.0, volume=80, pitch="C4")

    tone2 = sound.Sound(duration=1.0, volume=80, pitch="D4")

    tone3 = sound.Sound(duration=1.0, volume=80, pitch="E4")

    tone4 = sound.Sound(duration=1.0, volume=80, pitch="G4")
    try:
        while not TOUCH_SENSOR.is_pressed():
            pass  # do nothing while waiting for first button press
        print("Touch sensor pressed")
        sleep(1)
        print("Starting to collect US distance samples")
        out_file = open(US_SENSOR_DATA_FILE, "w")
        while not TOUCH_SENSOR.is_pressed():
            us_data = US_SENSOR.get_value()  # Float value in centimeters 0, capped to 255 cm
            if 0 < us_data <= 10:
                tone1.play().wait_done()
            elif 10 < us_data <= 20:
                tone2.play().wait_done()
            elif 20 < us_data <= 30:
                tone3.play().wait_done()
            elif 30 < us_data <= 255:
                tone4.play().wait_done()

            out_file.write(f"{us_data}\n")

            sleep(DELAY_SEC)
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    finally:
        print("Stopping US sensor detection.")
        out_file.close()
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()

if __name__ == "__main__":
    #Use this for testing of this functionality
    detect_note()
