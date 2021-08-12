from game_scripts import game_text
from player_scripts import player_main_script
from game_scripts import map
import os


def checkInput(player_input, player, player_map_array):
    
    os.system('cls' if os.name == 'nt' else 'clear')

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
            player.checkLocation()
            
            
        elif player_input == 'south' or player_input == 'walk south' or player_input == 'walk down' or player_input == 'down':
            valid_input = True
            player.moveLocation(player_input, player_map_array)  
            player.checkLocation()
            

        elif player_input == 'east' or player_input == 'walk east' or player_input == 'walk right' or player_input == 'right':
            valid_input = True
            player.moveLocation(player_input, player_map_array) 
            player.checkLocation()
            

        elif player_input == 'west' or player_input == 'walk west' or player_input == 'walk left' or player_input == 'left':
            valid_input = True
            player.moveLocation(player_input, player_map_array) 
            player.checkLocation()
            

        elif player_input == 'escape':
            return True

        elif player_input == 'walk' or player_input == 'wwalk' or player_input == 'waalk' or player_input == 'wakl':
            valid_input = True
            walk(player, player_map_array)

        elif player_input == 'stay' or player_input == 'sstay' or player_input == 'staay' or player_input == 'stayss':
            valid_input = True
            print("You have stood still")
        
        elif player_input == 'map' or player_input == 'maps' or player_input == 'maaps':
            valid_input = True
            showMap(player_map_array, player.location)
            
            

        else:
            player_input = input("That was not a valid input, please try again: ")
            

def checkValidInput(player_input):
    
    valid_input = False

    while valid_input == False:
        
        player_input = player_input.lower()

        if player_input == 'fight':
            valid_input = True
            return 'fight'
        elif player_input == 'use potion':
            valid_input = True
            return 'use potion' 
        elif player_input == 'switch weapon':
            valid_input = True
            return 'switch weapon'
            
            
        else:
            player_input = input("That was not a valid input, please try again: ")



def walk(player1, player_map_array):
    print("\tYour current location is {0}".format(player1.location))

    player_direction = checkInput(input("\nWhere would you like to go?: "), player1, player_map_array)

    player1.moveLocation(player_direction.lower())

    #print("\n\tYou are now at location {0}".format(player1.location))

    player1.checkLocation()


def showMap(player_map, player_loc):

    print ("\n\tHere is the map, your locaiton is:,", player_loc)

    print ("\n\tHere is the map.")

    map.printMap(player_map, player_loc)






'''def checkLocation(player1):
    
    if player1.location[0] == 1 and player1.location[1] == 2:
        print ("\n\tYOU HAVE FOUND THE NECROMANCER")

        # sets found_necro = True'''