from utils.brick import wait_ready_sensors
from utils.brick import Motor, EV3UltrasonicSensor, EV3GyroSensor
import time
from utils.brick import EV3ColorSensor

#Left wheel is on port = "B"
left_motor = Motor("B")
#Right wheel is on port = "C"
right_motor = Motor("C")

gyro = EV3GyroSensor(1)


#The ultrasonic is ON for the first 10 seconds
side_ultrasonic_duration= 100.0
#Check ultrasonic every 2 sec
check_interval = 0.01

state = "side_ultrasonic_on"
#When the side started
side_start_time = time.time()
#Last ultrasonic measurement
last_ultrasonic_check_time = time.time()

desiredDist = 4.4
baseDeg = 360
prev_distance= None

def forward():
    left_motor.set_dps(baseDeg)
    right_motor.set_dps(baseDeg)

def deltaAdjust(angle):
    ang = angle[0]
    # Ignore bad data
    Kp = 2
    correction = Kp *ang

    left_motor.set_dps(baseDeg - correction)
    right_motor.set_dps(baseDeg + correction)


def stop():
    left_motor.set_dps(0)
    right_motor.set_dps(0)


if __name__ == "__main__":
    wait_ready_sensors()
    try:
        forward()
        while True:
            #State 1(Ultrasonic Sensor is ON)
            #Ultrasonic sesnor is ON for the first 10 seconds
            if state == "side_ultrasonic_on":
                now = time.time()

                if now - last_ultrasonic_check_time >= check_interval:
                    #distance = ultrasonic.get_value()
                    angle = gyro.get_value()
                    if angle is not None:
                        print("Angle:", angle, "deg")

                        deltaAdjust(angle)
                    #Reset the timer
                    last_ultrasonic_check_time = now

                #Turn off the ultrasonic sensor after 10 seconds
                if now - side_start_time >= side_ultrasonic_duration:
                    print("10 seconds done so it will be turning right")
                    state = "turning"
                    rotate_start_time = time.time()

    except KeyboardInterrupt:
        stop()
        print("Stopped.")
