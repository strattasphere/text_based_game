
# The Map

from numpy import array
import math
import random

# Procedural generation of the map happens here

class MapObject:
    
    def __init__(self, loc_id, env):
        self.loc_id = loc_id # the (x,y) value of the location
        self.env = env # the biome type of the room ()

        # the status of the walls (door_open, door_locked, wall)
        self.right_bound_open = False
        self.left_bound_open = False
        self.top_bound_open = False
        self.bottom_bound_open = False
        '''
        self.right_bound = right_bound
        self.left_bound = left_bound
        self.top_bound = top_bound
        self.bottom_bound = bottom_bound
       '''

class Map:
    
    def __init__(self):
        self.dimensions = 20
        self.max_tunnels = 20
        self.max_length = 8

    def create2DArray(self, num):
        
        array2D = [[] for pos in range(self.dimensions)] 
        x = 0
        for list in array2D:
            for elem in range(0, self.dimensions):
                array2D[x].append(num) 
            x += 1

        return array2D

    def getStartLocation(self):
        pass

''' 
1. A function randomly generates a series of map objects that fit work with each other
2. These objects are put into a list
3. The list is printed in order combining the map objects to show a map
'''

# Procedural generation
def createMap():
    '''
    dimensions = 20 # width and height of the map
    max_tunnels = 20 # max number of tunnels possible
    max_length = 8 # max length each tunnel can have
    '''

    # create a 2D array (or list of lists) of 1's
    new_map = Map()
    
    map_array = new_map.create2DArray(1)

    current_row = math.floor(random.random() * new_map.dimensions) # our current row starting at a random row
    current_column = math.floor(random.random() * new_map.dimensions) # our current column starting at a random column

    #print("Starting row =", current_row)
    #print("Starting column =", current_column)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # array to get a random direction, up, down, left, right
    last_direction = [0,0] # saves the last direction we went
    random_direction = [0,0]

    # Create some tunnels

    while new_map.max_tunnels > 0 and new_map.dimensions > 0 and new_map.max_length > 0:

        #print("\nMax tunnels =", max_tunnels)
        #print("Dimensions =", dimensions)
        #print("Max_length =", max_length)

        #print ("\nCreating tunnels has started")

        '''
        Gets a random directions until it is perpendicular to our last_direction
        if the last direction = left or right,
        then our new direction has to be up or down 
        and vice versa
        '''

        while (random_direction[0] == -last_direction[0] and random_direction[1] == -last_direction[1] or
             random_direction[0] == last_direction[0] and random_direction[1] == last_direction[1]):

            random_direction = directions[math.floor(random.random() * len(directions))] 

            #print("\nChosen random direction = ", random_direction)
        
        random_length = math.ceil(random.random() * new_map.max_length) # length the next tunnel will be (max of max_length)
        if random_length == 0:
            random_length += 1

        tunnel_length = 0 # current length of tunnel being created

        # loop until our tunnel is long enough or until we hit an edge
        while (tunnel_length < random_length):

            #print("\n\tLooping until tunnel is long enough")

            # break the loop if it is going out of the map
            if (current_row == 0 and random_direction[0] == -1 or 
                current_column == 0 and random_direction[1] == -1 or 
                current_row == new_map.dimensions - 1 and random_direction[0] == 1 or 
                current_column == new_map.dimensions - 1 and random_direction[1] == 1):
                
                #print("\n\tMap going out of bounds\n\tWhile loop now breaking")

                break

            else:
                map_array[current_row][current_column] = 0 #set the value of the index in map to 0 (a tunnel, making it one longer)
                current_row += random_direction[0] #add the value from randomDirection to row and col (-1, 0, or 1) to update our location
                current_column += random_direction[1]
                tunnel_length += 1 # the tunnel is now 1 longer

                #print("\nThe new current row = ", current_row)
                #print("\nThe new current column = ", current_column)
                #print("\nTunnel length is now =", tunnel_length)

            #printMap(map)
        
        if (tunnel_length >= 0): 
            last_direction = random_direction # set the last direction so we can remember which way we went
            new_map.max_tunnels -= 1 # a tunnel has been created so we decrement how many we have left to create

            #print("The new max tunnels is =", max_tunnels)
            #print("The last direction is =", last_direction)


    #print("\n\tClosing program\n")
    
    n = 0
    for x in map_array:
        print (map_array[n])
        n += 1

    return map_array


def printMap(map, player_loc):
    
    print()

    found_player = False
    map_x = 0
    map_y = 0

    for y_axis in map:

        print_string = ""
        map_x = 0

        for x_axis in y_axis:
            
            if (x_axis == 0 and found_player == False and player_loc[0] == map_x and player_loc[1] == map_y):
                print_string = print_string + " " + "[P]"
                found_player = True

            elif x_axis == 0:
                print_string = print_string + " " + "[ ]"

            elif x_axis == 1:
                print_string = print_string + " " + "   "
            
            map_x += 1

        map_y += 1
        
        print(print_string)
    
    print(found_player)
    
#created_map = createMap()

#printMap(created_map)


#******* TEST *******

'''test_map = [[0,0,1,0,1],[1,0,1,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
player_location = [1,1]

printMap(test_map, player_location)'''


#******* TEST *******
