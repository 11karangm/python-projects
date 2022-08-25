import math
import random


class Player:
    def __init__(self,letter):
        self.letter = letter

    def get_move():
        pass

class HumanPlayer:
    def __init__(self,letter):
        self.letter = letter

    def get_move(self,gameone):
         val = int(input("Enter your move (0-8): "))
         try:
            if val not in gameone.available_moves():
                raise ValueError
         except:
            print("Invalid move , try again")

         return val


class RandomComputerPlayer:
    def __init__(self,letter):
        self.letter = letter

    def get_move(self,gameone):
        val = random.choice(gameone.available_moves())

        return val
