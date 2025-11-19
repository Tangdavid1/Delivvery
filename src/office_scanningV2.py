from wheels import Wheels
from utils.brick import EV3ColorSensor, wait_ready_sensors

ANGLE = 150

def scanningProcess(wheels: Wheels, color_sensor: EV3ColorSensor, color: str) -> bool:
    # turn left and scan for color
    found_color = wheels.turn_angle_and_check_color(ANGLE, "left", color, color_sensor)

    if found_color:
        return True

    # Go back to original position by reverting turn left
    wheels.turn_angle_and_check_color(-ANGLE, "left", color, color_sensor)

    # turn right and scan for color
    found_color = wheels.turn_angle_and_check_color(ANGLE, "right", color, color_sensor)

    if found_color:
        return True

    # Go back to original position by reverting turn right
    wheels.turn_angle_and_check_color(-ANGLE, "right", color, color_sensor)
    return False


def scanOffice(wheels: Wheels, color_sensor: EV3ColorSensor) -> int:
    if scanningProcess(wheels, color_sensor, "red"):
        return 0

    # if not color scanned, move forward and scan again
    wheels.go_straight(20)
    
    for i in range(4):
        if scanningProcess(wheels, color_sensor, "green"):
            return 1

        # if still not scanned, move backwards and scan again
        wheels.go_straight(-3)

    return -1


if __name__ == "__main__":
    wheels = Wheels("B", "C")
    color_sensor = EV3ColorSensor(2)
    wait_ready_sensors()
    scanOffice(wheels, color_sensor)
