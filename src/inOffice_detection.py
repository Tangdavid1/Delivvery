from utils.brick import Motor, EV3ColorSensor

import movement
import time 
import math

color = EV3ColorSensor(1) # port S2

colorScanned = False

def scanningProcess(motor: Motor):
    global colorScanned

    # turn left and scan for color
    movement.turn_90_left(motor, motor)

    time.sleep(1)  
    if color.get_color() != 'None':  
        colorScanned = True
        return

    # Go back to original position by reverting turn left
    movement.turn_90_left(motor, motor)
    movement.turn_90_left(motor, motor)
    movement.turn_90_left(motor, motor)

    # turn right and scan for color
    movement.turn_90_right(motor, motor)
    time.sleep(1)  
    if color.get_color() != 'None':
        colorScanned = True
        return

    # Go back to original position by reverting turn right
    movement.turn_90_right(motor, motor)
    movement.turn_90_right(motor, motor)
    movement.turn_90_right(motor, motor)

def scanOffice(motor: Motor):
    global colorScanned

    while not colorScanned:
        scanningProcess(motor)

        # if not color scanned, move forward and scan again
        movement.go_forward_both_wheels(motor, motor, 60)
        scanningProcess(motor)

        # if still not scanned, move backwards and scan again
        movement.go_forward_both_wheels(motor, motor, -20)
        scanningProcess(motor)

        # if still not scanned, move backwards and scan again
        movement.go_forward_both_wheels(motor, motor, -20)
        scanningProcess(motor)

        # if still not scanned, move forward to original position
        movement.go_forward_both_wheels(motor, motor, -20)
        scanningProcess(motor)






