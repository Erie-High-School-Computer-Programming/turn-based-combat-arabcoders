# Create a game that allows players to choose between multiple characters
# and fight against each other. The game should have a simple combat system
# where characters can deal damage to each other. The game should also have
# a way to display the current health of each character.

# The game should have turned based combat where each player takes turns
# Players should have an attack, defense, and health stat

# Combat should involve a level of randomness.

# The game should have a way to display the current health of each character after each turn.

# Combat should continue until one of the characters health reaches 0.

# The game should have a way to display the winner of the game.

# The game should have a way to restart the game.

# The game should have a way to exit the game.
import sys

from player import Player

class Game:
    def __init__(self, players, moves):
        """Initializes the game,
        It should give the game a list of at least 4 characters to choose from
        It should also give the game a list of m oves for each character
        It should show player a list of characters to choose from
        and allow them to select a character,
        then have the computer choose a character at random
        It should randomly select a player to go first"""
        self.players = [ "Knight", "Orc", "Mage", "Thief"]
        self.moves = { "FireBall": 50, "Slap": 25 }
        self.current_turn = 0
        self.player = None
        self.computer = None
        self.turn = 0
        self.winner = None


    def turn(self, current_turn):
        """ ayers, 
        and allow the player to select a move to use on the opponent
        If it is the computer player's turn, it should select a move at random"""
        return self.current_turn
        

    def check_winner(self):
        """This method should check if either player's health has reached 0
        If a player's health has reached 0, it should display the winner"""
        if self.player <= 0:
            print("Computer wins")
        elif self.computer <= 0:
            print("Player wins")
        else:
            print("It's a tie")

    def restart(self):
        """This method should allow the player to restart the game"""
        if self.player <= 0 or self.computer <= 0:
            self.player = 100
            self.computer = 100
            self.turn = 0
            self.winner = None
            print("Game has been restarted")
        else:
            print("Game is still ongoing")

        

    def exit(self):
        """This method should allow the player to exit the game"""
        sys.exit()

    
def main():
    game = Game()
    game.turn(1)
    game.check_winner()
    game.turn(2)
    game.check_winner() 

main()