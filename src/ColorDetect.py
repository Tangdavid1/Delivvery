  GNU nano 8.6                              LineDetection.py
from utils.brick import wait_ready_sensors, EV3ColorSensor, EV3UltrasonicSensor, TouchSensor
import math




# created method for computing nearest cluster
def computeDistance(rgb):
    color = None
    min_dist= 300 # since max is 255, this will ensure max initial is above it.
    for i in range(len(R)):
        D = math.sqrt(pow((rgb[0]-R[i]),2)+pow((rgb[1]-G[i]),2)+pow((rgb[2]-B[i]),2))
        if(D<min_dist):
            color = i
            min_dist = D
    if color==None:
        print("Error, invalid color")
    else:
        return(colorList[color])


# script
colorList=("red", "green", "yellow" , "orange", "blue" , "black" , "white")
r = []
g = []
b = []



color = EV3ColorSensor(2) # port S2

# waits until every previously defined sensor is ready
wait_ready_sensors()

color.get_raw_value() # usually list [r,g,b,intensity], sometimes one number

input("Waiting. Press Enter to take Color ID Value")


closest_color = computeDistance(color.get_rgb())


input("Waiting. Press Enter to take Color Component Data")


rgb_list = color.get_rgb()
print(rgb_list)



        
