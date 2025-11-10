"""
Main program file for our python mini project.
Authors: David Tang, Santiago Padron
"""

from utils import sound
from utils.brick import TouchSensor, EV3UltrasonicSensor, wait_ready_sensors, reset_brick, Motor, SensorError
from time import sleep
import threading

# Helper function for the drumming loop
# Argument is the motor we want to use to drum
def drumming(motor):
    motor.set_position(-40)
    sleep(0.2)
    motor.set_position(0)
    sleep(0.2)

# Helper function for the note detection algorithm.
# Arguments are the ultrasonic sensor, the delay, and the four tones we want to play
def note_detection(US_SENSOR, DELAY_SEC, tone1, tone2, tone3, tone4):
    us_data = US_SENSOR.get_value()  # Float value in centimeters 0, capped to 255 cm
    
    if 0 < us_data <= 10:
        tone1.play().wait_done()
    elif 10 < us_data <= 20:
        tone2.play().wait_done()
    elif 20 < us_data <= 30:
        tone3.play().wait_done()
    elif 30 < us_data <= 255:
        tone4.play().wait_done()

    sleep(DELAY_SEC)

# Main function for our robot drummer
def main():
    # CONSTANTS
    DELAY_SEC = 0.1
    TONE_1 = sound.Sound(duration=0.2, volume=100, pitch="C4")
    TONE_2 = sound.Sound(duration=0.2, volume=100, pitch="D4")
    TONE_3 = sound.Sound(duration=0.2, volume=100, pitch="E4")
    TONE_4 = sound.Sound(duration=0.2, volume=100, pitch="F4")

    # Initialize sensors and motors
    MOTOR = Motor("A")
    START_TRIGGER = TouchSensor(1)
    EMERGENCY_STOP = TouchSensor(2)
    US_SENSOR = EV3UltrasonicSensor(3)

    wait_ready_sensors(True)
    MOTOR.reset_encoder()
    print("Drumming system ready. Press the touch sensor to start.")

    active = False

    try:
        while True:
            if EMERGENCY_STOP.is_pressed():
                print("Emergency stop triggered. Stopping all motors.")
                active = False
                break

            if START_TRIGGER.is_pressed():
                print("active...")
                active = True
            
            if active:
                # Create threads to run both drumming and note detection
                t1 = threading.Thread(target=drumming, args=(MOTOR,))
                t2 = threading.Thread(target=note_detection, args=(US_SENSOR, DELAY_SEC, TONE_1, TONE_2, TONE_3, TONE_4))
                t1.start()
                t2.start()
                t1.join()
                t2.join()

    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        print("Resetting BrickPi and shutting down safely.")
        reset_brick()


if __name__ == "__main__": # runs main program
    main()
