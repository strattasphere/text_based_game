from game_scripts import game_text
from player_scripts import player_main_script
from game_scripts import map

def checkInput(player_input, player, player_map_array):
    
    # TO DO: Implement a Try/Except statement
    valid_input = False

    
    while valid_input == False:
        
        player_input = player_input.lower()

        if player_input == 'help':
            
            game_text.helpScreen()
            valid_input = True
        elif player_input == 'north' or player_input == 'walk north' or player_input == 'walk up'  or player_input == 'up':
            valid_input = True
            player.moveLocation(player_input, player_map_array)
            
            return 'north' 

        elif player_input == 'south' or player_input == 'walk south' or player_input == 'walk down' or player_input == 'down':
            valid_input = True
            player.moveLocation(player_input, player_map_array) 
            
            return 'south' 

        elif player_input == 'east' or player_input == 'walk east' or player_input == 'walk right' or player_input == 'right':
            valid_input = True
            player.moveLocation(player_input, player_map_array) 

            return 'east' 

        elif player_input == 'west' or player_input == 'walk west' or player_input == 'walk left' or player_input == 'left':
            valid_input = True
            player.moveLocation(player_input, player_map_array) 

            return 'west' 

        elif player_input == 'escape':
            return True

        elif player_input == 'walk' or player_input == 'wwalk' or player_input == 'waalk' or player_input == 'wakl':
            return 'walk'

        elif player_input == 'stay' or player_input == 'sstay' or player_input == 'staay' or player_input == 'stayss':
            return 'stay'
        
        elif player_input == 'map' or player_input == 'maps' or player_input == 'maaps':
            return 'map'

        else:
            player_input = input("That was not a valid input, please try again: ")
            

def walk(player1, player_map_array):
    print("\tYour current location is {0}".format(player1.location))

    player_direction = checkInput(input("\nWhere would you like to go?: "), player1, player_map_array)

    player1.moveLocation(player_direction.lower())

    print("\n\tYou are now at location {0}".format(player1.location))

    checkLocation(player1)

def checkLocation(player1):
    
    if player1.location[0] == 1 and player1.location[1] == 2:
        print ("\n\tYOU HAVE FOUND THE NECROMANCER")

        # sets found_necro = True

def showMap(player_map, player_loc):

    print ("\n\tHere is the map")

    map.printMap(player_map, player_loc)
