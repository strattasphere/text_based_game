
from game_scripts import map 
import math
import random

class Player:
    
    def __init__(self, name, player_loc):
        
        self.name = name
        self.health = 100
        self.mana = 0
        self.weapon_count = 1
        self.weapon_list = ['rusty blade']
        self.item_count = 1
        self.item_list = ['potion']

        self.location = player_loc
        
    def moveLocation(self, direction):

        if direction == 'north':
            
            self.location[0] += 0
            self.location[1] += -1

        elif direction == 'south':

            self.location[0] += 0
            self.location[1] += 1

        elif direction == 'east':
           
            self.location[0] += 1
            self.location[1] += 0

        elif direction == 'west':
           
            self.location[0] += -1
            self.location[1] += 0

        elif direction == 'stay':
            pass


def printTest():

    print("This is the player script")


