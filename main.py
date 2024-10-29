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
import random

class Player:
    def __init__(self, name, health, attack, defense, moves):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.moves = moves

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        """Initializes the game,
        It should give the game a list of at least 4 characters to choose from
        It should also give the game a list of moves for each character
        It should show player a list of characters to choose from
        and allow them to select a character,
        then have the computer choose a character at random
        It should randomly select a player to go first"""
        self.characters = [
            Player("Knight", 100, 20, 10, {"Sword Strike": {"damage": 35, "accuracy": 90}, "Shield Bash": {"damage": 20, "accuracy": 95}}),
            Player("Orc", 120, 25, 5, {"Axe Swing": {"damage": 40, "accuracy": 80}, "Headbutt": {"damage": 30, "accuracy": 85}}),
            Player("Mage", 80, 30, 5, {"FireBall": {"damage": 50, "accuracy": 70}, "Magic Blast": {"damage": 40, "accuracy": 75}}),
            Player("Thief", 90, 15, 15, {"Arrow Shot": {"damage": 30, "accuracy": 85}, "Backstab": {"damage": 25, "accuracy": 90}})
        ]

        self.player = None
        self.computer = None
        self.turn = 0
        self.winner = None
        self.setup_game()

    def setup_game(self):
        print("Choose your character:")
        for i, character in enumerate(self.characters):
            print(f"{i + 1}. {character.name}")
        choice = int(input("Enter the number of your choice: ")) - 1
        self.player = self.characters[choice]
        self.computer = random.choice(self.characters)
        print(f"You chose {self.player.name}. The computer chose {self.computer.name}.")
        self.turn = random.choice([0, 1])

    def take_turn(self):
        """Players take turns,
        and allow the player to select a move to use on the opponent
        If it is the computer player's turn, it should select a move at random"""
        if self.turn == 0:
            print("Your turn:")
            while True:
                move = input(f"Choose your move ({'/'.join(self.player.moves.keys())}): ")
                if move in self.player.moves:
                    move_details = self.player.moves[move]
                    if random.randint(1, 100) <= move_details["accuracy"]:
                        self.computer.take_damage(move_details["damage"])
                        print(f"You used {move}. {self.computer.name} took {move_details['damage']} damage.")
                    else:
                        print(f"You used {move}. It missed!")
                    break
                else:
                    print("You entered an invalid move name. Please try again.")
        else:
            print("Computer's turn:")
            move = random.choice(list(self.computer.moves.keys()))
            move_details = self.computer.moves[move]
            if random.randint(1, 100) <= move_details["accuracy"]:
                self.player.take_damage(move_details["damage"])
                print(f"Computer used {move}. You took {move_details['damage']} damage.")
            else:
                print(f"Computer used {move}. It missed!")
        self.turn = 1 - self.turn

    def check_winner(self):
        """This method should check if either player's health has reached 0
        If a player's health has reached 0, it should display the winner"""
        if not self.player.is_alive():
            print("Computer wins")
            self.winner = "Computer"
        elif not self.computer.is_alive():
            print("Player wins")
            self.winner = "Player"
        else:
            print(f"Player health: {self.player.health}, Computer health: {self.computer.health}")

    def restart(self):
        """This method should allow the player to restart the game"""
        self.player.health = 100
        self.computer.health = 100
        self.turn = 0
        self.winner = None
        print("Game has been restarted")

    def exit(self):
        """This method should allow the player to exit the game"""
        sys.exit()

def main():
    game = Game()
    while True:
        game.take_turn()
        game.check_winner()
        if game.winner:
            break
    if input("Do you want to restart the game? (yes/no): ").lower() == "yes":
        game.restart()
        main()
    else:
        game.exit()

main()
