
# Fight mechanics


from player_scripts import player_main_script
from game_scripts import enemies
from game_scripts import user_inputs
from game_scripts import weapon_scripts

turn_counter = 0
enemies_list = [enemies.necromancer, enemies.zombie_guard, enemies.zombie_guard_capt]
player_action = ''
player_target = ''

# display 'UI' (player and stats, all enemies and stats)

def showPlayerUI(player):
    
    player_potions_count = player.playerPotionsCount()
    
    
    print("_________________________________________________________________________")
    print("|\n|\t\t\tPLAYER")
    print("|\t\tHealth:{0}/{1}\n|".format(player.current_health, player.max_health))
    print("|\t\tAvailable actions: {0}".format(player.current_weapon))
    print("|\n\t\t\tFight: {0}".format(player.active_weapon))
    print("|\t\t\tUse potion: {0} remaining".format(player_potions_count))
    print("|\n|\t\tChoose action (type 'fight' or 'use potion' or\n'switch weapon')")
    print("_________________________________________________________________________")
    print("\n_________________________________________________________________________")
    
    showEnemiesUI()

    player_action = user_inputs.checkFightInput(input())
    player_target = user_inputs.checkTargetInput(input())


def showEnemiesUI():

    enemy_counter = 0

    print("\n\n|\t\t\tENEMIES")
    for enemy in enemies_list:
        enemy_counter += 1
        print("|\n|\t\t{1} - {0}\t\tHealth : {2}/{3}".\
            format(enemy.name, enemy_counter,enemy.health_remaining,enemy.max_health))
    print("_________________________________________________________________________")
    print("_________________________________________________________________________")

def fight(player):

    if player_action == 'fight':
        
        for enemy in enemies_list:
            if enemy.name == player_target:
                enemy.health_remaining -= weapon_scripts.weapon_dict[player.active_weapon][0] 

    showEnemiesUI()


# character with highest speed gets first turn

# if player, player chooses action they want to take and chooses target of action

# action applies effect on target

# if enemy character has higher speed, they choose what action to use at random

# applies effect of action to target
