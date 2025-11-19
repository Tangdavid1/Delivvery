from utils.brick import Motor
from utils.sound import Sound
from time import sleep
import math

class DeliverySystem: 
    def __init__(self, motor_port="D"):
        self.belt = Motor(motor_port)

        #Make a sound once all of the 2 packages were dropped in the office
        self.finish_sound = Sound(duration = 0.6, volume = 120, pitch = "A4")

        #Make a sound after visiting all 4 offices
        self.mailroom_sound = Sound(duration = 1, volume = 100, pitch="C5")
        
        #We would like to keep track of how many packages were dropped
        self.count = 0

        #Constants
        self.MOTOR_POLL_DELAY = 0.05

    def wait_for_motor(self):
        while math.isclose(self.belt.get_speed(), 0):
            sleep(self.MOTOR_POLL_DELAY)
        while not math.isclose(self.belt.get_speed(), 0):
            sleep(self.MOTOR_POLL_DELAY)

    def drop_package(self): 
        #Move forward to drop the package
        self.belt.set_position_relative(100)
        self.wait_for_motor()
        sleep(0.4)

        #We would like to keep a track of the dropped pacakges
        self.count +=1

        #Only play the sound when both packages are delivered 
        if self.count == 2:
            self.finish_sound.play().wait_done()
    
    def reset_for_next_office(self):
        """
        We call this after finishing the dropping of each 
        office to reset the count.  
        """
        self.count=0
    
    def play_sound_once_all_is_visited(self):
        #When the robot returns to the mailroom, play sound
        self.mailroom_sound.play().wait_done()


if __name__ == "__main__":
    # Initialize your system (motor on port D)
    system = DeliverySystem("D")
    print("TEST 1: Dropping first package")
    system.drop_package()
    sleep(1)

    print("TEST 2: Dropping second package (should play finish sound)")
    system.drop_package()
    sleep(1)

    print("Resetting for next office")
    system.reset_for_next_office()
    sleep(1)

    print("TEST 3: Dropping two packages again")
    system.drop_package()
    sleep(1)
    system.drop_package()
    sleep(1)

    print("TEST 4: Test mailroom sound")
    system.play_sound_once_all_is_visited()

    print("All tests finished.")
