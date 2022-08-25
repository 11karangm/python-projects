import math
import random


class Player:
    def __init__(self,letter):
        self.letter = letter

    def get_move(self,game):
        pass

class RandomComputerPLayer(Player):
    def __init__(self,letter):
        self.letter = letter

    def get_move(self,game):
        print("entered computer get move")
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self,letter):
        self.letter = letter

    def get_move(self,game):
        
        print("entered player get move")
        val = None
        square = input(self.letter + "\' s turn. Input move (0-9):")
        try:
            val = int(square)
            if val not in game.available_moves():
                raise ValueError
        except ValueError:
            print("Invalid square. Try again")
        return val