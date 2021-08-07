from game_scripts import game_text
from player_scripts import player_main_script
from game_scripts import map

def checkInput(player_input):
    
    # TO DO: Implement a Try/Except statement
    valid_input = False

    
    while valid_input == False:
        
        player_input = player_input.lower()

        if player_input == 'help':
            
            game_text.helpScreen()
            valid_input = True
        elif player_input == 'north':
            valid_input = True
            return 'north'

        elif player_input == 'south':
            valid_input = True
            return 'south'
            
        elif player_input == 'east':
            valid_input = True
            return 'east'

        elif player_input == 'west':
            valid_input = True
            return 'west'

        elif player_input == 'escape':
            return True

        elif player_input == 'walk':
            return 'walk'

        elif player_input == 'stay':
            return 'stay'
        
        elif player_input == 'map':
            return 'map'

        else:
            player_input = input("That was not a valid input, please try again:")
            

def walk(player1):
    print("\tYour current location is {0}".format(player1.location))

    player_direction = checkInput(input("\nWhere would you like to go?: "))

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
