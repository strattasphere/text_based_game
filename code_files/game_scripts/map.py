
# The Map

# Procedural generation of the map happens here

class Map:
    
    def __init__(self):
        self.loc_id = room_id # the (x,y) value of the location
        self.env = env # the biome type of the room ()

        # the status of the walls (door_open, door_locked, wall)
        self.right_wall = right_wall
        self.left_wall = left_wall
        self.up_wall = up_wall
        self.down_wall = down_wall

        def showBounds(): # print function
            pass

        def destroyBound():
            pass

        def openBound():
            pass

        def closeBound():
            pass



    

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