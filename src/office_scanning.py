from wheels import Wheels
from utils.brick import EV3ColorSensor, wait_ready_sensors

ANGLE = 150

def scanningProcess(wheels: Wheels, color_sensor: EV3ColorSensor, color: str) -> tuple[bool, str, int]:
    # turn left and scan for color
    found_color, difference = wheels.turn_angle_and_check_color(ANGLE, "left", color, color_sensor)

    if found_color:
        return (True, "left", difference)

    # Go back to original position by reverting turn left
    wheels.turn_angle_and_check_color(-(ANGLE), "left", color, color_sensor)

    # turn right and scan for color
    found_color, difference = wheels.turn_angle_and_check_color(ANGLE, "right", color, color_sensor)

    if found_color:
        return (True, "right", difference)

    # Go back to original position by reverting turn right
    wheels.turn_angle_and_check_color(-(ANGLE), "right", color, color_sensor)
    return (False, "none", 0)


def scanOffice(wheels: Wheels, color_sensor: EV3ColorSensor) -> tuple[int, str, int]:
    result = scanningProcess(wheels, color_sensor, "red")
    if result[0]:
        wheels.reverse_previous_position(result[1], result[2])
        return (0, "none", 0)

    # if not color scanned, move forward and scan again
    wheels.go_straight(17)
    
    for i in range(6):
        result = scanningProcess(wheels, color_sensor, "green")
        if result[0]:
            return (17 - 3*i, result[1], result[2])

        # if still not scanned, move backwards and scan again
        wheels.go_straight(-3)


    return (-1, "none", 0)


if __name__ == "__main__":
    wheels = Wheels("B", "C")
    color_sensor = EV3ColorSensor(2)
    wait_ready_sensors()
    scanOffice(wheels, color_sensor)

