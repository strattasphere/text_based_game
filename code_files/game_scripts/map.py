
# The Map

# Procedural generation of the map happens here


# the map class stores the data about the map objects
class Map:
    
    def __init__(self, x_value, y_value):
        self.x_value = x_value
        self.y_value = y_value
        self.mapObjList = [] # a list of all the map objects


    def printMap(mapObjList):

        for obj in mapObjList:
        
            pass
    


# defines what the contents of map object contains
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


# a function that creates a map from map objects and appends them to a list
# this determines which map objects are at the edge of the map,
# and which are inside so can have open walls
# then decides on a path to the goal and builds map around that 
def createMap():
    
    # determine map size
    # if map object at edge, edge side bounds are closed
    # 
    
    pass


# this is a pre-built map to then eventually be replaced by
# a procedural generation machine




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

map_list = ['']

printMap()