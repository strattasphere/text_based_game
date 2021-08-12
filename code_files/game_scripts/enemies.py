
# enemies

class Enemy():

    def __init__(self, enemy_name, health, speed, weapon, *magic_ability): # * = creates tuple of the arguments
        self.enemy_name = enemy_name
        self.health = health
        self.speed = speed
        self.weapon = weapon
        self.magic_ability = magic_ability

    def attackPlayer(self):
        pass



# the drunkard

drunkard = Enemy('The Drunkard', 4, 3, 'glass bottle')

# the zombie guard

zombie_guard = Enemy('Zombie Guard', 6, 4, 'rusty blade')

# the zombie guard captain

zombie_guard_capt = Enemy('Zombie Guard Captain', 7, 5, 'deadly spear', 'cripple')

# the necromancer

necromancer = Enemy('Necromancer', 10, 7, "necromancer's blade", 'fireball', 'resurrect' )

print(necromancer.enemy_name)
print(type(necromancer.magic_ability))