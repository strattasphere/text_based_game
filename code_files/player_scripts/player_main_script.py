import math
import random

class Player:
    
    def __init__(self, name, map):
        
        self.name = name
        self.health = 100
        self.mana = 0
        self.weapon_count = 1
        self.weapon_list = ['rusty blade']
        self.item_count = 1
        self.item_list = ['potion']
    
        # choose a random start location for player

        while map[start_row][start_col] == 1:
            start_row = random.randint(0,1)
            start_col = random.randint(0,1)
        


        for lst in map:
            self.location = (0,0)
        
    def moveLocation(self, direction):

        if direction == 'north':
            x_loc, y_loc = self.location

            x_loc += 0
            y_loc += -1

            self.location = (x_loc, y_loc)

        elif direction == 'south':
            x_loc, y_loc = self.location
            x_loc += 0
            y_loc += 1

            self.location = (x_loc, y_loc)

        elif direction == 'east':
            x_loc, y_loc = self.location
            x_loc += 1
            y_loc += 0

            self.location = (x_loc, y_loc)

        elif direction == 'west':
            x_loc, y_loc = self.location
            x_loc += -1
            y_loc += 0

            self.location = (x_loc, y_loc)

        elif direction == 'stay':
            pass


def printTest():

    print("This is the player script")


