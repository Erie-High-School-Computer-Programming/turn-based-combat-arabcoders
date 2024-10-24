class Player:
    def __init__(self, name, attack, defense, health, movelist ):
        
        """This method initializes the character
        It should give the character a name, attack, defense, and health stat
        It should also give the character a movelist"""
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health
        self.hp = 100
        #self.movelist = {}
        self.movelist = movelist

    def attack(self, move, target):
        """This method should allow the character to attack another character using the 
        selected move. The move should deal damage to the target character"""
        print(self.movelist[move])
        target.health -= self.movelist[move]
        print(target.health)
        return target.health

    def display_stats(self):
        """This method should display the current health of the character"""
        print(self.health)
        return self.health 