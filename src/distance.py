from utils.brick import Motor, EV3UltrasonicSensor
import time

#Left wheel is on port = "B"
left_motor = Motor("B")   
#Right wheel is on port = "C"    
right_motor = Motor("C")
#The ultrasonic sensor is on port 1      
ultrasonic = EV3UltrasonicSensor(1)  

def forward():
    left_motor.set_power(40)
    right_motor.set_power(40)

def soft_left():
    #We make the left motor a little slower
    left_motor.set_power(25) 
    #We make the right motor a little faster     
    right_motor.set_power(45)     

def soft_right():
    #We make the left motor a little faster
    left_motor.set_power(45)  
    #We make the right motor a little slower    
    right_motor.set_power(25)      

try:
    while True:
        #We would like to read the distance
        distance = ultrasonic.get_value()     

        if distance is None:  
            continue

        print("Distance:", distance, "cm")

        if distance < 20:
            print("Too close, move a little bit to the right")
            soft_right()

        elif distance > 30:
            print("Too far,  move a little bit to the left")
            soft_left()

        else:
            print("Perfect distance, move forward")
            forward()

        time.sleep(0.1)

except KeyboardInterrupt:
    left_motor.set_power(0)
    right_motor.set_power(0)
    print("Stopped.")
