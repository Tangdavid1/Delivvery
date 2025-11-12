from utils.brick import wait_ready_sensors, EV3ColorSensor, EV3UltrasonicSensor, TouchSensor

color = EV3ColorSensor(2) # port S2

# waits until every previously defined sensor is ready
wait_ready_sensors()

color.get_raw_value() # usually list [r,g,b,intensity], sometimes one number

input("Waiting. Press Enter to take Color ID Value")

color_name = color.get_color_name()
print(color_name)

input("Waiting. Press Enter to take Color Component Data")


rgb_list = color.get_rgb()
print(rgb_list)


