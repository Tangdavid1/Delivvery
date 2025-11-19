from utils.brick import Motor, EV3ColorSensor

import movement_OBSOLETE
import color_average_finder
import color_detect
import time 
import math

color = EV3ColorSensor(1) # port S2

# Angle constants

frontleft_angle = -110

backleft_angle = 110

frontright_angle = 200

backright_angle = -200

# Some variables

colorScanned = False

turn_Counter = 0

# Movement functions used:
# go_forward_both_wheels(left_motor: Motor, right_motor: Motor, distance_cm: int)
# def turn_angle(left_motor: Motor, right_motor: Motor, angle_deg: int, direction: str):

# Color functions used:
# computeDistance(rgb)

# colorList=("red", "green", "orange" , "blue", "yellow" , "white" , "black")
# R = [0.8333333333333433, 0.3737024221453372, 0.676011090029638, 0.328125, 0.5579144244105435, 0.4363872528125503, 0.4117647058823596]
# G = [0.1172839506172815, 0.5778546712802685, 0.2934346556750594, 0.43973214285715145, 0.4111973647711494, 0.3905860748375745, 0.4313725490196124]
# B = [0.04938271604938167, 0.04844290657439399, 0.030554254295305495, 0.2321428571428597, 0.030888210818308705, 0.17302667234988325, 0.15686274509803871]

def scanningProcess(motor: Motor):
    global colorScanned

    # turn left and scan for color
    movement_OBSOLETE.turn_90_left(motor, motor)

    time.sleep(1)  
    if color.get_color() != 'None':  
        colorScanned = True
        return

    # Go back to original position by reverting turn left
    movement_OBSOLETE.turn_angle(motor, motor, backleft_angle)

    # turn right and scan for color
    movement_OBSOLETE.turn_90_right(motor, motor)
    time.sleep(1)  
    if color.get_color() != 'None':
        colorScanned = True
        return

    # Go back to original position by reverting turn right
    movement_OBSOLETE.turn_angle(motor, motor, backright_angle)

def scanOffice(motor: Motor):
    global colorScanned

    while not colorScanned:
        scanningProcess(motor)

        # if not color scanned, move forward and scan again
        movement_OBSOLETE.go_forward_both_wheels(motor, motor, 60)
        scanningProcess(motor)

        # if still not scanned, move backwards and scan again
        movement_OBSOLETE.go_forward_both_wheels(motor, motor, -20)
        scanningProcess(motor)

        # if still not scanned, move backwards and scan again
        movement_OBSOLETE.go_forward_both_wheels(motor, motor, -20)
        scanningProcess(motor)

        # if still not scanned, move forward to original position
        movement_OBSOLETE.go_forward_both_wheels(motor, motor, -20)
        scanningProcess(motor)






