
# This is the script you run to play the game
# It calls in scripts in other folders to make it more manageable to read

# Start game

from player_scripts import player_main_script
from game_scripts import game_text
from game_scripts import user_inputs
from game_scripts import map
from game_scripts import created_maps
from game_scripts import fight_mechanics




# WELCOME SCREEN

game_text.welcomeScreen()

# INITIALISE MAP

#player_map = map.Map()

player_map_array = created_maps.map_a

# INITIALISE PLAYER

player_location = [18,9]

player_name = input("\nWhat is your name?: ")

player1 = player_main_script.Player(player_name, player_location)

print ("\nYour name is:", player1.name)

# ********************************************************************

# INTRODUCTION

print("To navigate this world, you must type in commands\
 and explore to find treasures, new weapons\nand your way to defeating the Necromancer.")
print("\nHere are a list of the commands you will need to use.\
    \n\nYou can access this at any time by typing 'Help' into the command bar.\
    \n\nTry it now.")

user_inputs.checkInput(input("\nType 'Help': "), player1, player_map_array)
print("")

print("\nYou have arrived in the entrance of the city")

# ********************************************************************

# TOTAL PLAYER CONTROL STARTS

escape = False
fight_active = True

while escape != True:

    print("\nWhat would you like to do now?")

    player_input = user_inputs.checkInput(input(), player1, player_map_array)

    if player_input == "fight":
        fight_active = True

    while fight_active == True:
        
        fight_mechanics.showPlayerUI(player1)

        fight_active = False

    user_inputs.showMap(player_map_array, player1.location)

    if player_input == True:
        escape = True
    
        
print("GAME OVER\n\nThanks for playing, {0}!".format(player_name))



fight_mechanics.printthing(player1)