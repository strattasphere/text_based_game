
# WEAPON SCRIPTS AND DATA

class MagicAbility():

    def __init__(self, name):
        self.name = name
    

    def resurrect(self):
        pass

    def fireball(self):
        pass

    def cripple(self):
        pass


# each weapon has a damage and speed value in a tuple (dmg, spd_mod)
weapon_dict = {'rusty blade' : (2, -1), 'glass bottle': (1, +1),\
        'deadly spear': (3, 0), "necromancer's blade": (4, +2),\
        'greatsword': (4, -2)}

# each item has an effect value (ev) and 
# buff value (bv) and debuff value (dv) in a tuple (ev, bv, dv)
item_dict = {'potion' : (35, 0, 0)}

armour_dict = {'leather armour': 3}

fireball = MagicAbility('fireball')
resurrect = MagicAbility('resurrect')
cripple = MagicAbility('cripple')

# each magic ability has an effect name which is a class of ability
magic_abilities = [fireball, resurrect, cripple]

