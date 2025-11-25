from utils.brick import wait_ready_sensors
from utils.brick import Motor, EV3UltrasonicSensor
import time
from utils.brick import EV3ColorSensor

#Left wheel is on port = "B"
left_motor = Motor("B")
#Right wheel is on port = "C"
right_motor = Motor("C")
#The ultrasonic sensor is on port 1
ultrasonic = EV3UltrasonicSensor(1)
#The color sensor is on port 2
color=EV3ColorSensor(2)

#The ultrasonic is ON for the first 10 seconds
side_ultrasonic_duration= 100.0
#Check ultrasonic every 2 sec
check_interval = 0.1

state = "side_ultrasonic_on"
#When the side started
side_start_time = time.time()
#Last ultrasonic measurement
last_ultrasonic_check_time = time.time()

desiredDist = 5
baseDeg = 180
prev_distance= None

def forward():
    left_motor.set_dps(baseDeg)
    right_motor.set_dps(baseDeg)

def deltaAdjust(dist):
    global prev_distance

    # Initialize
    if prev_distance is None:
        prev_distance = dist
        return

    error = desiredDist - dist
    delta_rate = dist - prev_distance

    # KEY FIX: Predict future drift based on current trend
    # If sensor hasn't changed (delta_rate == 0) but we're off target,
    # assume we're STILL drifting in the same direction
    if abs(error) > 0.3:
        # Assume continuing drift - amplify correction
        predicted_error = error * 0.5  # Predict we'll drift further
    else:
        predicted_error = error

    # Aggressive P for slow sensor, ignore useless D
    Kp = 15   # Very high for strong immediate correction

    correction = Kp * predicted_error*0.5

    # Allow strong corrections
    correction = max(-70, min(70, correction))

    # Apply
    left_motor.set_dps(baseDeg + correction)
    right_motor.set_dps(baseDeg - correction)

    prev_distance = dist
    print(f"d={dist:.1f} e={error:.2f} pred={predicted_error:.2f} c={correction:.0f}")



def stop():
    left_motor.set_power(0)
    right_motor.set_power(0)

def rotate_right():
    left_motor.set_power(40)
    right_motor.set_power(-40)

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
                    distance = ultrasonic.get_value()

                    if distance is not None:
                        print("Distance:", distance, "cm")

                        deltaAdjust(distance)
                    #Reset the timer
                    last_ultrasonic_check_time = now

                #Turn off the ultrasonic sensor after 10 seconds
                if now - side_start_time >= side_ultrasonic_duration:
                    print("10 seconds done so it will be turning right")
                    state = "turning"
                    rotate_start_time = time.time()

            #State 2(Ultrasonic is OFF)
            #Rotate Right
            # elif state == "turning":
            #     rotate_right()

            #     if time.time() - rotate_start_time >= 1.2:
            #         print("Rotation finished.")
            #         stop()
            #         state = "wait for the intersection"

            # #State 3
            # #Keep on moving forward until we reach an intersection
            # elif state == "wait for the intersection":
            #     #the ultrasonic is OFF until it reaches an intersection
            #     forward()

            #     #if black line is detected
            #     if color.get_color_name()=="BLACK":
            #         print("The intersection is found so ultrasonic sensor is back ON")
            #         #Ultrasonic is ON
            #         state = "side_ultrasonic_on"
            #         side_start_time = time.time()
            #         last_ultrasonic_check_time = time.time()



    except KeyboardInterrupt:
        stop()
        print("Stopped.")

