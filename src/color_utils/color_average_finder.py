from utils.brick import wait_ready_sensors, EV3ColorSensor, EV3UltrasonicSensor, TouchSensor
import math
import json


color = EV3ColorSensor(1) # port S2


# waits until every previously defined sensor is ready
wait_ready_sensors()


while True:

        input("Waiting. Press Enter to take Color ID Value")

#colors = {}

        current_color = [0, 0, 0]

        for i in range(1000):
                r= None
                g= None
                b= None
                while (r == None or g == None or b == None):
                        r, g, b = color.get_rgb()
                r_normalized = r/(r+g+b)
                g_normalized = g/(r+g+b)
                b_normalized = b/(r+g+b)
                current_color[0] += r_normalized
                current_color[1] += g_normalized
                current_color[2] += b_normalized

        for i in range(3):
                current_color[i] = (current_color[i]/1000)


        print(current_color)
# Convert to tuple (so it can be used as a dictionary key)
        avg_color = tuple(current_color)

# Store color mapping
        colors = {str(avg_color): "blue"}  # use str() for JSON compatibility


        with open("colors.json", "a") as file:
                json.dump(colors, file, indent=2)


input("Waiting. Press Enter to take Color Component Data")


