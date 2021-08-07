
# This is the script you run to play the game
# It calls in scripts in other folders to make it more manageable to read

# Start game

from player_scripts import player_main_script
from game_scripts import game_text
from game_scripts import user_inputs
from game_scripts import map

escape = False

# WELCOME SCREEN

game_text.welcomeScreen()

# INITIALISE PLAYER

player_name = input("\nWhat is your name?: ")

player1 = player_main_script.Player(player_name)

print ("\nYour name is:", player1.name)

player_map = map.createMap()

print(type(player_map))

# ********************************************************************

# INTRODUCTION

print("To navigate this world, you must type in commands\
 and explore to find treasures, new weapons\nand your way to defeating the Necromancer.")
print("\nHere are a list of the commands you will need to use.\n\nYou can access this at any time by typing 'Help' into the command bar.\n\nTry it now.")

user_inputs.checkInput(input("\nType 'Help': "))
print("")

print("\nYou have arrived in the entrance of the city")

user_inputs.walk(player1)

# TOTAL PLAYER CONTROL STARTS

while escape != True:

    print("\nWhat would you like to do now?")

    player_input = user_inputs.checkInput(input())

    if player_input == True:
        escape = True
    
    elif player_input == 'walk':

        user_inputs.walk(player1)

    elif player_input == 'map':

        user_inputs.showMap(player1.location, player_map)




    


print("GAME OVER")



