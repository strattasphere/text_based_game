
# enemies

class Enemy():

    def __init__(self, name, max_health, speed, weapon, *magic_ability): # * = creates tuple of the arguments
        self.name = name
        self.health_remaining = max_health
        self.max_health = max_health
        self.speed = speed
        self.weapon = weapon
        self.magic_ability = magic_ability
        self.flavour = ""

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
