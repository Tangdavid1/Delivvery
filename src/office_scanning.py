from utils.brick import Motor, EV3ColorSensor

import movement_OBSOLETE
import color_average_finder
import color_detect
import time 
import math

color = EV3ColorSensor(1) # port S2

#Angle constants

frontleft_angle = -110

backleft_angle = 110

frontright_angle = 200

backright_angle = -200

colorScanned = False

# Movement functions used:
# go_forward_both_wheels(left_motor: Motor, right_motor: Motor, distance_cm: int)

# Color functions used:
# computeDistance(rgb)
#

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






