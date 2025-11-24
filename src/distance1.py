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
side_ultrasonic_duration= 10.0
#Check ultrasonic every 2 sec       
check_interval = 2.0      

state = "side_ultrasonic_on"
#When the side started
side_start_time = time.time() 
#Last ultrasonic measurement     
last_ultrasonic_check_time = time.time()   

class ultrasonicSensor 
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

def stop():
    left_motor.set_power(0)
    right_motor.set_power(0)

def rotate_right():
    left_motor.set_power(40)
    right_motor.set_power(-40)
     
if __name__ == "__main__":     
    try:
        while True:
            #State 1(Ultrasonic Sensor is ON)
            #Ultrasonic sesnor is ON for the first 10 seconds
            if state == "side_ultrasonic_on":
                now = time.time()

                if now - last_ultrasonic_check_time >= check_interval: 
                    distance = ultrasonic.get_value()  

                    if distance is not None:  
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
                
                    #Reset the timer
                    last_ultrasonic_check_time = now

                #Turn off the ultrasonic sensor after 10 seconds
                if now - side_start_time >= side_ultrasonic_duration:
                    print("10 seconds done so it will be turning right")
                    state = "turning"
                    rotate_start_time = time.time()
                
            #State 2(Ultrasonic is OFF)
            #Rotate Right
            elif state == "turning":
                rotate_right()   

                if time.time() - rotate_start_time >= 1.2:
                    print("Rotation finished.")
                    stop()
                    state = "wait for the intersection"

            #State 3
            #Keep on moving forward until we reach an intersection
            elif state == "wait for the intersection":
                #the ultrasonic is OFF until it reaches an intersection
                forward()   

                #if black line is detected
                if color.get_color_name()=="BLACK": 
                    print("The intersection is found so ultrasonic sensor is back ON")
                    #Ultrasonic is ON 
                    state = "side_ultrasonic_on"
                    side_start_time = time.time()
                    last_ultrasonic_check_time = time.time()

            time.sleep(0.05)

    except KeyboardInterrupt:
        stop()
        print("Stopped.")



