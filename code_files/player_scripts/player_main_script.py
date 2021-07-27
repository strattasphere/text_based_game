

class Player:
    
    def __init__(self, name):
        
        self.name = name
        self.health = 100
        self.mana = 0
        self.weapon_count = 1
        self.weapon_list = ['rusty blade']
        self.item_count = 1
        self.item_list = ['potion']
        self.location = (0,0)
        
    def moveLocation(self, direction):

        if direction == 'north':
            x_loc, y_loc = self.location

            x_loc += 0
            y_loc += 1

            self.location = (x_loc, y_loc)

        elif direction == 'south':
            x_loc, y_loc = self.location
            x_loc += 0
            y_loc += -1

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


def printTest():

    print("This is the player script")


