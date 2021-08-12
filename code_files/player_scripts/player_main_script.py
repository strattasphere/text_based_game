
from game_scripts import map 
from game_scripts import locations
import math
import random

class Player:
    
    def __init__(self, name, player_loc):
        
        self.name = name
        self.health = 10
        self.armour = 3
        self.mana = 0
        self.weapon_count = 1
        self.weapon_list = ['rusty blade']
        self.item_count = 1
        self.item_list = ['potion']
        self.keep_key = False

        self.location = player_loc
        
    def moveLocation(self, direction, player_map_array):

        x_val, y_val = self.location[0], self.location[1]

        if direction == 'north' or direction == 'walk north' or direction == 'walk up'  or direction == 'up':
            try:
                if player_map_array[x_val-1][y_val] == 0:

                    self.location[0] += -1
                    self.location[1] += 0
                else:
                    print("\n\tYou've hit a wall! You can't go that way!")
            except:
                print("\n\tStop trying to leave the city... Has it really got too much for you?")
            

        elif direction == 'south' or direction == 'walk south' or direction == 'walk down' or direction == 'down':

            try:
                if player_map_array[x_val+1][y_val] == 0:

                    self.location[0] += 1
                    self.location[1] += 0

                else:
                    print("\n\tYou've hit a wall! You can't go that way!")    
            
            except:
                print("\n\tStop trying to leave the city... Has it really got too much for you?")


        elif direction == 'east' or direction == 'walk east' or direction == 'walk right' or direction == 'right':
            try:
                if player_map_array[x_val][y_val+1] == 0:

                    self.location[0] += 0
                    self.location[1] += 1

                else:
                    print("\n\t You've hit a wall! You can't go that way!")

            except:
                print("\n\tStop trying to leave the city... Has it really got too much for you?")

            

        elif direction == 'west' or direction == 'walk west' or direction == 'walk left' or direction == 'left':
            try:  
                if player_map_array[x_val][y_val-1] == 0:

                    self.location[0] += 0
                    self.location[1] += -1

                else:
                    print("\n\t You've hit a wall! You can't go that way!")
                    
            except:
                print("\n\tStop trying to leave the city... Has it really got too much for you?")
            

        elif direction == 'stay':
            pass

    def checkLocation(self):
        if self.location == locations.tavern.location:
            print("\n\tYOU'VE ARRIVED AT THE TAVERN")

        elif self.location == locations.blacksmth_loc:
            print("\n\tYOU'VE ARRIVED AT THE BLACKSMITH")

        elif self.location == locations.church_loc:
            print("\n\tYOU'VE ARRIVED AT THE CHURCH")

        elif self.location == locations.guard_twr_loc:
            print("\n\tYOU'VE ARRIVED AT THE GUARD TOWER")

        elif self.location == locations.keep_loc:
            print("\n\tYOU'VE ARRIVED AT THE KEEP")


def printTest():

    print("This is the player script")


