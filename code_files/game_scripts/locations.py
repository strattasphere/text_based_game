

# base class which each location is based off of
class GameLocation():

    def __init__(self, location,loc_name, enemies_alive = False):
        self.location = location
        self.loc_name = loc_name
        self.enemies_list = 0
        self.enemies_alive = enemies_alive



    def enemiesAttack(self):
        pass


# the tavern
tavern = GameLocation([15,6], 'The Tavern')

# the black smith
blacksmth_loc = GameLocation([11,12], 'The Blacksmith')

# the church
church_loc = GameLocation([7,6], 'The Church')

# the guard tower
guard_twr_loc = GameLocation([4,9], 'The Guard Tower')

# the keep
keep_loc = GameLocation([1,9], 'THE KEEP')
