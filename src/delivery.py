from utils.brick import Motor
from utils.sound import Sound
from time import sleep

class DeliverySystem: 
    def __init__(self, motor_port="A"):
        self.belt = Motor(motor_port)

        #Make a sound once all of the 2 packages were dropped in the office
        self.finish_sound = Sound(duration = 0.6, volume = 120, pitch = "A4")

        #Make a sound after visiting all 4 offices
        self.mailroom_sound = Sound(duration = 1, volume = 100, pitch="C5")
        
        #We would like to keep track of how many packages were dropped
        self.count = 0

    def drop_package(self): 
        #Move forward to drop the package
        self.belt.set_position_relative(90)
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


        