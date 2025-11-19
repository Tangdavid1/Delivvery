from utils.brick import wait_ready_sensors, EV3ColorSensor, EV3UltrasonicSensor, TouchSensor
import math

#{
#  "(0.8333333333333433, 0.1172839506172815, 0.04938271604938167)": "red"
#}{
#  "(0.3737024221453372, 0.5778546712802685, 0.04844290657439399)": "green"
#}
#{
#  "(0.676011090029638, 0.2934346556750594, 0.030554254295305495)": "orange"
#}
#{
#  "(0.328125, 0.43973214285715145, 0.2321428571428597)": "blue"
#}
#{
#  "(0.5579144244105435, 0.4111973647711494, 0.030888210818308705)": "yellow"
#}
#{
#  "(0.4363872528125503, 0.3905860748375745, 0.17302667234988325)": "white"
#}
#
#{
#  "(0.4117647058823596, 0.4313725490196124, 0.15686274509803871)": "black"
#}


# created method for computing nearest cluster
def computeDistance(rgb):
        intensity = rgb[0] + rgb[1] + rgb[2]
        color = None
        min_dist= 2 # since max is 1, this will ensure max initial is above it.

        normalized_r = rgb[0]/(intensity)
        normalized_g = rgb[1]/(intensity)
        normalized_b = rgb[2]/(intensity)
        for i in range(len(R)):
                D = math.sqrt(pow((normalized_r-R[i]),2)+pow((normalized_g-G[i]),2)+pow((normalized_b-B[i]),2))
                #print(f"Color: {i} , {D}")
                if(D<min_dist):
                        color = i
                        min_dist = D
        if color==None:
                print("Error, invalid color")
        else:
                if colorList[color] == "black" or colorList[color] == "white":
                        if intensity > 500:
                                return "white"
                        else:
                                return "black"

                return(colorList[color])


# script
colorList=("red", "green", "orange" , "blue", "yellow" , "white" , "black")
R = [0.8333333333333433, 0.3737024221453372, 0.676011090029638, 0.328125, 0.5579144244105435, 0.4363872528125503, 0.4117647058823596]
G = [0.1172839506172815, 0.5778546712802685, 0.2934346556750594, 0.43973214285715145, 0.4111973647711494, 0.3905860748375745, 0.4313725490196124]
B = [0.04938271604938167, 0.04844290657439399, 0.030554254295305495, 0.2321428571428597, 0.030888210818308705, 0.17302667234988325, 0.15686274509803871]


if __name__ == "__main__":
    color = EV3ColorSensor(1) # port S1

    # waits until every previously defined sensor is ready
    wait_ready_sensors()

    color.get_raw_value() # usually list [r,g,b,intensity], sometimes one number

    input("Waiting. Press Enter to take Color ID Value")

    temp = color.get_rgb()
    while(temp[0]==None or temp[1]==None or temp[2]==None):
        temp=color.get_rgb()
    print(temp)
    closest_color = computeDistance(temp)


    print(closest_color)

    #input("Waiting. Press Enter to take Color Component Data")


    #rgb_list = color.get_rgb()
    #print(rgb_list)
