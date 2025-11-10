"""
Emergency stop code.
"""
from utils.brick import BP, TouchSensor, wait_ready_sensors, SensorError

def emergency_stop() -> bool:
    #Initialize sensor
    TOUCH_SENSOR = TouchSensor("C")

    wait_ready_sensors(True)

    try:
        while True:
            # Emergency stop
            if TOUCH_SENSOR.is_pressed():
                print("Emergency stop triggered. Stopping all motors.")
                return True
            return False

    except SensorError as e:
        print("Sensor error:", e)

    except KeyboardInterrupt:
        print("Interrupted by user.")

    finally:
        print("Resetting BrickPi and shutting down safely.")
        BP.reset_all()
    return False

if __name__ == "__main__":
    #Use this for testing of this functionality
    emergency_stop()
