
# The Map

from numpy import array
import math
import random

# Procedural generation of the map happens here


# the map class stores the data about the map objects
class Map:
    
    def __init__(self, width, height):
        self.width = width # the width of the map
        self.height = height # the height of the map
        self.mapObjList = [] # a list of all the map objects


    def printMap(mapObjList):

        for obj in mapObjList:
        
            print (obj.top_bound)
            
            

            
    

class MapObject:
    
    def __init__(self, loc_id, env, right_bound, left_bound, top_bound, bottom_bound):
        self.loc_id = loc_id # the (x,y) value of the location
        self.env = env # the biome type of the room ()

        # the status of the walls (door_open, door_locked, wall)
        self.right_bound = right_bound
        self.left_bound = left_bound
        self.top_bound = top_bound
        self.bottom_bound = bottom_bound

        # map objects start in a hidden state, then are revealed by the player when entered
        self.revealed = False 
    

        def showBounds(): # prints the map object
            pass

        def hideBounds(): # hides the map object 
            pass

        def destroyBound(): # allows for a wall to be destoyed in game
            pass

        def openBound(): # allows for a boudary to be opened in game
            pass

        def closeBound(): # allows for a boundary to be closed in game
            pass

''' 
1. A function randomly generates a series of map objects that fit work with each other
2. These objects are put into a list
3. The list is printed in order combining the map objects to show a map
'''

def createArray(num, dimensions):
    array2D = [[] for pos in range(dimensions)] 
    x = 0
    for list in array2D:
        for elem in range(0, dimensions):
            array2D[x].append(num) 
        x += 1

    return array2D


# Procedural generation
def createMap():
    
    dimensions = 20 # width and height of the map
    max_tunnels = 50 # max number of tunnels possible
    max_length = 8 # max length each tunnel can have

    # create an array/list of 1's
    map = createArray(1, dimensions)

    current_row = math.floor(random.random() * dimensions) # our current row starting at a random row
    current_column = math.floor(random.random() * dimensions) # our current column starting at a random column

    print("Starting row =", current_row)
    print("Starting column =", current_column)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # array to get a random direction, up, down, left, right
    last_direction = [0,0] # saves the last direction we went
    random_direction = [0,0]

    # Create some tunnels

    while (max_tunnels > 0 and dimensions > 0 and max_length > 0):

        print("Max tunnels =", max_tunnels)
        print("Dimensions =", dimensions)
        print("Max_length =", max_length)



        print ("Creating tunnels has started")

        '''
        Gets a random directions until it is perpendicular to our last_direction
        if the last direction = left or right,
        then our new direction has to be up or down 
        and vice versa
        '''

        while (random_direction[0] == -last_direction[0] and random_direction[1] == -last_direction[1] or
             random_direction[0] == last_direction[0] and random_direction[1] == last_direction[1]):

            random_direction = directions[math.floor(random.random() * len(directions))] 

            print("Chosen random direction = ", random_direction)
        
        random_length = math.ceil(random.random() * max_length) # length the next tunnel will be (max of max_length)
        tunnel_length = 0 # current length of tunnel being created

        # loop until our tunnel is long enough or until we hit an edge
        while (tunnel_length < random_length):

            # break the loop if it is going out of the map
            if (current_row == 0 and random_direction[0] == -1 or 
                current_column == 0 and random_direction[0] == -1 or 
                current_row == dimensions - 1 and random_direction[0] == 1 or 
                current_column == dimensions - 1 and random_direction[1] == 1):
                
                print("While loop now breaking")

                break

            else:
                map[current_row][current_column] = 0 #set the value of the index in map to 0 (a tunnel, making it one longer)
                current_row += random_direction[0] #add the value from randomDirection to row and col (-1, 0, or 1) to update our location
                current_column += random_direction[1]
                tunnel_length += 1 # the tunnel is now 1 longer

                print("The new current row = ", current_row)
                print("The new current column = ", current_column)

                
        
        if (tunnel_length > 0): 
            last_direction = random_direction # set the last direction so we can remember which way we went
            max_tunnels =- 1 # a tunnel has been created so we decrement how many we have left to create

    print("Closing program")
    n = 0
    for x in map:
        print (map[n])
        n += 1
    return map

# this is a pre-built map to then eventually be replaced by
# a procedural generation machine


createMap()

def printMap():
    
    print("----------     ----------     ----------")
    print("|        |     |        |     |        |")
    print("|        |     |        |     |        |")
    print("|        |     |        |     |        |")
    print("|        |     |        |     |        |")
    print("---    ---     ---    ---     ---    ---")
    print("---    ---     ---    ---     ---    ---")
    print("|        |     |        |     |        |")
    print("|        |     |                       |")
    print("|        |     |                       |")
    print("|        |     |        |     |        |")
    print("---    ---     ---    ---     ---    ---")
    print("---    ---     ---    ---     ---    ---")
    print("|        |     |        |     |        |")
    print("|   ()                  |     |        |")
    print("|                       |     |        |")
    print("|        |     |        |     |        |")
    print("----------     ----------     ----------")
    
    pass

#map_list = ['']

#printMap()
